# TCP 协议仿真工具

一个基于 Python 和 Scapy 的 TCP 协议仿真工具，用于学习和研究 TCP 协议的工作原理。

## 项目地址

- GitHub: [https://github.com/GuangQianHui/tcp_simulation](https://github.com/GuangQianHui/tcp_simulation)
- 作者: [GuangQianHui](https://github.com/GuangQianHui)

## 功能特性

- TCP 三次握手和四次挥手仿真
- 完整的错误处理机制
- 详细的日志记录
- 支持自定义参数配置
- 自动化测试和代码质量检查
- 使用设计模式（工厂、状态、观察者）实现

## 环境要求

- Python 3.7+
- Scapy 2.5.0+
- cryptography 41.0.0+
- typing-extensions 4.0.0+

## 安装方法

1. 克隆仓库：

```bash
git clone https://github.com/GuangQianHui/tcp_simulation.git
cd tcp_simulation
```

2. 创建虚拟环境：

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. 安装依赖：

```bash
# 开发环境安装
pip install -e ".[dev]"

# 或使用安装脚本
python install.py
```

## 使用方法

1. 基本使用：

```bash
# 使用默认配置运行
tcp-sim

# 或直接运行 Python 模块
python -m tcp_simulation
```

2. 自定义参数：

```bash
tcp-sim --src-ip 192.168.1.100 --dst-ip 192.168.1.101 --src-port 12345 --dst-port 80 --debug
```

## 项目结构

```
tcp-simulation/
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions 工作流配置
├── tcp_simulation/
│   ├── __init__.py
│   ├── __main__.py               # 主程序入口
│   ├── core/
│   │   ├── __init__.py
│   │   ├── tcp_simulation.py     # TCP 仿真核心类
│   │   ├── packet_factory.py     # 数据包工厂类
│   │   └── tcp_state.py          # TCP 状态类
│   └── utils/
│       ├── __init__.py
│       ├── error_handler.py      # 错误处理模块
│       ├── packet_analyzer.py    # 数据包分析器
│       └── observers.py          # 观察者模式实现
├── tests/                        # 测试目录
├── .gitignore                    # Git 忽略文件
├── .pre-commit-config.yaml       # 预提交钩子配置
├── CODE_OF_CONDUCT.md           # 行为准则
├── CONTRIBUTING.md              # 贡献指南
├── LICENSE                      # MIT 许可证
├── README.md                    # 项目说明文档
├── SECURITY.md                  # 安全策略
├── install.py                   # 安装脚本
├── requirements.txt             # 依赖包列表
└── setup.py                     # 包安装配置
```

## 核心组件

### PacketFactory

负责创建各种 TCP 数据包，使用工厂模式实现。

### TCPState

管理 TCP 连接状态，使用状态模式实现。

### Observers

实现观察者模式，用于日志记录、数据包捕获和分析。

## 测试

运行测试：

```bash
pytest tests/
```

## 注意事项

1. 需要管理员/root 权限运行
2. 需要安装 Wireshark 进行数据包分析
3. 建议在测试环境中运行
4. 不要在生产环境中使用

## 日志说明

日志文件位于 `logs/` 目录下：

- `tcp_simulation.log`: 主日志文件
- `packet_capture.log`: 数据包捕获日志
- `error.log`: 错误日志

## 开发指南

1. 添加新的 TCP 状态：

   - 在 `tcp_simulation/core/tcp_state.py` 中创建新的状态类
   - 实现必要的方法
   - 在 `TCPSimulation` 类中集成新状态

2. 添加新的观察者：
   - 在 `tcp_simulation/utils/observers.py` 中创建新的观察者类
   - 实现 `update` 方法
   - 在 `TCPSimulation` 类中注册新观察者

## 贡献指南

欢迎提交 Issue 和 Pull Request。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 行为准则

请参阅 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。

## 安全策略

请参阅 [SECURITY.md](SECURITY.md)。

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 联系方式

- 作者: GuangQianHui
- GitHub: [https://github.com/GuangQianHui](https://github.com/GuangQianHui)
- 邮箱: xuqiguang9@gmail.com
