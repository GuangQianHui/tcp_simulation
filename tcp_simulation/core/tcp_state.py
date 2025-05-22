#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Optional, List
from scapy.all import IP
from ..utils.packet_analyzer import PacketAnalyzer

class TCPState(ABC):
    """TCP状态基类"""
    
    def __init__(self, context):
        self.context = context
        self.packet_analyzer = PacketAnalyzer()
    
    @abstractmethod
    def handle_packet(self, packet: IP) -> Optional[IP]:
        """处理数据包"""
        pass
    
    @abstractmethod
    def get_next_state(self) -> 'TCPState':
        """获取下一个状态"""
        pass

class ClosedState(TCPState):
    """关闭状态"""
    
    def handle_packet(self, packet: IP) -> Optional[IP]:
        # 发送SYN包
        return self.context.create_syn_packet()
    
    def get_next_state(self) -> 'TCPState':
        return ListenState(self.context)

class ListenState(TCPState):
    """监听状态"""
    
    def handle_packet(self, packet: IP) -> Optional[IP]:
        # 发送SYN-ACK包
        return self.context.create_syn_ack_packet()
    
    def get_next_state(self) -> 'TCPState':
        return SynReceivedState(self.context)

class SynReceivedState(TCPState):
    """SYN已接收状态"""
    
    def handle_packet(self, packet: IP) -> Optional[IP]:
        # 发送ACK包
        return self.context.create_ack_packet()
    
    def get_next_state(self) -> 'TCPState':
        return EstablishedState(self.context)

class EstablishedState(TCPState):
    """已建立连接状态"""
    
    def handle_packet(self, packet: IP) -> Optional[IP]:
        # 发送FIN包
        return self.context.create_fin_packet()
    
    def get_next_state(self) -> 'TCPState':
        return FinWait1State(self.context)

class FinWait1State(TCPState):
    """等待FIN-1状态"""
    
    def handle_packet(self, packet: IP) -> Optional[IP]:
        # 发送ACK包
        return self.context.create_ack_packet()
    
    def get_next_state(self) -> 'TCPState':
        return FinWait2State(self.context)

class FinWait2State(TCPState):
    """等待FIN-2状态"""
    
    def handle_packet(self, packet: IP) -> Optional[IP]:
        # 发送FIN包
        return self.context.create_fin_packet()
    
    def get_next_state(self) -> 'TCPState':
        return TimeWaitState(self.context)

class TimeWaitState(TCPState):
    """等待时间状态"""
    
    def handle_packet(self, packet: IP) -> Optional[IP]:
        # 发送ACK包
        return self.context.create_ack_packet()
    
    def get_next_state(self) -> 'TCPState':
        return ClosedState(self.context) 