<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 🎉 Automated Party Management System 📈

Welcome to the **Automated Party Management System** project! Our goal is to provide Habitica users with an efficient and convenient Party management tool. Whether you are a management-loving leader or a member eager to participate, we have the tools and documentation you need right here! ✨

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
│   ├── party_description.md                   # Party description document
│   ├── remove_PM.md                           # Member removal notification template
│   └── remove_members.md                      # Remove members record template
├── logs                                        # Log folder
│   ├── manage_members.log                     # Member management log
│   └── update_description.log                 # Description update log
├── requirements.txt                           # Dependency file
└── scripts                                     # Scripts directory
    ├── manage_members.py                      # Script for managing members
    └── update_description.py                  # Script for updating party description
```

## 📄 File Overview

| File Name                                 | Description                                                       |
|---------------------------------------|------------------------------------------------------------|
| **automated_party_management.yml**    | A GitHub Actions workflow file that runs automatically every 10 minutes, responsible for managing team tasks. It sets up the Python environment, installs dependencies, and executes member management and description update scripts to keep your Party active! 🎯 |
| **brief_description.md**              | Provides a daily quote and its translation to promote language learning and community engagement. This document also automatically updates with the latest member information to ensure fresh content. 🌱 |
| **new_members.md**                    | Records invitations to new members, highlighting community participation. This document is updated regularly to ensure you don't miss any new members joining! 👥 |
| **party_description.md**              | Outlines the purpose and rules of the Party, encouraging members to share their personal experiences and actively participate in tasks. It also includes discussions of existentialism and nihilism to help you explore deeper meanings in life. 📚 |
| **remove_PM.md**                      | A friendly notification template to inform members who have been removed due to inactivity, providing options for rejoining, enhancing the friendliness and efficiency of communication. 🤝 |
| **remove_members.md**                 | Records the reasons for member removals and related links, ensuring transparency in the management process and regularly updated for auditing and recording purposes. 🔍 |
| **requirements.txt**                  | Lists the required Python dependencies to ensure your environment is set up consistently for easy installation of needed libraries. ⚙️ |
| **manage_members.py**                 | Script for managing Party members, including features for removing inactive members, sending invitations, and logging activities to simplify the management process. ⚡️ |
| **update_description.py**             | Script for automatically updating the Party description, ensuring you have updated content to share with members daily, enhancing engagement. 🌟 |

## How to Use

1. **Fork this Project**: Click the "**Fork**" button in the upper right corner.
2. **Configure API Token**: Set up your Habitica API token and ID in the Actions secrets of your cloned project.
3. **Customize Templates**: Modify the templates in the `documents` folder as needed, ensuring placeholders remain intact.
4. **Enjoy Automated Management**: Once you've completed these steps, you'll be able to achieve the desired automated management! 🚀

## 🌟 How to Contribute

If you find this project helpful or want to get involved, please give our project a ⭐️! Your support is our biggest motivation! We look forward to your suggestions, bug reports, and code contributions—your participation is welcome! 💪

## 📧 Contact Us

If you have any questions or suggestions, feel free to contact us through Issues, and we will respond to you as soon as possible! 😉

Thank you for your interest in the Automated Party Management System, and we hope you enjoy using it! 🎉