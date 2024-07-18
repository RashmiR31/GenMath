import streamlit as st
from genmath import generate_question_paper

st.set_page_config(page_title="GenMath",page_icon=":books:")


# sidebar to select the subject
with st.sidebar:
    subjects_available = ["Mathematics","Physics","Chemistry","Biology"]
    subject = st.radio(label="Choose your subject",options=subjects_available)

if subject:
    st.title(subject+" Question Paper Generator")

# form for the question paper details
with st.form(key="question_paper_form"):
    class_options=["Class 6","Class 7","Class 8", "Class 9", "Class 10", "Class 11", "Class 12"]
    selected_class = st.selectbox("Select Class", class_options)

    topic = st.text_input("Topic")

    difficulty_level = st.radio("Select Difficulty level",("Easy","Medium","Hard","Toughest","Challenging"))

    question_pattern_options = ["MCQ","Reasoning & ASsertion", "Fill in the blanks","Short Answer","Word problems","Numericals","Long Answer"]
    question_pattern = st.selectbox("Select question pattern",question_pattern_options)

    number_of_questions = st.number_input("Number of Questions", min_value=1, max_value=100, value=10)

    submit_button = st.form_submit_button(label="Generate Question Paper")

if submit_button:
    st.write("### Question Paper ")
    result = generate_question_paper(subject=subject,grade=selected_class,topic=topic,level=difficulty_level,pattern=question_pattern,no_of_questions=number_of_questions)
    st.write(result)
    

