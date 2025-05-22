# TCP 协议仿真工具

一个使用 Python 和 Scapy 实现的 TCP 协议仿真工具，采用现代化的架构设计和设计模式，用于学习和研究 TCP 协议的工作原理。

## 功能特点

- 采用现代化的架构设计
  - 依赖注入容器管理服务
  - 事件驱动架构
  - 接口分离原则
  - 配置管理
- 使用设计模式
  - 工厂模式：数据包创建
  - 状态模式：TCP 状态转换
  - 观察者模式：事件通知
  - 发布-订阅模式：组件通信
- 支持自定义 TCP 参数
  - IP 地址和端口配置
  - 序列号和确认号
  - 窗口大小
  - 调试模式
- 完善的日志系统
  - 多级别日志记录
  - 数据包捕获
  - 错误追踪
- 可扩展的架构
  - 插件式设计
  - 接口标准化
  - 松耦合组件

## 环境要求

- Python 3.7+
- Windows/Linux/macOS
- 管理员/root 权限（用于网络数据包捕获）
- Wireshark（用于查看捕获的数据包）

## 安装步骤

1. 克隆仓库：

```bash
git clone https://github.com/guangqianhui/tcp-simulation.git
cd tcp-simulation
```

2. 运行安装脚本：

```bash
python install.py
```

3. 激活虚拟环境：

```bash
# Windows
.\venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

## 使用方法

### 基本用法

```bash
python -m tcp_simulation --src-ip 192.168.1.100 --dst-ip 192.168.1.101
```

### 自定义参数

```bash
python -m tcp_simulation \
    --src-ip 192.168.1.100 \
    --dst-ip 192.168.1.101 \
    --src-port 12345 \
    --dst-port 80 \
    --seq 1000 \
    --ack 2000 \
    --window 65535 \
    --debug
```

### 参数说明

- `--src-ip`: 源 IP 地址（必需）
- `--dst-ip`: 目标 IP 地址（必需）
- `--src-port`: 源端口号（默认：随机）
- `--dst-port`: 目标端口号（默认：80）
- `--seq`: 初始序列号（默认：随机）
- `--ack`: 初始确认号（默认：0）
- `--window`: 窗口大小（默认：65535）
- `--debug`: 启用调试模式（可选）

## 项目结构

```
tcp-simulation/
├── tcp_simulation/
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py          # 配置管理
│   ├── core/
│   │   ├── __init__.py
│   │   ├── container.py         # 依赖注入容器
│   │   ├── events.py           # 事件系统
│   │   ├── interfaces.py       # 接口定义
│   │   ├── packet_factory.py   # 数据包工厂
│   │   ├── tcp_state.py        # TCP状态
│   │   └── tcp_simulation.py   # TCP仿真核心
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── error_handler.py    # 错误处理
│   │   └── logger.py          # 日志系统
│   ├── observers/
│   │   ├── __init__.py
│   │   ├── packet_logger.py    # 数据包日志
│   │   └── packet_capture.py   # 数据包捕获
│   └── __main__.py            # 程序入口
├── tests/
│   ├── __init__.py
│   ├── test_packet_factory.py
│   ├── test_tcp_state.py
│   └── test_tcp_simulation.py
├── install.py
├── setup.py
├── requirements.txt
├── README.md
└── LICENSE
```

## 核心组件

### 配置管理 (Config)

- 使用数据类管理配置
- 支持 TCP 和日志配置
- 类型安全的配置访问

### 事件系统 (Events)

- 发布-订阅模式
- 支持多种事件类型
- 松耦合的组件通信

### 依赖注入 (Container)

- 服务注册和解析
- 接口实现管理
- 依赖关系管理

### 接口定义 (Interfaces)

- 清晰的接口契约
- 类型提示支持
- 实现一致性保证

### 数据包工厂 (PacketFactory)

- 工厂模式实现
- 支持多种数据包类型
- 参数化数据包创建

### TCP 状态 (TCPState)

- 状态模式实现
- 状态转换管理
- 事件处理机制

### 观察者 (Observers)

- 观察者模式实现
- 数据包日志记录
- 数据包捕获功能

## 开发指南

### 添加新的 TCP 状态

1. 在 `tcp_simulation/core/tcp_state.py` 中创建新的状态类
2. 实现 `ITCPState` 接口
3. 在 `TCPState` 类中注册新状态

### 添加新的观察者

1. 在 `tcp_simulation/observers` 目录下创建新的观察者类
2. 实现 `IObserver` 接口
3. 在容器中注册新观察者

### 添加新的事件类型

1. 在 `tcp_simulation/core/events.py` 中的 `EventType` 枚举中添加新类型
2. 实现相应的事件处理逻辑
3. 在需要的地方触发事件

## 测试

运行测试：

```bash
# 激活虚拟环境后
pytest tests/
```

## 注意事项

1. 需要管理员/root 权限运行
2. 确保 Wireshark 已安装
3. 如果遇到权限问题，请使用 `python -m tcp_simulation` 命令运行

## 日志

日志文件保存在 `logs` 目录下：

- `tcp_simulation.log`: 主日志文件
- `packet_capture.pcap`: 数据包捕获文件

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 贡献指南

欢迎提交 Pull Request 或创建 Issue！

## 联系方式

- 作者：Guang Qianhui
- 邮箱：xuqiguang9@gmail.com
- GitHub：[guangqianhui](https://github.com/guangqianhui)
