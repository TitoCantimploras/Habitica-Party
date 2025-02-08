- [切換語言: 繁體中文](README/README_繁体中文.md)
- [Switch Language: English](README/README_English.md)
- [Cambiar idioma: Español](README/README_Español.md)
- [Changer de langue: Français](README/README_Français.md)
- [Sprache wechseln: Deutsch](README/README_Deutsch.md)
- [言語を切り替える: 日本語](README/README_日本語.md)

# 📚 项目简介 README

欢迎来到我们的项目！🎉 在这里，我们致力于通过自动化工具来管理 Habitica 社区的团队成员，让团队管理更加高效和轻松。接下来，让我们了解一下这个项目的结构和功能吧！✨

## 📁 项目结构

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/automated_party_management.yml": "automated_party_management.yml"
    }
  },
  "LICENSE": "LICENSE",
  "README.md": "README.md",
  "README": {
    "README/README_Deutsch.md": "README_Deutsch.md",
    "README/README_English.md": "README_English.md",
    "README/README_Español.md": "README_Español.md",
    "README/README_Français.md": "README_Français.md",
    "README/README_日本語.md": "README_日本語.md",
    "README/README_繁体中文.md": "README_繁体中文.md"
  },
  "documents": {
    "documents/brief_description.md": "brief_description.md",
    "documents/new_members.md": "new_members.md",
    "documents/party_description.md": "party_description.md",
    "documents/remove_PM.md": "remove_PM.md",
    "documents/remove_members.md": "remove_members.md"
  },
  "logs": {
    "logs/manage_members.log": "manage_members.log",
    "logs/update_description.log": "update_description.log"
  },
  "requirements.txt": "requirements.txt",
  "scripts": {
    "scripts/manage_members.py": "manage_members.py",
    "scripts/update_description.py": "update_description.py"
  }
}
```

## 📝 文件简介

### GitHub Actions 自动化工作流

在 `.github/workflows/automated_party_management.yml` 文件中，定义了一个 GitHub Actions 工作流，用于自动管理团队成员。它每 10 分钟触发一次，或可手动调用，运行在 Ubuntu 环境中，包含多个关键步骤：

1. **检出代码**：获取项目代码。
2. **搭建 Python 环境**：配置 Python 3.8。
3. **安装依赖**：安装需要的 `requests` 库。
4. **执行管理脚本**：运行管理成员的 Python 脚本（`manage_members.py`），使用环境变量管理用户凭证。
5. **速率限制**：引入暂停以管理请求速率。
6. **执行更新脚本**：运行更新说明的脚本（`update_description.py`），同样使用环境变量。
7. **记录更改**：将脚本生成的日志更新提交到代码库。
8. **推送更改**：将更新的日志推送回远程代码库。

这个工作流旨在高效自动化团队成员的管理和日志的更新工作，真是个聪明的助手！🤖

### 许可文件

`LICENSE` 文件是 Apache 许可证 2.0，作为一种宽松的开源软件许可证，它为软件及其他作品的使用、复制和分发奠定了条款和条件。它赋予用户改革、修改和分发作品的权利，并确保对原作者的适当致谢。同时，文件中还包含商标使用、保证免责的条款及责任限制。这份文档旨在促进开发者间的合作与用户的使用，维护软件自由，同时保护原作者的权利。

### 依赖文件

`requirements.txt` 文件列出了项目运行所需的外部程序包和库。在本项目中，它仅列出了 `requests` 库，这是一个广受欢迎的 Python 模块，它使得开发者能够轻松发送 HTTP 请求，与网页服务和 API 进行互动。使用简洁的命令 `pip install -r requirements.txt`，你就可以轻松安装这些依赖，立刻开始你的魔法之旅！✨

### 脚本文件

- **成员管理脚本 `manage_members.py`**

  这个脚本用于管理 Habitica 团队中的成员，执行以下主要功能：

  1. **日志记录**：使用日志模块记录操作和错误，存储在旋转日志文件中，并在控制台输出重要信息。
  2. **速率限制的 API 请求**：定义一个辅助函数以确保请求遵循规定的间隔。
  3. **用户管理**：获取团队成员列表，检查不活跃成员并将其移除。
  4. **消息发送**：可向用户发送私信，并在团队聊天中发布成员邀请和移除消息。
  5. **邀请新用户**：对寻找团队的新用户发送邀请，并在聊天中通知团队。

  通过这些功能，这个脚本极大地简化了 Habitica 团队成员的管理，让社区管理变得更加轻松愉快！🎈

- **更新描述脚本 `update_description.py`**

  此脚本通过整合每日句子和成员活动信息，自动更新 Habitica 团队描述。其主要功能包括：

  1. **速率限制的 API 请求**：管理请求的间隔，防止过载 Habitica API。
  2. **每日句子获取**：从外部 API 获取每日句子，获取其英文内容和翻译。
  3. **成员数据收集**：收集团队成员的信息，包括最后登录时间和上次活跃时长。
  4. **描述格式化**：读取 Markdown 模板并格式化为当前内容、成员信息和时间戳。
  5. **更新阐释**：将更新的描述发送回 Habitica API。

  通过这样的自动化手段，该脚本不断提升团队描述的吸引力和成员互动，简直是个文艺范儿的朋友！🎨

---

感谢您查看我们的项目！希望我们提供的工具能为您的 Habitica 社区管理带来便利与乐趣。如有任何问题，请随时联系！🎈👋