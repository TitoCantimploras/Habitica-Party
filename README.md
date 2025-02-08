## README

### 语言切换
- [繁体中文](README/README_繁体中文.md)
- [English](README/README_English.md)
- [Español](README/README_Español.md)
- [Français](README/README_Français.md)
- [Deutsch](README/README_Deutsch.md)
- [日本語](README/README_日本語.md)

# 🎉 自动化队伍管理项目

欢迎来到我们的**自动化队伍管理项目**! 🚀 本项目旨在通过自动化脚本轻松管理 Habitica 平台上的队伍成员，保持队伍活跃并提升管理效率。让我们一起看看这个项目的结构及其功能吧！

## 📁 项目结构

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/automated_party_management.yml": "自动化队伍管理工作流"
    }
  },
  "LICENSE": "许可证文件",
  "README.md": "项目说明文档",
  "README": {
    "README/README_Deutsch.md": "德语文档",
    "README/README_English.md": "英语文档",
    "README/README_Español.md": "西班牙语文档",
    "README/README_Français.md": "法语文档",
    "README/README_日本語.md": "日语文档",
    "README/README_繁体中文.md": "繁体中文文档"
  },
  "documents": {
    "documents/brief_description.md": "项目简要说明",
    "documents/new_members.md": "新成员介绍",
    "documents/party_description.md": "队伍描述",
    "documents/remove_PM.md": "移除项目经理说明",
    "documents/remove_members.md": "移除成员说明"
  },
  "logs": {
    "logs/manage_members.log": "成员管理日志",
    "logs/update_description.log": "更新描述日志"
  },
  "requirements.txt": "依赖包要求",
  "scripts": {
    "scripts/manage_members.py": "成员管理脚本",
    "scripts/update_description.py": "更新描述脚本"
  }
}
```

## 📜 项目功能

### 1. 自动化队伍管理工作流 🤖
我们在 `.github/workflows/automated_party_management.yml` 中定义了一个名为“队伍自动化管理”的工作流。它每10分钟自动运行一次，而且也可以手动触发。这个工作流的主要目的是通过 Python 脚本管理和更新队伍成员信息，包含以下几个重要步骤：

- **代码检出**：获取代码库的最新代码。
- **设置 Python 环境**：安装 Python 3.8。
- **安装依赖项**：安装脚本所需的 `requests` 库。
- **运行管理脚本**：执行 `manage_members.py` 脚本进行成员管理。
- **限制请求频率**：通过休眠命令防止过载 API。
- **运行更新脚本**：执行 `update_description.py` 脚本更新描述。
- **记录更改**：记录所有操作并将日志提交到仓库。

### 2. 许可证 📝
项目包含 `LICENSE` 文件，使用 Apache License, Version 2.0，为您提供使用、复制和分发本软件的条款和条件。

### 3. 依赖项 📦
项目中的 `requirements.txt` 文件列出了项目运行所需的外部库，这里需要的库是 `requests`，这是一种流行的 HTTP 库，用于处理网络请求和响应。

### 4. 成员管理脚本 🧑‍🤝‍🧑
`manage_members.py` 脚本负责管理 Habitica 平台上的队伍成员。它的主要功能包括：
- 记录日志、设置请求频率、检测不活跃成员、发送邀请等，确保队伍活跃不掉队。

### 5. 描述更新脚本 🔄
`update_description.py` 脚本每隔一段时间更新队伍的描述，结合成员信息和来自外部 API 的内容，让你的队伍描述始终充满新意和吸引力。

## 🛠️ 如何运行
- 确保你有 Python 环境，并且安装了 `requirements.txt` 中的依赖库。
- 通过执行 `manage_members.py` 和 `update_description.py` 脚本，手动运行成员管理与描述更新。
- 你也可以依赖自动化工作流，设置定时任务，轻松维护队伍信息。🎈

## 🌐 多语言支持
项目附带了多种语言的说明文档，包括中文、德语、英语、西班牙语、法语和日语，确保每位用户都能方便地理解项目内容！🌍

## 📬 反馈与支持
欢迎向我们提交问题或建议，一起让这个项目变得更好！🙏

感谢您阅读！愿您的队伍在 Habitica 上充满活力，永远走在成功的路上！💪✨