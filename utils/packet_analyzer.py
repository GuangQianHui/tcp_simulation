#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scapy.all import *
import logging

logger = logging.getLogger(__name__)

class PacketAnalyzer:
    @staticmethod
    def analyze_tcp_packet(packet):
        """分析TCP数据包"""
        if packet.haslayer(TCP):
            # 获取TCP层信息
            tcp = packet[TCP]
            
            # 分析TCP标志
            flags = []
            if tcp.flags & 0x01:  # FIN
                flags.append("FIN")
            if tcp.flags & 0x02:  # SYN
                flags.append("SYN")
            if tcp.flags & 0x04:  # RST
                flags.append("RST")
            if tcp.flags & 0x08:  # PSH
                flags.append("PSH")
            if tcp.flags & 0x10:  # ACK
                flags.append("ACK")
            if tcp.flags & 0x20:  # URG
                flags.append("URG")
            
            # 打印数据包信息
            logger.info(f"TCP数据包分析:")
            logger.info(f"源IP: {packet[IP].src}")
            logger.info(f"目标IP: {packet[IP].dst}")
            logger.info(f"源端口: {tcp.sport}")
            logger.info(f"目标端口: {tcp.dport}")
            logger.info(f"序列号: {tcp.seq}")
            logger.info(f"确认号: {tcp.ack}")
            logger.info(f"TCP标志: {' '.join(flags)}")
            
            return {
                'src_ip': packet[IP].src,
                'dst_ip': packet[IP].dst,
                'sport': tcp.sport,
                'dport': tcp.dport,
                'seq': tcp.seq,
                'ack': tcp.ack,
                'flags': flags
            }
        return None

    @staticmethod
    def capture_packets(interface=None, count=0, timeout=None):
        """捕获数据包"""
        try:
            packets = sniff(iface=interface, count=count, timeout=timeout)
            return packets
        except Exception as e:
            logger.error(f"捕获数据包时发生错误: {str(e)}")
            return []

    @staticmethod
    def save_pcap(packets, filename):
        """保存数据包到pcap文件"""
        try:
            wrpcap(filename, packets)
            logger.info(f"数据包已保存到 {filename}")
        except Exception as e:
            logger.error(f"保存数据包时发生错误: {str(e)}") 