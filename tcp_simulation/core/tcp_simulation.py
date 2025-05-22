#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional, Dict, Any
from scapy.all import IP, send, sniff
import time
import logging
from .packet_factory import PacketFactory
from .tcp_state import TCPState, ClosedState
from .observers import Subject, LoggingObserver, PacketCaptureObserver, PacketAnalyzerObserver

logger = logging.getLogger(__name__)

class TCPSimulation(Subject):
    """TCP仿真主类"""
    
    def __init__(self, config: Dict[str, Any]):
        """初始化TCP仿真器"""
        super().__init__()
        self.config = config
        self.src_ip = config['src_ip']
        self.dst_ip = config['dst_ip']
        self.src_port = config['src_port']
        self.dst_port = config['dst_port']
        self.seq = config['initial_seq']
        self.ack = 0
        self.current_state: TCPState = ClosedState(self)
        
        # 初始化观察者
        self.logging_observer = LoggingObserver()
        self.capture_observer = PacketCaptureObserver()
        self.analyzer_observer = PacketAnalyzerObserver()
        
        # 注册观察者
        self.attach(self.logging_observer)
        self.attach(self.capture_observer)
        self.attach(self.analyzer_observer)
    
    def create_syn_packet(self) -> IP:
        """创建SYN包"""
        return PacketFactory.create_tcp_packet(
            self.src_ip, self.dst_ip,
            self.src_port, self.dst_port,
            'S', self.seq, self.ack
        )
    
    def create_syn_ack_packet(self) -> IP:
        """创建SYN-ACK包"""
        return PacketFactory.create_tcp_packet(
            self.src_ip, self.dst_ip,
            self.src_port, self.dst_port,
            'SA', self.seq + 1, self.seq + 1
        )
    
    def create_ack_packet(self) -> IP:
        """创建ACK包"""
        return PacketFactory.create_tcp_packet(
            self.src_ip, self.dst_ip,
            self.src_port, self.dst_port,
            'A', self.seq + 1, self.seq + 2
        )
    
    def create_fin_packet(self) -> IP:
        """创建FIN包"""
        return PacketFactory.create_tcp_packet(
            self.src_ip, self.dst_ip,
            self.src_port, self.dst_port,
            'FA', self.seq + 1, self.seq + 2
        )
    
    def send_and_capture(self, packet: IP, description: str) -> None:
        """发送数据包并捕获响应"""
        # 发送数据包
        send(packet, verbose=0)
        self.notify(packet, f"SEND_{description}")
        
        # 捕获响应
        response = sniff(
            iface=self.config['interface'],
            count=1,
            timeout=2,
            filter=f"host {self.src_ip} and host {self.dst_ip}"
        )
        
        if response:
            self.notify(response[0], f"RECEIVE_{description}")
        
        time.sleep(self.config['packet_delay'])
    
    def run(self) -> None:
        """运行TCP仿真"""
        try:
            logger.info("开始TCP仿真...")
            
            # 执行状态转换
            while True:
                # 处理当前状态
                packet = self.current_state.handle_packet(None)
                if packet:
                    self.send_and_capture(packet, self.current_state.__class__.__name__)
                
                # 转换到下一个状态
                self.current_state = self.current_state.get_next_state()
                
                # 如果回到初始状态，结束仿真
                if isinstance(self.current_state, ClosedState):
                    break
            
            # 保存捕获的数据包
            if self.config['save_pcap']:
                from scapy.all import wrpcap
                wrpcap(self.config['pcap_filename'], self.capture_observer.get_captured_packets())
            
            logger.info("TCP仿真完成")
            
        except Exception as e:
            logger.error(f"仿真过程中发生错误: {str(e)}")
            raise 