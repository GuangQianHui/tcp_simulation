import pytest
from tcp_simulation.core.tcp_state import TCPState, ClosedState, ListenState

def test_closed_state():
    """测试CLOSED状态"""
    state = ClosedState()
    assert state.name == "CLOSED"
    
    # 测试状态转换
    next_state = state.handle_packet(None, "SYN")
    assert isinstance(next_state, ListenState)

def test_listen_state():
    """测试LISTEN状态"""
    state = ListenState()
    assert state.name == "LISTEN"
    
    # 测试状态转换
    next_state = state.handle_packet(None, "SYN")
    assert next_state.name == "SYN_RECEIVED"
    
    next_state = state.handle_packet(None, "RST")
    assert next_state.name == "CLOSED" 