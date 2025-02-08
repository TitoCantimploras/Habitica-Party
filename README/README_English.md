[Back to main language README](README.md)

切换语言: 简体中文
切換語言: 繁體中文
Cambiar idioma: Español
Changer de langue: Français
Sprache wechseln: Deutsch
言語を切り替える: 日本語

# Project Self-Management System README 🌟

Welcome to our Project Self-Management System! 🎉 This project is designed for team management on the Habitica platform, automating the management of team members and updating team descriptions to ensure that every team operates smoothly. 👏

## Project Structure 🗂️

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

## Project File Descriptions 📁

### Workflow File 🔄
- **Automated Management Workflow**: This file, located at `.github/workflows/automated_party_management.yml`, manages the team periodically using GitHub Actions. It runs every 10 minutes to ensure the team status is always up to date! 💼

### License 📜
- **LICENSE**: This project is under the Apache License 2.0, detailing the terms for the use, reproduction, and distribution of the software and other works, making everything clear for everyone! ✨

### Dependency File 📦
- **requirements.txt**: This file lists the dependencies required for the project, containing just one critical library: `requests`, which simplifies sending HTTP requests! 🚀

### Script Files 🖥️
- **Member Management Script (manage_members.py)**: This script is responsible for monitoring member activity, automatically removing inactive members, inviting new members, and ensuring that our team stays vibrant! 💪

- **Description Update Script (update_description.py)**: This script is tasked with updating the team's description, including daily motivational quotes, member information, and the current time, ensuring our team is always filled with positivity! 🌈

## Contribution Guidelines 🤝

We welcome anyone interested in this project to contribute! Please ensure you follow our license and engage politely with other contributors. 🌍

## Usage Instructions 🛠️

1. **Clone the Project**: Use the following command to clone the project locally:
   ```bash
   git clone https://github.com/your-repo-url.git
   ```

2. **Install Dependencies**: Use pip to install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up GitHub Secrets**: Configure the required user ID and API key for the management scripts to ensure you have access to the Habitica API.

4. **Start the Workflow**: Trigger the workflow manually or wait for it to run automatically every 10 minutes to experience the joy of automated management! 🥳

## Logging 📊

In the `logs` folder, you can find the log files generated during the management of the team and updates to the descriptions, helping us track each action! 🪄

## Contact Us 📧

If you encounter any issues while using the project or have suggestions, feel free to reach out to us via email! 😊

Thank you for your interest and use of the project! Let’s work together to build a more active and efficient team! 🎊

---

We hope this introduction piques your interest in the project! Come and experience the fun of automated management! 🚀✨