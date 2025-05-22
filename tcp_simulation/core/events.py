"""
TCP协议仿真工具的事件系统
"""
from dataclasses import dataclass
from typing import Any, Callable, Dict, List
from enum import Enum, auto

class EventType(Enum):
    """事件类型枚举"""
    PACKET_SENT = auto()
    PACKET_RECEIVED = auto()
    STATE_CHANGED = auto()
    ERROR_OCCURRED = auto()

@dataclass
class Event:
    """事件基类"""
    type: EventType
    data: Any

class EventManager:
    """事件管理器"""
    def __init__(self):
        self._handlers: Dict[EventType, List[Callable]] = {
            event_type: [] for event_type in EventType
        }

    def subscribe(self, event_type: EventType, handler: Callable) -> None:
        """订阅事件"""
        if handler not in self._handlers[event_type]:
            self._handlers[event_type].append(handler)

    def unsubscribe(self, event_type: EventType, handler: Callable) -> None:
        """取消订阅事件"""
        if handler in self._handlers[event_type]:
            self._handlers[event_type].remove(handler)

    def emit(self, event: Event) -> None:
        """触发事件"""
        for handler in self._handlers[event.type]:
            handler(event) 