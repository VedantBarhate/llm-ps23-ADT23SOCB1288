
import os
import json
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Concept Explainer",
    page_icon="🧠",
    layout="centered"
)

# Initialize Groq client
api_key = os.getenv("GROQ_API_KEY")

# Application heading
st.title("🧠 Concept Explainer")
st.subheader("Understand anything at three different levels")

st.write(
    "Enter a complex concept and get explanations "
    "designed for kids, students and experts."
)

# Input section
concept = st.text_input(
    "Enter a concept",
    placeholder="e.g. Artificial Intelligence, Neural Networks..."
)

# Prompt engineering
def generate_prompt(concept):

    return f"""
You are an expert educational content creator.

Explain the following concept at exactly three
different levels of understanding:

Concept: {concept}

Return the response as a valid JSON object with
exactly these three keys:

1. kid:
Explain the concept as if teaching a 10-year-old.
Use very simple words, relatable analogies and
everyday examples. Avoid technical jargon.

2. student:
Explain the concept to a college student.
Include a proper definition, working principles,
important components and relevant examples.

3. expert:
Explain the concept to someone with advanced
technical knowledge.
Include technical terminology, underlying
mechanisms, relevant theories and deeper insights.

Important instructions:
- All three explanations must be accurate.
- Gradually increase the technical depth.
- Avoid repeating the same explanation.
- Use examples wherever appropriate.
- Do not mix the three levels.
- Return only valid JSON without Markdown fences.

Expected JSON structure:

{{
    "kid": "Explanation...",
    "student": "Explanation...",
    "expert": "Explanation..."
}}
"""


# Generate explanations
def explain_concept(concept):

    client = Groq(api_key=api_key)

    prompt = generate_prompt(concept)

    response = client.chat.completions.create(
        model="qwen/qwen3.8-27b",
        messages=[
            {
                "role": "system",
                "content": "You are an educational AI assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_completion_tokens=2500,
        response_format={"type": "json_object"}
    )

    result = response.choices[0].message.content

    return json.loads(result)


# Generate button
if st.button("Explain Concept", type="primary"):

    if not concept.strip():
        st.warning("Please enter a concept first.")

    elif not api_key:
        st.error("Groq API key not found. Check your .env file.")

    else:
        try:
            with st.spinner("Generating explanations..."):

                explanations = explain_concept(concept.strip())

            st.success(f"Explanations generated for: {concept}")

            # Display three levels in separate tabs
            kid_tab, student_tab, expert_tab = st.tabs(
                ["🧒 Kid Level", "🎓 Student Level", "🧠 Expert Level"]
            )

            with kid_tab:
                st.markdown("### Simple Explanation")
                st.write(explanations["kid"])

            with student_tab:
                st.markdown("### Student Explanation")
                st.write(explanations["student"])

            with expert_tab:
                st.markdown("### Advanced Explanation")
                st.write(explanations["expert"])

        except json.JSONDecodeError:
            st.error("The model returned an invalid response. Please try again.")

        except Exception as e:
            st.error(f"Something went wrong: {e}")
