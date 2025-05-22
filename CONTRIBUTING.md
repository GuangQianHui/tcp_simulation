# 贡献指南

感谢您对 TCP 协议仿真项目的关注！我们欢迎各种形式的贡献，包括但不限于：

- 报告 bug
- 提出新功能建议
- 改进文档
- 提交代码修复
- 添加新功能

## 开发环境设置

1. Fork 并克隆仓库：

```bash
git clone https://github.com/your-username/tcp-simulation.git
cd tcp-simulation
```

2. 创建虚拟环境：

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. 安装开发依赖：

```bash
pip install -e ".[dev]"
```

4. 安装 pre-commit 钩子：

```bash
pre-commit install
```

## 开发流程

1. 创建新分支：

```bash
git checkout -b feature/your-feature-name
```

2. 进行更改并提交：

```bash
git add .
git commit -m "描述你的更改"
```

3. 运行测试：

```bash
pytest tests/
```

4. 确保代码质量：

```bash
black tcp_simulation tests
isort tcp_simulation tests
flake8 tcp_simulation tests
mypy tcp_simulation tests
```

5. 推送到你的 fork：

```bash
git push origin feature/your-feature-name
```

6. 创建 Pull Request

## 代码风格

- 使用 Black 进行代码格式化
- 使用 isort 进行导入排序
- 使用 flake8 进行代码检查
- 使用 mypy 进行类型检查
- 遵循 PEP 8 规范
- 编写清晰的文档字符串

## 提交规范

提交信息应该清晰描述更改内容，建议使用以下格式：

```
类型: 简短描述

详细描述（可选）

相关issue: #123
```

类型包括：

- feat: 新功能
- fix: 修复
- docs: 文档更新
- style: 代码格式
- refactor: 重构
- test: 测试
- chore: 构建过程或辅助工具的变动

## 测试

- 编写单元测试
- 确保测试覆盖率
- 运行所有测试确保通过

## 文档

- 更新 README.md
- 更新文档字符串
- 添加必要的注释

## 问题反馈

- 使用 GitHub Issues
- 提供详细的错误信息
- 提供复现步骤

## 行为准则

- 尊重他人
- 接受建设性批评
- 关注问题本身
- 保持专业

## 许可证

贡献代码时，您同意将代码按照项目的 MIT 许可证授权。

# 添加远程仓库

git remote add origin https://github.com/GuangQianHui/tcp-simulation.git

# 推送到主分支

git push -u origin main

## 功能特性

- TCP 三次握手和四次挥手仿真
- 完整的错误处理机制
- 详细的日志记录
- 支持自定义参数配置
- 自动化测试和代码质量检查

## 技术栈

- Python 3.7+
- Scapy
- 设计模式（工厂、状态、观察者）

## 文档

- 详细的使用说明
- 完整的 API 文档
- 贡献指南
- 行为准则
- 安全策略
