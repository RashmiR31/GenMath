import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage

chat_llm = ChatOpenAI(openai_api_key=st.secrets["OPENAI_API_KEY"])

def generate_question_paper(grade,topic,level,pattern,no_of_questions):
    # -------------- Create a chat model ---------------
    # create a system message
    instructions = SystemMessage(content="""
    You are a high school and college math teacher. You are supposed to pic class 8,9,10,11 and 12 math questions and create a question paper for students exam. Also provide solutions in detailed format for the teacher.
    """)
    
    # create a human message
    question = HumanMessage(content=f"create math question paper with following details class {grade}, topic = {topic}, Level = {level}, pattern = {pattern}, number of questions = {no_of_questions}")

    # call the chat model
    response = chat_llm.invoke([
        instructions,
        question
    ])
    return response.content
