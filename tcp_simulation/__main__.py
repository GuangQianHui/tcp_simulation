#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
from typing import Optional

from .config.settings import TCPConfig, AppConfig
from .core.container import Container
from .core.events import EventManager, EventType
from .core.tcp_simulation import TCPSimulation
from .utils.logger import Logger
from .observers.packet_logger import PacketLogger
from .observers.packet_capture import PacketCapture

def parse_args() -> TCPConfig:
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="TCP协议仿真工具")
    parser.add_argument("--src-ip", required=True, help="源IP地址")
    parser.add_argument("--dst-ip", required=True, help="目标IP地址")
    parser.add_argument("--src-port", type=int, help="源端口号")
    parser.add_argument("--dst-port", type=int, default=80, help="目标端口号")
    parser.add_argument("--seq", type=int, help="初始序列号")
    parser.add_argument("--ack", type=int, default=0, help="初始确认号")
    parser.add_argument("--window", type=int, default=65535, help="窗口大小")
    parser.add_argument("--debug", action="store_true", help="启用调试模式")
    
    args = parser.parse_args()
    return TCPConfig(
        src_ip=args.src_ip,
        dst_ip=args.dst_ip,
        src_port=args.src_port,
        dst_port=args.dst_port,
        seq=args.seq,
        ack=args.ack,
        window=args.window,
        debug=args.debug
    )

def setup_container(config: AppConfig) -> Container:
    """设置依赖注入容器"""
    container = Container()
    
    # 注册服务
    container.register(ILogger, Logger(config.log))
    container.register(IPacketFactory, PacketFactory())
    
    # 注册观察者
    container.register(IObserver, PacketLogger(container.get_logger()))
    container.register(IObserver, PacketCapture(config.log.capture_file))
    
    return container

def main() -> Optional[int]:
    """主函数"""
    try:
        # 解析配置
        tcp_config = parse_args()
        app_config = AppConfig(tcp=tcp_config)
        
        # 设置容器
        container = setup_container(app_config)
        
        # 创建事件管理器
        event_manager = EventManager()
        
        # 创建TCP仿真器
        simulation = TCPSimulation(
            config=app_config.tcp,
            container=container,
            event_manager=event_manager
        )
        
        # 运行仿真
        simulation.run()
        return 0
        
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main()) 