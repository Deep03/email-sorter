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

### Usage

- Run the script `email_sorter.py`:

    ```bash
    python email_sorter.py
    ```

- The script will connect to your Gmail account, fetch unread emails, and sort them into the specified custom labels based on your rules.

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

This project is licensed under the MIT License.
### Disclaimer

This script accesses your Gmail account for your emails and modifies your email labels. Use it responsibly and at your own risk.
