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
        "typing-extensions>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "isort>=5.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "pre-commit>=3.0.0",
        ],
    },
    entry_points={
        'console_scripts': [
            'tcp-sim=tcp_simulation.__main__:main',
        ],
    },
    author="Guang Qianhui",
    author_email="xuqiguang9@gmail.com",
    description="TCP协议仿真工具 - 用于学习和研究TCP协议的高级工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guangqianhui/tcp-simulation",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Education",
        "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: System :: Networking :: Time Synchronization",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    keywords="tcp, networking, protocol, simulation, education, scapy",
    project_urls={
        "Bug Reports": "https://github.com/guangqianhui/tcp-simulation/issues",
        "Source": "https://github.com/guangqianhui/tcp-simulation",
        "Documentation": "https://github.com/guangqianhui/tcp-simulation/wiki",
    },
)
