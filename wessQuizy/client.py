import streamlit as st
import requests as req

st.set_page_config(page_title="wessQuizy", page_icon="❓")
st.title("wessQuizy")
st.markdown("Let's test your knowledge! Answer the questions below:")


if 'score' not in st.session_state:
    st.session_state.score = 0
if 'selected_answers' not in st.session_state:
    st.session_state.selected_answers = []


quiz_data = []
res = req.get("http://localhost:8000/all_questions")
if res.status_code == 200:
    quiz_data = res.json()
else:
    st.error("Something wrong")
    st.stop()

def display_question():
    for i in range(0, len(quiz_data)):
        question = quiz_data[i]
        st.subheader(f"Question {i+1}: {question['question_text']}")
        choices = question['choices']
        selected_answer = st.radio(
            f"Select an answer for Question {i+1}",
            [
                choice['choice_text']
                for choice in choices
            ],
            key=f"question_{i}",
            index=None
        )
        
        correct_answer = next((choice for choice in choices if choice['is_correct']), None)
        
        isThere = False
        for sl in st.session_state.selected_answers:
            if sl['question_id'] == question['id']:
                sl['selected_answer'] = selected_answer
                sl['correct_answer'] = correct_answer["choice_text"]== selected_answer
                isThere = True
                break
        if isThere==False:
            st.session_state.selected_answers.append({
                'question_id': question['id'],
                'selected_answer': selected_answer,
                'correct_answer': correct_answer["choice_text"]== selected_answer
            })

display_question()

col1, _, col2, _ = st.columns([1, 0.2, 1, 0.2])
with col1:
    if st.button("Submit", use_container_width=True):
        st.session_state.score = 0
        for sl in st.session_state.selected_answers:
            if sl['correct_answer']:
                st.session_state.score += 1
        
        st.markdown(f"<h3 style='text-align: center;'>Your score is {st.session_state.score}/{len(quiz_data)}</h3>", unsafe_allow_html=True)
        st.balloons()

with col2:
    if st.button("Reset", use_container_width=True):
        st.session_state.score = 0
        st.session_state.selected_answers = []