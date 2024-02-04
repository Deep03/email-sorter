# Email Sorter using Gmail API**

This repository contains a Python script that connects to Gmail using the Gmail API and sorts emails into custom labels based on predefined rules.

### Features

- Automatically sorts incoming emails into custom labels.
- Uses the Gmail API for secure access to email data.
- Customizable rules for sorting emails based on sender, subject, or other criteria.

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Deep03/email-sorter.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the Gmail API:
   
    - Follow the instructions in the [Gmail API Quickstart Guide](https://developers.google.com/gmail/api/quickstart/python) to enable the Gmail API for your Google account.
    - Download the `credentials.json` file and save it in the project directory.

4. Configure custom labels and rules:

    - Open the `config.json` file and define your custom labels and sorting rules. For example:

    ```json
    {
        "labels": {
            "work": ["work@example.com"],
            "friends": ["friend1@example.com", "friend2@example.com"]
        },
        "default_label": "other"
    }
    ```

### Usage

- Run the script `email_sorter.py`:

    ```bash
    python email_sorter.py
    ```

- The script will connect to your Gmail account, fetch unread emails, and sort them into the specified custom labels based on your rules.

### Email Sorter

**For M1/M2 tensorflow-text:**
- download from: https://github.com/sun1638650145/Libraries-and-Extensions-for-TensorFlow-for-Apple-Silicon/releases/tag/v2.15
- Download tensorflow_text-2.15.0-cp39-cp39-macosx_11_0_arm64.whl or the one for your device


**NLT resources**
- You may need to download these resources:
    - nltk.download('punkt')
    - nltk.download('stopwords')
    - nltk.download('wordnet')
 
### Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or create a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Disclaimer

This script accesses your Gmail account and may modify your email labels. Use it responsibly and at your own risk.
