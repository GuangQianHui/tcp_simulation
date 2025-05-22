#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import platform
from pathlib import Path

def check_python_version():
    """检查Python版本"""
    if sys.version_info < (3, 7):
        print("错误: 需要Python 3.7或更高版本")
        sys.exit(1)
    print(f"Python版本检查通过: {platform.python_version()}")

def create_virtual_env():
    """创建虚拟环境"""
    venv_path = Path("venv")
    if not venv_path.exists():
        print("创建虚拟环境...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    else:
        print("虚拟环境已存在")

def get_venv_python():
    """获取虚拟环境中的Python解释器路径"""
    if platform.system() == "Windows":
        return Path("venv/Scripts/python.exe")
    return Path("venv/bin/python")

def install_dependencies():
    """安装依赖"""
    python_path = get_venv_python()
    if not python_path.exists():
        print(f"错误: 找不到虚拟环境Python解释器: {python_path}")
        sys.exit(1)

    print("正在安装依赖...")
    
    # 升级pip
    print("升级pip...")
    subprocess.run([str(python_path), "-m", "pip", "install", "--upgrade", "pip"], check=True)
    
    # 安装项目依赖
    print("安装项目依赖...")
    subprocess.run([str(python_path), "-m", "pip", "install", "-e", "."], check=True)
    
    # 安装开发依赖
    print("安装开发依赖...")
    subprocess.run([str(python_path), "-m", "pip", "install", "-e", ".[dev]"], check=True)

def main():
    """主函数"""
    try:
        print("开始安装TCP协议仿真工具...")
        check_python_version()
        create_virtual_env()
        install_dependencies()
        print("\n安装完成！")
        print("\n使用说明：")
        print("1. 激活虚拟环境：")
        if platform.system() == "Windows":
            print("   .\\venv\\Scripts\\activate")
        else:
            print("   source venv/bin/activate")
        print("2. 运行程序：")
        print("   python -m tcp_simulation --src-ip 192.168.1.100 --dst-ip 192.168.1.101")
        print("\n注意：")
        print("- 请确保使用管理员权限运行")
        print("- 如果遇到权限问题，请尝试使用 'python -m tcp_simulation' 命令")
        
    except subprocess.CalledProcessError as e:
        print(f"安装过程中出错: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"发生错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 