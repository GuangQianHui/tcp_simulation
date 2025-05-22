#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """检查 Python 版本"""
    if sys.version_info < (3, 7):
        print("错误: 需要 Python 3.7 或更高版本")
        sys.exit(1)

def create_virtual_env():
    """创建虚拟环境"""
    if not os.path.exists("venv"):
        print("创建虚拟环境...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    else:
        print("虚拟环境已存在")

def install_dependencies():
    """安装依赖"""
    print("安装依赖...")
    
    # 获取虚拟环境中的 Python 路径
    if sys.platform == "win32":
        python_path = os.path.join("venv", "Scripts", "python")
    else:
        python_path = os.path.join("venv", "bin", "python")
    
    # 升级 pip
    print("升级 pip...")
    subprocess.run([python_path, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    
    # 安装项目依赖
    print("安装项目依赖...")
    subprocess.run([python_path, "-m", "pip", "install", "-e", "."], check=True)
    
    # 安装开发依赖
    print("安装开发依赖...")
    subprocess.run([python_path, "-m", "pip", "install", "-e", ".[dev]"], check=True)

def main():
    """主函数"""
    try:
        print("开始安装 TCP 协议仿真项目...")
        
        # 检查 Python 版本
        check_python_version()
        
        # 创建虚拟环境
        create_virtual_env()
        
        # 安装依赖
        install_dependencies()
        
        print("\n安装完成！")
        print("\n使用方法:")
        print("1. 激活虚拟环境:")
        if sys.platform == "win32":
            print("   .\\venv\\Scripts\\activate")
        else:
            print("   source venv/bin/activate")
        print("2. 运行程序:")
        print("   tcp-sim")
        
    except subprocess.CalledProcessError as e:
        print(f"错误: 安装过程中出现错误: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 