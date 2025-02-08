[Back to main language README](README.md)

# 🥳 Automated Team Management Tool README

Welcome to our Automated Team Management Tool! This project aims to enhance team management efficiency and engagement through integration with the Habitica API. 💼✨

## 📁 File Overview

### 1. GitHub Actions Workflow
- **Path**: `.github/workflows/automated_party_management.yml`
- **Functionality**: This workflow triggers every 10 minutes (can also be run manually) and includes the following key steps:
  - Check out code
  - Set up Python environment
  - Install dependencies
  - Execute management scripts to handle team members on the Habitica platform
  - Run update scripts to log changes
- **Features**: Includes a pause function to manage request rates, and finally commits and pushes any log changes to the repository. 🔄

### 2. License Agreement
- **File Name**: `LICENSE`
- **Content**: Contains the Apache License, Version 2.0, outlining the terms and conditions for the use, reproduction, and distribution of the software and related works, including definitions, user permissions, redistribution requirements, and disclaimers. 📜

### 3. Member Management Script
- **File Name**: `manage_members.py`
- **Functionality**: This Python script is designed to manage team members on the Habitica platform, with key features including:
  - **Logging Setup**: Initializes logging to track script operations, including errors and general information.
  - **Rate Limiting**: Implements mechanisms to adhere to API request limits by managing request timing.
  - **Member Management**:
    - Identify and retrieve inactive team members based on last login time.
    - Send private notifications before removing members.
    - Send notifications to team chat regarding member removals.
  - **Invitation Feature**: Look for users seeking teams and send them invitations, including a formatted message listing the invited members.
  - **Utilities**: Contains helper functions for handling API responses, sending messages, and calculating time based on user activity.

In summary, this script enhances Habitica team management by automating the removal of inactive users and inviting new ones, fostering better user engagement. 🎉

### 4. Description Update Script
- **File Name**: `update_description.py`
- **Functionality**: This Python script is aimed at updating the Habitica team's description, featuring:
  - Daily fetching of a quote and details on team members' last login.
  - Logging and rate limiting for executing API requests.
  - Dynamically updating the team description based on retrieved data.
  - Reading description formats from a template file, compiling member information, and sending update requests to the Habitica API.
  - Logging successes and errors during the operation.

## 🛠️ Installation and Use

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/repository.git
   cd repository
   ```

2. Set up the Python environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure GitHub Actions workflow (if needed) and generate a valid key in the Habitica API.

5. Run the scripts:
   ```bash
   python manage_members.py
   python update_description.py
   ```

## 💡 Contributions

We welcome any form of contribution! If you have suggestions or questions, please submit an issue or open a pull request. 😊

## 📞 Contact

If you have any questions or feedback, please reach out to me via:
- Email: your_email@example.com
- GitHub: [Your GitHub Username](https://github.com/yourusername)

Thank you for using our tool, and we wish you smooth team management in Habitica! 🎊