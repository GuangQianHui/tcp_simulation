"""
TCP协议仿真工具的配置管理模块
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class TCPConfig:
    """TCP配置类"""
    src_ip: str
    dst_ip: str
    src_port: Optional[int] = None
    dst_port: int = 80
    seq: Optional[int] = None
    ack: int = 0
    window: int = 65535
    debug: bool = False

@dataclass
class LogConfig:
    """日志配置类"""
    log_level: str = "INFO"
    log_file: str = "logs/tcp_simulation.log"
    capture_file: str = "logs/packet_capture.pcap"

@dataclass
class AppConfig:
    """应用配置类"""
    tcp: TCPConfig
    log: LogConfig = LogConfig() 