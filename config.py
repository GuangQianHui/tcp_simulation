#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 默认配置
DEFAULT_CONFIG = {
    'src_ip': '192.168.1.100',
    'dst_ip': '192.168.1.101',
    'src_port': 12345,
    'dst_port': 80,
    'initial_seq': 1000,
    'packet_delay': 1,  # 数据包发送间隔（秒）
    'interface': None,  # 网络接口，None表示自动选择
    'log_level': 'INFO',
    'save_pcap': True,  # 是否保存pcap文件
    'pcap_filename': 'tcp_simulation.pcap'
}

# TCP标志位映射
TCP_FLAGS = {
    'FIN': 0x01,
    'SYN': 0x02,
    'RST': 0x04,
    'PSH': 0x08,
    'ACK': 0x10,
    'URG': 0x20
} 