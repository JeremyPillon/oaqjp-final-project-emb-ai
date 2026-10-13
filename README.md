t# Emotion Detection Web Application

An end-to-end Python web application that performs real-time emotion detection on text statements using IBM Watson's Natural Language Processing (NLP) runtime. Built with **Flask**, **JavaScript**, and **Bootstrap**, this project demonstrates complete microservice integration, unit testing, error handling, and static code analysis.

---

## Features

- **Watson NLP Integration:** Analyzes input text to calculate confidence scores for five core emotions: `anger`, `disgust`, `fear`, `joy`, and `sadness`.
- **Dominant Emotion Identification:** Dynamically evaluates and extracts the primary emotion expressed in the statement.
- **Robust Error Handling:** Seamlessly manages invalid queries, empty inputs, and HTTP 400 response codes by returning safe fallback structures and friendly UI alerts.
- **Interactive Front-End:** Web interface powered by HTML5, JavaScript (AJAX), and Bootstrap for real-time analysis without full page reloads.
- **High Code Quality:** Tested via unit tests with mock responses and formatted to achieve a **10/10 Pylint score**.

---

## Project Architecture & Tech Stack

- **Backend:** Python 3.11, Flask
- **Frontend:** HTML, JavaScript (Async/XHR), Bootstrap 4
- **NLP Service:** IBM Watson NLP Runtime API
- **Testing & Quality:** `unittest`, `pylint`

---

## Directory Structure

```text
├── emotion_detection.py      # Core NLP API integration module
├── server.py                 # Flask web server routing & request handling
├── test_emotion_detection.py # Unit tests for the emotion detector logic
├── static/
│   └── mywebscript.js        # Frontend JavaScript handling AJAX requests
└── templates/
    └── index.html            # Main web page user interface
```

---

## Getting Started

### Prerequisites

Ensure you have Python 3.11+ and `pip` installed:

```bash
python3 --version
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JeremyPillon/oaqjp-final-project-emb-ai.git
   cd oaqjp-final-project-emb-ai
   ```

2. **Install required dependencies:**
   ```bash
   pip install flask requests pylint
   ```

---

## Running the Application

1. **Start the Flask server:**
   ```bash
   python3 server.py
   ```

2. **Access the application:**
   Open your browser and navigate to `http://localhost:5000` (or the provided cloud environment proxy URL).

3. **Analyze Emotion:**
   - Enter text into the input field (e.g., `"I love learning new technologies!"`).
   - Click **Run Sentiment Analysis**.
   - View the individual emotion scores along with the identified dominant emotion.

---

## Testing & Quality Assurance

### Running Unit Tests
To verify emotion detection behavior across various sentiment scenarios:

```bash
python3 -m unittest test_emotion_detection.py
```

### Static Code Analysis (Pylint)
To run code quality checks against PEP 8 standards:

```bash
pylint server.py
```

*Current Pylint Rating: **10.00/10***

---

## License

This project was developed as part of the **IBM Software Engineering Professional Certificate** on Coursera.
