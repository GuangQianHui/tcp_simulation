#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# 使用UTF-8编码读取README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="tcp-simulation",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "scapy>=2.5.0",
        "cryptography>=41.0.0",
    ],
    entry_points={
        'console_scripts': [
            'tcp-sim=tcp_simulation.__main__:main',
        ],
    },
    author="Guang Qianhui",
    author_email="xuqiguang9@gmail.com",
    description="TCP协议仿真工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guangqianhui/tcp-simulation",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 