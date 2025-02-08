- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# 项目简介 📚

欢迎来到 **Habitica 队伍自动化管理项目**！🎉 这个项目致力于通过自动化工具和脚本来优化团队成员管理，从而提升您在 Habitica 平台上的体验。无论您是游戏的一部分，还是仅仅想要轻松管理您的团队，我们的工具都能助您一臂之力！

## 项目结构 📂

下面是项目的结构，确保您能轻松找到所需的文件：

```
.
├── .github
│   └── workflows
│       └── automated_party_management.yml
├── LICENSE
├── README.md
├── README
│   ├── README_Deutsch.md
│   ├── README_English.md
│   ├── README_Español.md
│   ├── README_Français.md
│   ├── README_日本語.md
│   └── README_繁体中文.md
├── documents
│   ├── brief_description.md
│   ├── new_members.md
│   ├── party_description.md
│   ├── remove_PM.md
│   └── remove_members.md
├── logs
│   ├── manage_members.log
│   └── update_description.log
├── requirements.txt
└── scripts
    ├── manage_members.py
    └── update_description.py
```

## 文件简介 🔍

### 自动化队伍管理 (`.github/workflows/automated_party_management.yml`)
这个文件定义了一个名为 “队伍自动化管理” 的 GitHub Actions 工作流。它会每 10 分钟自动运行，或可手动触发，实现以下功能：
- 检出代码仓库
- 设置 Python 3.8 环境
- 安装所需的依赖库（如 `requests`）
- 执行管理脚本（`manage_members.py` 和 `update_description.py`），与 Habitica API 进行交互
- 在脚本执行之间设置延迟，防止超过 API 速率限制
- 提交并推送日志更改，以记录管理脚本的更新

### 许可证 (`LICENSE`)
本项目遵循 Apache 许可证 2.0，旨在促进开源合作，并保护创作者和用户的权利。许可证详细说明了使用、复制和分发软件及其他作品的条款和条件。

### 依赖文件 (`requirements.txt`)
该文件列出了项目所需的外部库和依赖项，这里只包含 “requests” 库，提供了一种简便的方式来发送 HTTP 请求和处理响应。

### 成员管理脚本 (`scripts/manage_members.py`)
此脚本用于管理 Habitica 平台上的成员，自动化以下任务：
- 移除不活跃成员并向其发送通知
- 邀请寻求加入团队的新用户

### 描述更新脚本 (`scripts/update_description.py`)
该脚本负责更新 Habitica 队伍的描述，动态获取内容并进行更新。它的关键功能包括：
- 每日从外部 API 获取的灵感语句
- 自动更新队伍描述，确保信息新鲜感十足！

## 日志文件 📜
所有执行操作的日志都会记录在 `logs` 文件夹中，方便您查看执行历史和排查潜在问题。

## 开始使用 🚀

1. 克隆项目仓库
2. 安装依赖：`pip install -r requirements.txt`
3. 使用 GitHub Actions 自动化工作流，享受无缝的成员管理体验！

## 参与贡献 💡
如您希望为这个项目做出贡献，欢迎提交 PR 或提出问题！让我们一起让 Habitica 更精彩！⭐️

感谢您阅读本项目的 README 文件！期待您的加入与支持，快来 ⭐️ 这个项目吧！