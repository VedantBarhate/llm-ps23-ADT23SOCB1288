
# Concept Explainer (ELI5)

## Problem Statement
Complex topics can be difficult for beginners to understand. This project explains any given concept at three different levels: Kid, Student, and Expert.

## Technologies Used
- Python
- Streamlit
- Groq API
- Llama 3.3 70B Versatile
- Python-dotenv

## Features
- Accepts any concept as input.
- Generates three levels of explanations.
- Uses simple language for beginners.
- Provides detailed explanations for students.
- Provides technical explanations for experts.
- Displays explanations in separate tabs.

## Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   cd concept-explainer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory:

   ```env
   GROQ_API_KEY=your_groq_api_key
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the application in your browser.
2. Enter a concept in the input field.
3. Click **Explain Concept**.
4. View the explanations in Kid, Student, and Expert tabs.

## Project Structure

```text
concept-explainer/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## LLM Used
qwen/qwen3.8-27b through the Groq API.

## Author
Vedant Barhate
