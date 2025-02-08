[Back to main language README](README.md)

# 🎉 Automated Team Management Project

Welcome to our **Automated Team Management Project**! 🚀 This project aims to effortlessly manage team members on the Habitica platform through automation scripts, keeping the team active and enhancing management efficiency. Let's take a look at the structure and functionality of this project!

## 📁 Project Structure

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/automated_party_management.yml": "Automated Team Management Workflow"
    }
  },
  "LICENSE": "License file",
  "README.md": "Project documentation",
  "README": {
    "README/README_Deutsch.md": "German documentation",
    "README/README_English.md": "English documentation",
    "README/README_Español.md": "Spanish documentation",
    "README/README_Français.md": "French documentation",
    "README/README_日本語.md": "Japanese documentation",
    "README/README_繁体中文.md": "Traditional Chinese documentation"
  },
  "documents": {
    "documents/brief_description.md": "Brief project description",
    "documents/new_members.md": "Introduction of new members",
    "documents/party_description.md": "Team description",
    "documents/remove_PM.md": "Removing project manager instructions",
    "documents/remove_members.md": "Removing members instructions"
  },
  "logs": {
    "logs/manage_members.log": "Member management log",
    "logs/update_description.log": "Update description log"
  },
  "requirements.txt": "Dependency requirements",
  "scripts": {
    "scripts/manage_members.py": "Member management script",
    "scripts/update_description.py": "Update description script"
  }
}
```

## 📜 Project Features

### 1. Automated Team Management Workflow 🤖
We have defined a workflow called “Automated Team Management” in `.github/workflows/automated_party_management.yml`. It runs automatically every 10 minutes but can also be triggered manually. The main purpose of this workflow is to manage and update team member information through Python scripts, which includes the following key steps:

- **Checkout Code**: Fetch the latest code from the repository.
- **Set Up Python Environment**: Install Python 3.8.
- **Install Dependencies**: Install the `requests` library required for the scripts.
- **Run Management Script**: Execute the `manage_members.py` script for member management.
- **Limit Request Rate**: Use sleep commands to prevent overloading the API.
- **Run Update Script**: Execute the `update_description.py` script to update descriptions.
- **Record Changes**: Log all actions and commit the logs to the repository.

### 2. License 📝
The project includes a `LICENSE` file, using the Apache License, Version 2.0, which provides you terms and conditions for using, copying, and distributing this software.

### 3. Dependencies 📦
The `requirements.txt` file in the project lists the external libraries required to run the project. The library needed here is `requests`, a popular HTTP library used for handling network requests and responses.

### 4. Member Management Script 🧑‍🤝‍🧑
The `manage_members.py` script is responsible for managing team members on the Habitica platform. Its main functions include:
- Logging, setting request rates, detecting inactive members, sending invites, etc., ensuring the team remains active and engaged.

### 5. Description Update Script 🔄
The `update_description.py` script regularly updates the team's description, combining member information with content from external APIs, keeping your team description fresh and appealing.

## 🛠️ How to Run
- Ensure you have a Python environment set up and the dependencies in `requirements.txt` installed.
- Manually run the member management and description update by executing the `manage_members.py` and `update_description.py` scripts.
- You can also rely on the automated workflow set up a cron job to maintain team information easily. 🎈

## 🌐 Multilingual Support
The project comes with documentation in multiple languages, including Chinese, German, English, Spanish, French, and Japanese, ensuring every user can easily understand the project content! 🌍

## 📬 Feedback and Support
Feel free to submit any questions or suggestions to help make this project even better! 🙏

Thank you for reading! May your team be vibrant on Habitica and always succeed on the path to success! 💪✨