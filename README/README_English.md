- [简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# Project Introduction 📚

Welcome to the **Habitica Team Automation Management Project**! 🎉 This project aims to enhance your experience on the Habitica platform by optimizing member management through automation tools and scripts. Whether you're part of the game or just want to manage your team effortlessly, our tools are here to help you!

## Project Structure 📂

Here’s the structure of the project, ensuring you can easily find the files you need:

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

## File Descriptions 🔍

### Automated Team Management (`.github/workflows/automated_party_management.yml`)
This file defines a GitHub Actions workflow named "Team Automation Management." It runs automatically every 10 minutes or can be triggered manually, performing the following functions:
- Checks out the code repository
- Sets up a Python 3.8 environment
- Installs the required libraries (like `requests`)
- Executes management scripts (`manage_members.py` and `update_description.py`) to interact with the Habitica API
- Sets delays between script executions to prevent exceeding API rate limits
- Commits and pushes log changes to document updates to the management scripts

### License (`LICENSE`)
This project follows the Apache License 2.0, aimed at promoting open-source collaboration and protecting the rights of creators and users. The license details the terms and conditions for using, copying, and distributing software and other works.

### Dependency File (`requirements.txt`)
This file lists the external libraries and dependencies needed for the project, currently only containing the `requests` library, which provides a simple way to send HTTP requests and handle responses.

### Member Management Script (`scripts/manage_members.py`)
This script is used to manage members on the Habitica platform, automating the following tasks:
- Removing inactive members and notifying them
- Inviting new users seeking to join the team

### Description Update Script (`scripts/update_description.py`)
This script is responsible for updating the Habitica team's description, dynamically fetching and updating content. Its key features include:
- Daily inspirational quotes obtained from an external API
- Automatic updates to the team description, ensuring the information stays fresh!

## Log Files 📜
All executed operations are logged in the `logs` folder, making it easy for you to review execution history and troubleshoot potential issues.

## Getting Started 🚀

1. Clone the project repository
2. Install dependencies: `pip install -r requirements.txt`
3. Use GitHub Actions for an automated workflow and enjoy a seamless member management experience!

## Contributing 💡
If you would like to contribute to this project, feel free to submit a PR or raise an issue! Let’s make Habitica even more exciting together! ⭐️

Thank you for reading this project's README file! We look forward to your participation and support, so come and ⭐️ this project!