"""
TCP协议仿真工具的依赖注入容器
"""
from typing import Dict, Type, Any
from .interfaces import IPacketFactory, ITCPState, IObserver, ILogger

class Container:
    """依赖注入容器"""
    def __init__(self):
        self._services: Dict[Type, Any] = {}

    def register(self, interface: Type, implementation: Any) -> None:
        """注册服务"""
        self._services[interface] = implementation

    def resolve(self, interface: Type) -> Any:
        """解析服务"""
        if interface not in self._services:
            raise KeyError(f"未找到服务: {interface.__name__}")
        return self._services[interface]

    def get_packet_factory(self) -> IPacketFactory:
        """获取数据包工厂"""
        return self.resolve(IPacketFactory)

    def get_tcp_state(self) -> ITCPState:
        """获取TCP状态"""
        return self.resolve(ITCPState)

    def get_observers(self) -> list[IObserver]:
        """获取观察者列表"""
        return [service for service in self._services.values() 
                if isinstance(service, IObserver)]

    def get_logger(self) -> ILogger:
        """获取日志器"""
        return self.resolve(ILogger) 