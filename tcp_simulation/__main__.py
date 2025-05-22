#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import logging
import argparse
from typing import Dict, Any

from .core.tcp_simulation import TCPSimulation
from .utils.error_handler import (
    handle_error,
    check_requirements,
    validate_ip,
    validate_port,
    ConfigurationError,
    NetworkError,
    PermissionError
)

def setup_logging(debug: bool = False) -> logging.Logger:
    """
    设置日志记录
    
    Args:
        debug: 是否启用调试模式
    
    Returns:
        logging.Logger: 配置好的日志记录器
    """
    logger = logging.getLogger('tcp_simulation')
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # 创建文件处理器
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    file_handler = logging.FileHandler(
        os.path.join(log_dir, 'tcp_simulation.log'),
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    
    # 设置日志格式
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    # 添加处理器
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

def parse_arguments() -> Dict[str, Any]:
    """
    解析命令行参数
    
    Returns:
        Dict[str, Any]: 参数字典
    """
    parser = argparse.ArgumentParser(description='TCP协议仿真工具')
    
    parser.add_argument('--src-ip', type=str, required=True,
                      help='源IP地址')
    parser.add_argument('--dst-ip', type=str, required=True,
                      help='目标IP地址')
    parser.add_argument('--src-port', type=int, required=True,
                      help='源端口号')
    parser.add_argument('--dst-port', type=int, required=True,
                      help='目标端口号')
    parser.add_argument('--interface', type=str,
                      help='网络接口名称')
    parser.add_argument('--delay', type=float, default=1.0,
                      help='数据包发送延迟（秒）')
    parser.add_argument('--no-save', action='store_true',
                      help='不保存pcap文件')
    parser.add_argument('--debug', action='store_true',
                      help='启用调试模式')
    
    args = parser.parse_args()
    
    # 验证参数
    if not validate_ip(args.src_ip):
        raise ConfigurationError(f"无效的源IP地址: {args.src_ip}")
    if not validate_ip(args.dst_ip):
        raise ConfigurationError(f"无效的目标IP地址: {args.dst_ip}")
    if not validate_port(args.src_port):
        raise ConfigurationError(f"无效的源端口号: {args.src_port}")
    if not validate_port(args.dst_port):
        raise ConfigurationError(f"无效的目标端口号: {args.dst_port}")
    if args.delay < 0:
        raise ConfigurationError("延迟时间不能为负数")
    
    return vars(args)

def main() -> None:
    """
    主程序入口
    """
    try:
        # 检查运行环境
        check_requirements()
        
        # 解析命令行参数
        args = parse_arguments()
        
        # 设置日志
        logger = setup_logging(args.get('debug', False))
        logger.info("TCP协议仿真工具启动")
        
        # 创建TCP仿真实例
        simulation = TCPSimulation(
            src_ip=args['src_ip'],
            dst_ip=args['dst_ip'],
            src_port=args['src_port'],
            dst_port=args['dst_port'],
            interface=args.get('interface'),
            delay=args.get('delay', 1.0),
            save_pcap=not args.get('no_save', False)
        )
        
        # 运行仿真
        simulation.run()
        
    except KeyboardInterrupt:
        logger.info("程序被用户中断")
        sys.exit(0)
    except Exception as e:
        handle_error(e, logger if 'logger' in locals() else None)

if __name__ == '__main__':
    main() 