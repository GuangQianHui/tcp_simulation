import pytest
from tcp_simulation.core.tcp_simulation import TCPSimulation

def test_tcp_simulation_initialization():
    """测试TCP仿真初始化"""
    simulation = TCPSimulation(
        src_ip="192.168.1.100",
        dst_ip="192.168.1.101",
        src_port=12345,
        dst_port=80
    )
    
    assert simulation.src_ip == "192.168.1.100"
    assert simulation.dst_ip == "192.168.1.101"
    assert simulation.src_port == 12345
    assert simulation.dst_port == 80
    assert simulation.current_state.name == "CLOSED"

def test_tcp_simulation_state_transition():
    """测试TCP状态转换"""
    simulation = TCPSimulation(
        src_ip="192.168.1.100",
        dst_ip="192.168.1.101"
    )
    
    # 测试从CLOSED到LISTEN的转换
    simulation.handle_packet(None, "SYN")
    assert simulation.current_state.name == "LISTEN"
    
    # 测试从LISTEN到SYN_RECEIVED的转换
    simulation.handle_packet(None, "SYN")
    assert simulation.current_state.name == "SYN_RECEIVED" 