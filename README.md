# Habitica Party Management Script

## Overview

This script is designed to manage members of a Habitica party, including inviting new members, removing inactive members, and sending messages to users. It utilizes the Habitica API to perform these actions and is intended to be run in a GitHub Actions environment.

## Features

- **Invite New Members**: Searches for users looking to join a party and sends them invitations.
- **Remove Inactive Members**: Identifies and removes members who have been inactive for a specified duration.
- **Send Messages**: Sends private messages to users and updates the party chat with relevant information.
- **Logging**: Logs actions and errors for debugging and tracking purposes.

## Requirements

- **Environment Variables**: The script requires `HABITICA_USER_ID` and `HABITICA_API_KEY` to authenticate with the Habitica API.
- **GitHub Actions**: The script is configured to run in a GitHub Actions environment.

## Usage

1. **Set Up Environment Variables**: Ensure that `HABITICA_USER_ID` and `HABITICA_API_KEY` are set in the GitHub repository secrets.
2. **Schedule GitHub Actions**: Configure the GitHub Actions workflow to run the script at desired intervals.
3. **Run the Script**: The script will automatically perform the management tasks when triggered by the GitHub Actions workflow.

## Files

- `manage_members.py`: The main script for managing Habitica party members.
- `documents/new_members.md`: Template for the message sent when new members are invited.
- `documents/remove_PM.md`: Template for the private message sent to members before they are removed.
- `documents/remove_members.md`: Template for the message sent to the party chat when members are removed.

## Logging

The script uses a `RotatingFileHandler` to log messages to `logs/manage_members.log`. It also logs info-level messages to the console.

## Rate Limiting

The script includes a rate-limiting mechanism to prevent exceeding the Habitica API's rate limits.

## Error Handling

The script logs errors encountered during API requests and continues execution where possible.

## Contributions

Contributions to the script are welcome. Please follow the standard GitHub pull request process.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

# Habitica Update Description Script

## Overview

This script updates the description of a Habitica party with a daily sentence, its translation, and a list of party members along with their last login times. It is designed to be run in a GitHub Actions environment.

## Features

- **Daily Sentence**: Fetches a daily sentence and its translation from a third-party API.
- **Member Details**: Retrieves details of party members, including their last login times.
- **Update Description**: Formats and updates the party description with the fetched sentence, translation, and member details.
- **Logging**: Logs actions and errors for debugging and tracking purposes.

## Requirements

- **Environment Variables**: The script requires `HABITICA_USER_ID` and `HABITICA_API_KEY` to authenticate with the Habitica API.
- **GitHub Actions**: The script is configured to run in a GitHub Actions environment.

## Usage

1. **Set Up Environment Variables**: Ensure that `HABITICA_USER_ID` and `HABITICA_API_KEY` are set in the GitHub repository secrets.
2. **Schedule GitHub Actions**: Configure the GitHub Actions workflow to run the script daily or at desired intervals.
3. **Run the Script**: The script will automatically update the party description when triggered by the GitHub Actions workflow.

## Files

- `update_description.py`: The main script for updating the Habitica party description.
- `documents/brief_description.md`: Template for the party description format.

## Logging

The script uses a `RotatingFileHandler` to log messages to `logs/update_description.log`. It also logs info-level messages to the console.

## Error Handling

The script logs errors encountered during API requests and continues execution where possible.

## Contributions

Contributions to the script are welcome. Please follow the standard GitHub pull request process.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Please note that the actual implementation of the GitHub Actions workflow is not included in this README and should be configured separately in the `.github/workflows` directory of the repository.
