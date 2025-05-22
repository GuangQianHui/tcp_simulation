"""
TCP协议仿真工具的接口定义
"""
from abc import ABC, abstractmethod
from typing import Any, Optional

class IPacketFactory(ABC):
    """数据包工厂接口"""
    @abstractmethod
    def create_syn_packet(self, **kwargs) -> Any:
        """创建SYN数据包"""
        pass

    @abstractmethod
    def create_ack_packet(self, **kwargs) -> Any:
        """创建ACK数据包"""
        pass

class ITCPState(ABC):
    """TCP状态接口"""
    @property
    @abstractmethod
    def name(self) -> str:
        """获取状态名称"""
        pass

    @abstractmethod
    def handle_packet(self, packet: Any, event: str) -> 'ITCPState':
        """处理数据包"""
        pass

class IObserver(ABC):
    """观察者接口"""
    @abstractmethod
    def update(self, event: Any) -> None:
        """更新观察者"""
        pass

class ILogger(ABC):
    """日志接口"""
    @abstractmethod
    def info(self, message: str) -> None:
        """记录信息日志"""
        pass

    @abstractmethod
    def error(self, message: str) -> None:
        """记录错误日志"""
        pass

    @abstractmethod
    def debug(self, message: str) -> None:
        """记录调试日志"""
        pass 