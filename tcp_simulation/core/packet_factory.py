#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scapy.all import IP, TCP, Raw
from typing import Optional, Dict, Any

class PacketFactory:
    """TCP数据包工厂类"""
    
    @staticmethod
    def create_tcp_packet(
        src_ip: str,
        dst_ip: str,
        src_port: int,
        dst_port: int,
        flags: str,
        seq: int,
        ack: int,
        payload: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> IP:
        """
        创建TCP数据包
        
        Args:
            src_ip: 源IP地址
            dst_ip: 目标IP地址
            src_port: 源端口
            dst_port: 目标端口
            flags: TCP标志位
            seq: 序列号
            ack: 确认号
            payload: 数据包负载
            options: TCP选项
            
        Returns:
            IP: 构造的IP数据包
        """
        # 创建TCP层
        tcp_layer = TCP(
            sport=src_port,
            dport=dst_port,
            flags=flags,
            seq=seq,
            ack=ack
        )
        
        # 添加TCP选项
        if options:
            for key, value in options.items():
                setattr(tcp_layer, key, value)
        
        # 创建IP层
        packet = IP(src=src_ip, dst=dst_ip)/tcp_layer
        
        # 添加负载
        if payload:
            packet = packet/Raw(load=payload)
            
        return packet 