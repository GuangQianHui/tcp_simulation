#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
from typing import Optional, Type, Union

class TCPSimulationError(Exception):
    """TCP模拟基础异常类"""
    pass

class PacketError(TCPSimulationError):
    """数据包相关错误"""
    pass

class NetworkError(TCPSimulationError):
    """网络相关错误"""
    pass

class ConfigurationError(TCPSimulationError):
    """配置相关错误"""
    pass

class PermissionError(TCPSimulationError):
    """权限相关错误"""
    pass

def handle_error(error: Exception, logger: Optional[logging.Logger] = None) -> None:
    """
    统一的错误处理函数
    
    Args:
        error: 异常对象
        logger: 日志记录器
    """
    error_messages = {
        PermissionError: "需要管理员/root权限才能运行此程序",
        NetworkError: "网络操作失败，请检查网络连接和防火墙设置",
        ConfigurationError: "配置错误，请检查参数设置",
        PacketError: "数据包处理错误，请检查网络环境",
    }
    
    error_type = type(error)
    message = error_messages.get(error_type, str(error))
    
    if logger:
        logger.error(f"错误类型: {error_type.__name__}")
        logger.error(f"错误信息: {message}")
        logger.error(f"详细错误: {str(error)}")
    else:
        print(f"错误: {message}", file=sys.stderr)
        print(f"详细错误: {str(error)}", file=sys.stderr)
    
    sys.exit(1)

def check_requirements() -> None:
    """
    检查运行环境要求
    """
    import platform
    import os
    
    # 检查操作系统
    if platform.system() not in ['Windows', 'Linux', 'Darwin']:
        raise ConfigurationError("不支持的操作系统")
    
    # 检查Python版本
    if sys.version_info < (3, 7):
        raise ConfigurationError("需要Python 3.7或更高版本")
    
    # 检查权限
    if platform.system() == 'Windows':
        try:
            import ctypes
            if not ctypes.windll.shell32.IsUserAnAdmin():
                raise PermissionError()
        except Exception:
            raise PermissionError()
    else:
        if os.geteuid() != 0:
            raise PermissionError()

def validate_ip(ip: str) -> bool:
    """
    验证IP地址格式
    
    Args:
        ip: IP地址字符串
    
    Returns:
        bool: IP地址格式是否有效
    """
    import ipaddress
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def validate_port(port: int) -> bool:
    """
    验证端口号
    
    Args:
        port: 端口号
    
    Returns:
        bool: 端口号是否有效
    """
    return 0 < port < 65536 