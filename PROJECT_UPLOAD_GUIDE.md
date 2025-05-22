# TCP 协议仿真项目上传指南

本文档详细说明了如何将 TCP 协议仿真项目上传到 GitHub 以及如何进行后续修改。

## 目录

1. [初始上传](#初始上传)
2. [修改项目](#修改项目)
3. [常见问题解决](#常见问题解决)
4. [最佳实践](#最佳实践)

## 初始上传

### 1. 准备工作

1. 确保已安装 Git
2. 确保已配置 GitHub SSH 密钥
3. 确保项目目录结构完整

### 2. 初始化 Git 仓库

```bash
# 进入项目目录
cd C:\Users\徐啟光\Desktop\project4

# 初始化 Git 仓库
git init
```

### 3. 配置 .gitignore

确保 `.gitignore` 文件包含以下内容：

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.idea/
.vscode/
*.swp
*.swo
.project
.pydevproject
.settings/

# 环境
venv/
env/
ENV/
.env

# 日志
*.log
logs/

# 抓包文件
*.pcap
*.cap

# 系统文件
.DS_Store
Thumbs.db

# 测试覆盖率报告
.coverage
htmlcov/
.tox/
.nox/
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/
```

### 4. 添加文件到 Git

```bash
# 添加所有文件
git add .

# 检查状态
git status
```

### 5. 创建首次提交

```bash
git commit -m "feat: 初始提交 - TCP协议仿真项目"
```

### 6. 添加远程仓库

```bash
# 添加远程仓库
git remote add origin git@github.com:GuangQianHui/tcp_simulation.git
```

### 7. 推送到 GitHub

```bash
# 推送到主分支
git push -u origin master
```

## 修改项目

### 1. 修改文件

1. 修改需要更新的文件
2. 使用 `git status` 检查修改状态
3. 使用 `git diff` 查看具体修改内容

### 2. 提交修改

```bash
# 添加修改的文件
git add 文件名

# 提交修改
git commit -m "类型: 修改说明"

# 推送到远程仓库
git push origin master
```

### 3. 修改 README.md

1. 更新项目信息
2. 更新安装说明
3. 更新使用说明
4. 更新项目结构
5. 更新联系方式

```bash
# 添加修改
git add README.md

# 提交更改
git commit -m "docs: 更新 README.md 文档"

# 推送到远程仓库
git push origin main
```

## 常见问题解决

### 1. 推送失败

```bash
# 先拉取最新代码
git pull origin main

# 解决冲突后再推送
git push origin main
```

### 2. 分支问题

```bash
# 创建并切换到 main 分支
git branch -M main
```

### 3. 编码问题

```bash
# 设置 Git 编码
git config --global core.quotepath false
git config --global gui.encoding utf-8
git config --global i18n.commit.encoding utf-8
git config --global i18n.logoutputencoding utf-8
```

### 4. 撤销修改

```bash
# 撤销工作区的修改
git checkout -- 文件名

# 撤销暂存区的修改
git reset HEAD 文件名
```

## 最佳实践

1. 提交前检查

   - 使用 `git status` 检查修改状态
   - 使用 `git diff` 查看具体修改
   - 确保没有敏感信息

2. 提交信息规范

   - 使用清晰的提交信息
   - 遵循约定式提交规范
   - 说明修改的原因和影响

3. 分支管理

   - 主分支保持稳定
   - 新功能使用特性分支
   - 及时合并和删除分支

4. 文档维护

   - 及时更新 README.md
   - 保持文档的准确性
   - 添加必要的注释

5. 代码质量

   - 运行测试确保功能正常
   - 检查代码风格
   - 确保没有语法错误

6. 安全考虑
   - 不要提交敏感信息
   - 使用 .gitignore 排除不需要的文件
   - 定期检查文件权限

## 注意事项

1. 确保 Git 配置正确
2. 确保 SSH 密钥配置正确
3. 确保有足够的权限
4. 定期备份重要文件
5. 保持提交历史的清晰
6. 遵循项目的代码规范
7. 及时处理冲突
8. 保持文档的更新
