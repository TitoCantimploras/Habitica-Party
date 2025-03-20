# 🎉 自动化党派管理系统 📈

欢迎加入 **自动化党派管理系统** 项目！我们致力于为 Habitica 用户提供高效、便捷的党派管理工具。无论您是热爱管理的领袖，还是希望积极参与的成员，这里都有您所需的工具和文档！✨

## 🚀 项目结构

```
.
├── .github
│   └── workflows
│       └── automated_party_management.yml    # GitHub Actions 工作流程文件
├── LICENSE                                    # 项目许可证
├── documents                                  # 项目文档资料夹
│   ├── brief_description.md                   # 简要描述文档 
│   ├── new_members.md                         # 新成员列表文档 
│   ├── party_description.md                   # 党派描述文档 
│   ├── remove_PM.md                           # 成员移除通知模板 
│   └── remove_members.md                      # 移除成员记录模板 
├── logs                                        # 日志文件夹
│   ├── manage_members.log                     # 成员管理日志
│   └── update_description.log                 # 描述更新日志
├── requirements.txt                           # 依赖文件 
└── scripts                                     # 脚本目录
    ├── manage_members.py                      # 管理成员的脚本 
    └── update_description.py                  # 更新党派描述的脚本 
```

## 📄 文件简介

- **automated_party_management.yml**: 该 GitHub Actions 工作流文件每 10 分钟自动运行，管理团队任务。它设置 Python 环境、安装依赖，并执行成员管理和描述更新脚本，确保您的党派始终保持活跃！

- **brief_description.md**: 本文档每日提供一句名言及其翻译，以促进语言学习和社区参与，并自动更新最新成员信息，确保内容常新。

- **new_members.md**: 记录新成员的邀请，强调社区的积极参与。该文档会通过定时操作更新，确保您不会错过任何新伙伴的加入！

- **party_description.md**: 阐述党派宗旨与规则，鼓励成员分享个人体验并积极参与任务。同时，内容中包含存在主义与虚无主义的讨论，帮助您在生活中探索更深的意义。

- **remove_PM.md**: 一份友好的通知模板，用于告知因活跃度不佳而被移除的成员，并提供重新加入的选项，提升沟通的友好度与效率。

- **remove_members.md**: 记录成员被移除的原因和相关链接，确保管理过程透明。该文档会定期更新，方便审计与记录。

- **requirements.txt**: 列出所需的 Python 依赖，确保您的环境设置一致，以便轻松安装所需库。

- **manage_members.py**: 该脚本用于管理党派成员，包括不活跃成员的删除、邀请发送及日志记录等功能，简化管理过程。

- **update_description.py**: 自动更新党派描述的脚本，确保您每日都有新的内容与成员分享，增强参与感。

## 如何使用

首先，请 fork 本项目。接着，在您的克隆项目设置中的 Actions secrets 中配置您的 Habitica API token 和 ID。然后，根据需要自定义 `documents` 文件夹中的模板，确保占位符不被破坏。完成后，您就能实现期望的自动化管理！

## 🌟 如何贡献

如果您觉得这个项目对您有所帮助，或者希望参与其中，欢迎为我们项目加个 ⭐️！您的支持是我们最大的动力！期待您提供建议、报告问题或贡献代码，欢迎您的参与！💪

## 📧 联系我们

如您有任何问题或建议，请随时通过 Issues 与我们联系，我们会尽快回复您！😉

感谢您对自动化党派管理系统的关注，祝您使用愉快！🎉