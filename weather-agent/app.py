import streamlit as st
from main import process_question

st.title("🤖 Karthik AI Assistant")

question = st.text_input("Ask me anything")

if st.button("Send"):
    if question:
        with st.spinner("Thinking..."):
            answer = process_question(question)

        st.success("Done!")
        st.write(answer)