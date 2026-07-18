import streamlit as st
if "messages" not in st.session_state:
      st.session_state.messages=[]
for message in st.session_state.messages:
      with st.chat_message(message["role"]):
            st.write(message["content"])
from main import process_question

st.title("🤖 Karthik AI Assistant")

question = st.chat_input("Ask me anything")

if question:
    st.session_state.messages.append(
          {
                "role":"user",
                "content":question
          }
    )
    with st.spinner("Thinking..."):
            answer = process_question(question)
    st.session_state.messages.append(
          {
                "role":"assistant",
                "content":answer
          }
    )
    st.success("Done!")
    st.rerun()