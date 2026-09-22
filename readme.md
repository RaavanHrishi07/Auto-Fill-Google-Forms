# 🤖 Auto-Fill Google Forms

A Python-based **Google Forms automation tool built with Selenium WebDriver**.

The program reads data from a CSV file and automatically enters the information into the corresponding fields of a Google Form using Mozilla Firefox.

---

## 🎮 Features

- 📝 Automatically fills Google Form fields
- 📄 Reads input data from a CSV file
- 🌐 Automatically opens Google Forms in Firefox
- 🤖 Browser automation using Selenium WebDriver
- 🔧 Uses XPath selectors to locate form fields
- 📊 Supports multiple entries from CSV data
- 🔄 Automates repetitive form-filling tasks
- 🦊 Uses GeckoDriver for Firefox automation
- ⚡ Simple CSV-based input system
- 🛠️ Easy to customise for different Google Forms

---

## 🛠️ Technologies Used

- **Python 3**
- **Selenium WebDriver**
- **Mozilla Firefox**
- **GeckoDriver**
- **CSV**

---

## 📂 Project Structure

```text
Auto-Fill-Google-Forms/
│
├── test.py
├── input.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/RaavanHrishi07/Auto-Fill-Google-Forms.git
```

### 2. Navigate to the Project

```bash
cd Auto-Fill-Google-Forms
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Install Browser Requirements

Make sure the following are installed:

- Mozilla Firefox
- GeckoDriver
- Python 3
- pip

---

## 📋 Input CSV

The `input.csv` file contains the information that will be entered into the Google Form.

Example:

```csv
Name,Email,Phone
John Doe,john@example.com,9876543210
Jane Doe,jane@example.com,9876543211
```

The CSV columns should match the data expected by the Python script.

Use dummy or test information while experimenting with the project.

---

## ⚙️ Configuration

Open `test.py` and configure the following:

- Google Form URL
- XPath selectors for the form fields
- CSV input data
- GeckoDriver path

If the Google Form structure changes, the XPath selectors may need to be updated.

---

## ▶️ How to Run

### 1. Prepare the CSV File

Add the required information to:

```text
input.csv
```

### 2. Check the Google Form URL

Open `test.py` and make sure the Google Form URL is correct and accessible.

### 3. Run the Program

```bash
python test.py
```

Firefox will open automatically and Selenium will navigate to the configured Google Form.

The script will then read the CSV data and enter it into the corresponding form fields.

---

## 🔄 How It Works

1. The program starts Firefox using Selenium WebDriver.
2. The configured Google Form is opened.
3. The CSV file is read row by row.
4. The required form fields are located using XPath.
5. Data from the CSV file is entered into the form.
6. The form is submitted.
7. The process can be repeated for multiple entries.

---

## 🧪 Testing

The project was tested locally using:

```text
Python 3.11.9
Selenium 4.49.0
Mozilla Firefox
GeckoDriver 0.37.1
```

The following components were tested:

- Firefox browser launch
- GeckoDriver connection
- Google Form navigation
- XPath-based element selection
- CSV data handling
- Automated form interaction

---

## ⚠️ Important Notes

- The Google Form must be active and accessible.
- The Google Form URL must be valid.
- XPath selectors depend on the structure of the Google Form.
- If the form fields change, the XPath selectors may need to be updated.
- Some Google Forms may require users to sign in before submitting responses.
- Do not use sensitive or private information in `input.csv` when sharing the project publicly.
- Use this automation only on forms where you have permission to automate submissions.

---

## 💡 Future Improvements

Possible future improvements include:

- 📊 CSV validation
- 🛡️ Better error handling
- 🔄 Automatic retry mechanism
- ⏱️ Configurable delay between submissions
- 📝 Support for additional Google Form field types
- 📋 Automatic form field detection
- 📊 Detailed submission logs
- 🖥️ Graphical User Interface (GUI)
- 📈 Progress tracking
- ⚙️ Configuration file support

---

## 🎯 Purpose

This project was created to practise and demonstrate:

- Python programming
- Selenium WebDriver
- Browser automation
- CSV data handling
- XPath selectors
- Web form automation
- Automated task processing

---

## 👨‍💻 Author

**Hrishikesh Sharma**

GitHub: [RaavanHrishi07](https://github.com/RaavanHrishi07)

---

## 📄 License

This project is intended for educational and personal use.