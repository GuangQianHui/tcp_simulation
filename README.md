# TCP 协议仿真项目

本项目使用 Python 和 Scapy 库实现 TCP 协议的三次握手和四次挥手过程的仿真。项目采用面向对象设计，实现了多种设计模式，提供了灵活且可扩展的 TCP 协议仿真功能。

## 项目特点

- 使用工厂模式创建 TCP 数据包
- 使用状态模式管理 TCP 状态转换
- 使用观察者模式处理数据包事件
- 支持自定义 IP 地址、端口号等参数
- 自动捕获和保存数据包
- 详细的日志记录
- 完整的错误处理机制
- 参数验证和类型检查
- 运行环境检查

## 环境要求

- Python 3.7+
- Scapy >= 2.5.0
- cryptography >= 41.0.0
- Wireshark

## 安装步骤

1. 克隆项目到本地：

```bash
git clone [项目地址]
cd tcp-simulation
```

2. 创建并激活虚拟环境（推荐）：

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. 安装依赖：

```bash
# 方法1：使用pip安装（推荐）
pip install -e .

# 方法2：直接运行Python模块
python -m tcp_simulation
```

4. 安装 Wireshark（如果尚未安装）：

- Windows: 从[Wireshark 官网](https://www.wireshark.org/download.html)下载安装包
- Linux: `sudo apt-get install wireshark`

## 使用方法

1. 基本用法：

```bash
# 方法1：使用安装的命令
tcp-sim --src-ip 192.168.1.100 --dst-ip 192.168.1.101 --src-port 12345 --dst-port 80

# 方法2：直接运行Python模块
python -m tcp_simulation --src-ip 192.168.1.100 --dst-ip 192.168.1.101 --src-port 12345 --dst-port 80
```

2. 命令行参数说明：

- `--src-ip`: 源 IP 地址（必需）
- `--dst-ip`: 目标 IP 地址（必需）
- `--src-port`: 源端口号（必需）
- `--dst-port`: 目标端口号（必需）
- `--interface`: 网络接口名称（可选）
- `--delay`: 数据包发送延迟（秒），默认 1.0
- `--no-save`: 不保存 pcap 文件
- `--debug`: 启用调试模式

## 错误处理

程序包含完整的错误处理机制，主要处理以下几类错误：

1. 配置错误（ConfigurationError）：

   - 无效的 IP 地址
   - 无效的端口号
   - 无效的延迟时间
   - 不支持的参数组合

2. 权限错误（PermissionError）：

   - 缺少管理员/root 权限
   - 文件系统权限不足

3. 网络错误（NetworkError）：

   - 网络接口不可用
   - 数据包发送失败
   - 连接超时

4. 数据包错误（PacketError）：
   - 数据包构造失败
   - 数据包解析错误

## 日志记录

程序提供详细的日志记录功能：

1. 日志级别：

   - DEBUG：详细的调试信息
   - INFO：常规操作信息
   - WARNING：警告信息
   - ERROR：错误信息

2. 日志输出：

   - 控制台输出：实时显示程序运行状态
   - 文件记录：保存在 `logs/tcp_simulation.log`

3. 日志内容：
   - 时间戳
   - 日志级别
   - 模块名称
   - 详细信息

## 注意事项

1. 依赖版本要求：

   - Scapy >= 2.5.0
   - cryptography >= 41.0.0
   - Python >= 3.7

2. 可能出现的警告：

   - 如果看到 cryptography 相关的废弃警告，请确保已安装最新版本的 cryptography 包
   - 这些警告不会影响程序的正常运行

3. 运行环境：

   - 建议在虚拟环境中运行程序
   - 需要管理员/root 权限
   - 确保防火墙不会阻止程序运行
   - 建议在测试环境中运行，避免影响生产网络

4. 性能考虑：
   - 数据包发送延迟默认设置为 1 秒，可以根据需要调整
   - 大量数据包捕获可能会占用较多磁盘空间
   - 建议定期清理日志文件

## 开发说明

### 添加新的错误类型

1. 在 `error_handler.py` 中定义新的异常类
2. 在 `handle_error` 函数中添加对应的错误消息
3. 在适当的地方抛出新的异常

### 添加新的日志记录

1. 使用 `setup_logging` 函数获取日志记录器
2. 使用适当的日志级别记录信息
3. 确保日志消息清晰且有意义

## 许可证

MIT License
