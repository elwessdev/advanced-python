import streamlit as st
import random
import requests as req

st.set_page_config(page_title="wessQuizy", page_icon="❓")
st.title("wessQuizy - Quiz App")
st.markdown("Let's test your knowledge! Answer the questions below:")


if 'score' not in st.session_state:
    st.session_state.score = 0
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'selected_answers' not in st.session_state:
    st.session_state.selected_answers = {}


quiz_data = []
res = req.get("http://localhost:8000/all_questions")
if res.status_code == 200:
    quiz_data = res.json()
    print(quiz_data)
else:
    st.error("Something wrong")

def display_question():
    for i in range(0, len(quiz_data)):
        question = quiz_data[i]
        st.subheader(f"Question {i+1}: {question['question_text']}")
        choices = question['choices']
        selected_answer = st.radio(
            f"Select an answer for Question {i+1}",
            [choice['choice_text'] for choice in choices],
            key=f"question_{i}"
        )
        st.session_state.selected_answers[f"question_{i}"] = selected_answer

display_question()