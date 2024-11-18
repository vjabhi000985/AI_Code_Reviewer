# AI Code Reviewer

## Overview

AI Code Reviewer is a web application that uses Google's Generative AI to review code snippets written in JavaScript, Python, and Java. The app analyzes user-submitted code and provides detailed feedback, identifying bugs, suggesting optimizations, and offering general guidance to help developers improve their code.

## Features

- **Code Review:** Get a detailed analysis of your code, including bug detection, optimization suggestions, and user guidance.
- **Multi-Language Support:** The app can review code written in JavaScript, Python, and Java.
- **User-Friendly Interface:** Built using Streamlit for a smooth and interactive user experience.
- **Generative AI Integration:** Powered by Google's Generative AI to provide accurate and efficient code feedback.

## Deployment

You can access the deployed version of the app here:  
**Deployment link** : [aicodereviewer-epfeju6bjwruqwkc5jq38h.streamlit.app](https://aicodereviewer-epfeju6bjwruqwkc5jq38h.streamlit.app/)

## Demo Video

Watch the demonstration of the AI Code Reviewer in action:

[![AI Code Reviewer Demo](https://img.youtube.com/vi/-LCFDOVBnv8/0.jpg)](https://youtu.be/-LCFDOVBnv8)

## Installation and Setup

### Prerequisites

Before running the app locally, you need to have the following installed:

- Python 3.7+
- Streamlit
- `google-generativeai` library
- `python-dotenv` library

### Step 1: Clone the repository

```bash
git clone https://github.com/vjabhi000985/AI_Code_Reviewer.git
cd AI_Code_Reviewer
```

### Step 2: Set up the environment

- Create a .env file in the root directory of the project and add your Google API key:

```bash
GOOGLE_API_KEY=your_api_key_here
```

### Step 3: Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Run the app locally

- After the dependencies are installed and the .env file is configured, run the app using Streamlit:

```bash
streamlit run app.py
```

- This will start a local server, and you can open the app in your browser by visiting http://localhost:8501.

## Project Structure:

```
AI_Code_Reviewer/
├── app.py                # Main Streamlit app file
├── requirements.txt      # Python dependencies
├── .env                  # Store your Google API key here
└── assets/               # Folder for images or static assets (optional)
```

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is open-source and available under the MIT License.
