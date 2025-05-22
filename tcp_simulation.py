#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scapy.all import *
import time
import sys
import logging
import argparse
import os
from utils.packet_analyzer import PacketAnalyzer
from config import DEFAULT_CONFIG, TCP_FLAGS

# 配置日志
logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TCPSimulation:
    def __init__(self, config=None):
        """初始化TCP仿真器"""
        self.config = config or DEFAULT_CONFIG
        self.src_ip = self.config['src_ip']
        self.dst_ip = self.config['dst_ip']
        self.src_port = self.config['src_port']
        self.dst_port = self.config['dst_port']
        self.seq = self.config['initial_seq']
        self.ack = 0
        self.packet_analyzer = PacketAnalyzer()
        self.captured_packets = []

    def create_tcp_packet(self, flags, seq=None, ack=None, payload=None):
        """创建TCP数据包"""
        if seq is None:
            seq = self.seq
        if ack is None:
            ack = self.ack
            
        packet = IP(src=self.src_ip, dst=self.dst_ip)/TCP(
            sport=self.src_port,
            dport=self.dst_port,
            flags=flags,
            seq=seq,
            ack=ack
        )
        
        if payload:
            packet = packet/Raw(load=payload)
            
        return packet

    def send_and_capture(self, packet, description):
        """发送数据包并捕获响应"""
        logger.info(f"发送{description}包")
        send(packet, verbose=0)
        self.captured_packets.append(packet)
        
        # 捕获响应
        response = sniff(
            iface=self.config['interface'],
            count=1,
            timeout=2,
            filter=f"host {self.src_ip} and host {self.dst_ip}"
        )
        
        if response:
            self.captured_packets.extend(response)
            self.packet_analyzer.analyze_tcp_packet(response[0])
        
        time.sleep(self.config['packet_delay'])

    def three_way_handshake(self):
        """模拟TCP三次握手"""
        logger.info("开始TCP三次握手过程...")
        
        # 第一次握手：SYN
        syn_packet = self.create_tcp_packet('S')
        self.send_and_capture(syn_packet, "SYN")
        
        # 第二次握手：SYN-ACK
        syn_ack_packet = self.create_tcp_packet('SA', seq=self.seq+1, ack=self.seq+1)
        self.send_and_capture(syn_ack_packet, "SYN-ACK")
        
        # 第三次握手：ACK
        ack_packet = self.create_tcp_packet('A', seq=self.seq+1, ack=self.seq+2)
        self.send_and_capture(ack_packet, "ACK")
        
        logger.info("TCP三次握手完成")

    def four_way_handshake(self):
        """模拟TCP四次挥手"""
        logger.info("开始TCP四次挥手过程...")
        
        # 第一次挥手：FIN
        fin_packet = self.create_tcp_packet('FA', seq=self.seq+1, ack=self.seq+2)
        self.send_and_capture(fin_packet, "FIN")
        
        # 第二次挥手：ACK
        ack_packet = self.create_tcp_packet('A', seq=self.seq+2, ack=self.seq+2)
        self.send_and_capture(ack_packet, "ACK")
        
        # 第三次挥手：FIN
        fin_packet2 = self.create_tcp_packet('FA', seq=self.seq+2, ack=self.seq+2)
        self.send_and_capture(fin_packet2, "FIN")
        
        # 第四次挥手：ACK
        final_ack = self.create_tcp_packet('A', seq=self.seq+2, ack=self.seq+3)
        self.send_and_capture(final_ack, "ACK")
        
        logger.info("TCP四次挥手完成")

    def save_captured_packets(self):
        """保存捕获的数据包"""
        if self.config['save_pcap'] and self.captured_packets:
            self.packet_analyzer.save_pcap(
                self.captured_packets,
                self.config['pcap_filename']
            )

def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='TCP协议仿真工具')
    parser.add_argument('--src-ip', help='源IP地址')
    parser.add_argument('--dst-ip', help='目标IP地址')
    parser.add_argument('--src-port', type=int, help='源端口')
    parser.add_argument('--dst-port', type=int, help='目标端口')
    parser.add_argument('--interface', help='网络接口')
    parser.add_argument('--delay', type=float, help='数据包发送延迟（秒）')
    parser.add_argument('--no-save', action='store_true', help='不保存pcap文件')
    parser.add_argument('--debug', action='store_true', help='启用调试模式')
    
    return parser.parse_args()

def main():
    try:
        # 解析命令行参数
        args = parse_arguments()
        
        # 更新配置
        config = DEFAULT_CONFIG.copy()
        if args.src_ip:
            config['src_ip'] = args.src_ip
        if args.dst_ip:
            config['dst_ip'] = args.dst_ip
        if args.src_port:
            config['src_port'] = args.src_port
        if args.dst_port:
            config['dst_port'] = args.dst_port
        if args.interface:
            config['interface'] = args.interface
        if args.delay:
            config['packet_delay'] = args.delay
        if args.no_save:
            config['save_pcap'] = False
        if args.debug:
            config['log_level'] = 'DEBUG'
        
        # 设置日志级别
        logging.basicConfig(
            level=getattr(logging, config['log_level']),
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        # 创建TCP仿真实例
        tcp_sim = TCPSimulation(config)
        
        # 执行三次握手
        tcp_sim.three_way_handshake()
        time.sleep(2)
        
        # 执行四次挥手
        tcp_sim.four_way_handshake()
        
        # 保存捕获的数据包
        tcp_sim.save_captured_packets()
        
    except KeyboardInterrupt:
        logger.info("程序被用户中断")
        sys.exit(0)
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # 检查是否具有管理员权限
    if os.name == 'posix' and os.geteuid() != 0:
        logger.error("请使用管理员权限运行此程序！")
        sys.exit(1)
        
    main() 