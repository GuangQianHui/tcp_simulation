#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import List, Dict, Any
from scapy.all import IP
import logging

logger = logging.getLogger(__name__)

class PacketObserver(ABC):
    """数据包观察者基类"""
    
    @abstractmethod
    def update(self, packet: IP, event_type: str, **kwargs) -> None:
        """更新观察者状态"""
        pass

class LoggingObserver(PacketObserver):
    """日志观察者"""
    
    def update(self, packet: IP, event_type: str, **kwargs) -> None:
        """记录数据包事件"""
        logger.info(f"事件类型: {event_type}")
        logger.info(f"数据包: {packet.summary()}")
        for key, value in kwargs.items():
            logger.info(f"{key}: {value}")

class PacketCaptureObserver(PacketObserver):
    """数据包捕获观察者"""
    
    def __init__(self):
        self.captured_packets: List[IP] = []
    
    def update(self, packet: IP, event_type: str, **kwargs) -> None:
        """捕获数据包"""
        self.captured_packets.append(packet)
    
    def get_captured_packets(self) -> List[IP]:
        """获取捕获的数据包"""
        return self.captured_packets

class PacketAnalyzerObserver(PacketObserver):
    """数据包分析观察者"""
    
    def __init__(self):
        self.analysis_results: List[Dict[str, Any]] = []
    
    def update(self, packet: IP, event_type: str, **kwargs) -> None:
        """分析数据包"""
        if packet.haslayer(TCP):
            analysis = {
                'event_type': event_type,
                'src_ip': packet[IP].src,
                'dst_ip': packet[IP].dst,
                'sport': packet[TCP].sport,
                'dport': packet[TCP].dport,
                'seq': packet[TCP].seq,
                'ack': packet[TCP].ack,
                'flags': packet[TCP].flags
            }
            self.analysis_results.append(analysis)
    
    def get_analysis_results(self) -> List[Dict[str, Any]]:
        """获取分析结果"""
        return self.analysis_results

class Subject:
    """主题类"""
    
    def __init__(self):
        self._observers: List[PacketObserver] = []
    
    def attach(self, observer: PacketObserver) -> None:
        """添加观察者"""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: PacketObserver) -> None:
        """移除观察者"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, packet: IP, event_type: str, **kwargs) -> None:
        """通知所有观察者"""
        for observer in self._observers:
            observer.update(packet, event_type, **kwargs) 