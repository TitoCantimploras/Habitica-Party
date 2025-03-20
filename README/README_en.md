<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 🎉 Automated Guild Management System 📈

Welcome to the **Automated Guild Management System** project! Our goal is to provide Habitica users with an efficient and convenient tool for guild management. Whether you're a passionate leader or a member looking to engage actively, we have the tools and documentation you need! ✨

## 🚀 Project Structure

```
.
├── .github
│   └── workflows
│       └── automated_party_management.yml    # GitHub Actions workflow file
├── LICENSE                                    # Project license
├── documents                                  # Project documentation folder
│   ├── brief_description.md                   # Brief description document 
│   ├── new_members.md                         # New members list document 
│   ├── party_description.md                   # Guild description document 
│   ├── remove_PM.md                           # Member removal notification template 
│   └── remove_members.md                      # Member removal record template 
├── logs                                        # Log folder
│   ├── manage_members.log                     # Member management log
│   └── update_description.log                 # Description update log
├── requirements.txt                           # Dependency file 
└── scripts                                     # Scripts directory
    ├── manage_members.py                      # Script for managing members 
    └── update_description.py                  # Script for updating the guild description 
```

## 📄 File Overview

| Filename                                 | Description                                                  |
|-----------------------------------------|-----------------------------------------------------------|
| **automated_party_management.yml**      | A GitHub Actions workflow file that runs automatically every 10 minutes to manage team tasks. By setting up a Python environment, installing dependencies, and executing member management and description update scripts, it ensures your guild stays active! 🎯 |
| **brief_description.md**                | Provides a daily quote and its translation, promoting language learning and community engagement. This document also updates the latest member information automatically, ensuring fresh content. 🌱 |
| **new_members.md**                      | Records invitations for new members, emphasizing community engagement. This document updates periodically, ensuring you don't miss any new participants joining! 👥 |
| **party_description.md**                | Outlines the guild's mission and rules, encouraging members to share personal experiences and actively participate in tasks. It also includes discussions on existentialism and nihilism, aiding you in exploring deeper meanings in life. 📚 |
| **remove_PM.md**                        | A friendly notification template used to inform members removed due to inactivity, providing an option for rejoining, enhancing the friendliness and efficiency of communication. 🤝 |
| **remove_members.md**                   | Records reasons for member removal and related links, ensuring transparency in the management process, and updated regularly for auditing and record-keeping. 🔍 |
| **requirements.txt**                    | Lists the required Python dependencies to ensure your environment is set up consistently for easy installation of necessary libraries. ⚙️ |
| **manage_members.py**                   | A script for managing guild members, including functions for removing inactive members, sending invitations, and logging, which simplifies the management process. ⚡️ |
| **update_description.py**               | A script for automatically updating the guild description, ensuring you have daily updated content to share with members, enhancing engagement. 🌟 |

## How to Use

1. **Fork this project**: Click on the "**Fork**" button in the upper right corner.
2. **Configure API Token**: Set up your Habitica API token and ID in the Actions secrets of your cloned project.
3. **Customize Templates**: Modify the templates in the `documents` folder as needed, ensuring placeholders are not broken.
4. **Enjoy Automated Management**: Once you've completed these steps, you'll be able to achieve the desired automated management! 🚀

## 🌟 How to Contribute

If you find this project helpful or wish to get involved, feel free to give our project a ⭐️! Your support is our greatest motivation! We're looking forward to your suggestions, bug reports, or code contributions—your participation is welcome! 💪

## 📧 Contact Us

If you have any questions or suggestions, please feel free to reach out through Issues, and we will respond as soon as possible! 😉

Thank you for your interest in the Automated Guild Management System, and happy using! 🎉