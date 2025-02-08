## README

### 语言切换
- [繁体中文](README/README_繁体中文.md)
- [English](README/README_English.md)
- [Español](README/README_Español.md)
- [Français](README/README_Français.md)
- [Deutsch](README/README_Deutsch.md)
- [日本語](README/README_日本語.md)

# 🥳 自动化团队管理工具 README

欢迎使用我们的自动化团队管理工具！这个项目旨在通过与 Habitica API 的集成，提升团队管理的效率与参与感。💼✨

## 📁 文件概述

### 1. GitHub Actions 工作流
- **路径**: `.github/workflows/automated_party_management.yml`
- **功能**: 该工作流每 10 分钟触发一次（也可以手动运行），包含以下关键步骤：
  - 检出代码
  - 设置 Python 环境
  - 安装依赖
  - 执行管理脚本以处理 Habitica 平台的团队成员
  - 运行更新脚本记录更改
- **特点**: 包含暂停功能以管理请求速率，最后将任何日志更改提交并推送到代码库。🔄

### 2. 许可协议
- **文件名**: `LICENSE`
- **内容**: 内容为 Apache 许可证，版本 2.0，概述了软件及相关作品的使用、复制和分发的条款与条件，包括定义、用户权限、再分发要求及免责声明。📜

### 3. 成员管理脚本
- **文件名**: `manage_members.py`
- **功能**: 此 Python 脚本旨在管理 Habitica 平台中的团队成员，主要功能包括：
  - **日志设置**: 初始化日志以跟踪脚本操作，包括错误和一般信息。
  - **速率限制**: 实施机制以遵循 API 请求限制，通过控制请求时间进行管理。
  - **成员管理**:
    - 确定并检索基于最后登录时间的非活跃团队成员。
    - 在移除成员前发送私信通知。
    - 向团队聊天发送成员移除的通知。
  - **邀请功能**: 寻找正在寻找团队的用户，并向他们发送邀请，包括格式化的消息列表出被邀请的成员。
  - **实用工具**: 包含处理 API 响应、发送消息及根据用户活动计算时间的辅助函数。

总之，此脚本通过自动化非活跃用户的移除和新用户的邀请，提升了 Habitica 的团队管理，促进了更好的用户参与。🎉

### 4. 描述更新脚本
- **文件名**: `update_description.py`
- **功能**: 此 Python 脚本旨在更新 Habitica 团队的描述，功能包括：
  - 日常获取一句话和团队成员的最后登录详情。
  - 日志记录、执行 API 请求的速率限制。
  - 根据检索的数据动态更新团队描述。
  - 从模板文件读取描述格式，编译成员信息，并向 Habitica API 发送更新请求。
  - 记录操作过程中的成功与错误。

## 🛠️ 安装与使用

1. 克隆本仓库：
   ```bash
   git clone https://github.com/yourusername/repository.git
   cd repository
   ```

2. 设置 Python 环境：
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 配置 GitHub Actions 工作流（若需要），并在 Habitica API 中生成一个有效的密钥。

5. 运行脚本：
   ```bash
   python manage_members.py
   python update_description.py
   ```

## 💡 贡献

欢迎任何形式的贡献！如有建议或问题，请提交 issue 或发起 pull request。😊

## 📞 联系

如果您有任何问题或反馈，请通过以下方式联系我：
- 邮箱: your_email@example.com
- GitHub: [你的GitHub用户名](https://github.com/yourusername)

感谢您使用我们的工具，祝您在 Habitica 中的团队管理更加顺利！🎊