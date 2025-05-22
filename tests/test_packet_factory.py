import pytest
from tcp_simulation.core.packet_factory import PacketFactory

def test_create_syn_packet():
    """测试创建SYN数据包"""
    factory = PacketFactory()
    packet = factory.create_syn_packet(
        src_ip="192.168.1.100",
        dst_ip="192.168.1.101",
        src_port=12345,
        dst_port=80,
        seq=1000
    )
    
    assert packet["IP"].src == "192.168.1.100"
    assert packet["IP"].dst == "192.168.1.101"
    assert packet["TCP"].sport == 12345
    assert packet["TCP"].dport == 80
    assert packet["TCP"].seq == 1000
    assert packet["TCP"].flags == "S"

def test_create_ack_packet():
    """测试创建ACK数据包"""
    factory = PacketFactory()
    packet = factory.create_ack_packet(
        src_ip="192.168.1.100",
        dst_ip="192.168.1.101",
        src_port=12345,
        dst_port=80,
        seq=1000,
        ack=2000
    )
    
    assert packet["IP"].src == "192.168.1.100"
    assert packet["IP"].dst == "192.168.1.101"
    assert packet["TCP"].sport == 12345
    assert packet["TCP"].dport == 80
    assert packet["TCP"].seq == 1000
    assert packet["TCP"].ack == 2000
    assert packet["TCP"].flags == "A" 