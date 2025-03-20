# 🎉 自动化党派管理系统 📈

欢迎来到 **自动化党派管理系统** 项目！我们致力于为 Habitica 用户提供一个高效、便捷的党派管理工具。无论您是热爱管理的领袖，还是希望活跃参与的成员，这里都有您需要的工具与文档！✨

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

- **automated_party_management.yml**: 😎 这个 GitHub Actions 工作流文件每 10 分钟运行一次，自动管理团队任务。它设置 Python 环境，安装依赖，并运行管理成员和更新描述的脚本，确保您的党派始终保持活跃！

- **brief_description.md**: 📖 提供每日一句和翻译，促进语言学习和参与。包含最后更新的时间和成员信息，通过定时操作自动更新，保持内容新鲜！

- **new_members.md**: 👫 记录新邀请的成员，强调社区参与。这个文档通过定时操作来维护，保证您不会漏掉任何新朋友的加入！

- **party_description.md**: 🌟 阐述党派的宗旨和规则，鼓励成员分享体验，积极参与任务！这份文档还有关于存在主义与虚无主义的讨论，帮助您在生活中寻找意义。

- **remove_PM.md**: 🚪 一份通知模版，告知因未活跃而移除的成员，并提供重新加入的选项，让沟通更加友好和高效。

- **remove_members.md**: ⚠️ 记录移除成员的原因和链接，确保透明化管理。该文档通过定期操作更新，方便审核和记录。

- **requirements.txt**: 📦 列出所需的 Python 依赖，确保您的环境设置一致，轻松安装所需库！

- **manage_members.py**: 🤖 管理党派成员的脚本，包括删除不活跃成员、发送邀请和日志记录等功能，让管理变得自动化、轻松！

- **update_description.py**: 📅 自动更新党派描述的脚本，确保您每天都有新内容与各位成员分享，增强参与感！

## 🌟 如何贡献

如果您觉得这个项目对您有帮助，或者想要一起参与其中，欢迎给我们项目加个 ⭐️！您的支持是我们最大的动力！欢迎提建议、报告问题或者贡献代码，我们期待您的加入！💪

## 📧 联系我们

如果您有任何问题或建议，请随时通过电子邮件与我们联系！我们会尽快回复您！😉

感谢您对自动化党派管理系统的关注，祝您使用愉快！🎉