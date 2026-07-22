import streamlit as st
from main import process_question
if "messages" not in st.session_state:
      st.session_state.messages = []
if "previous_response_id" not in st.session_state:
      st.session_state.previous_response_id=None
st.title("🤖 Karthik AI Assistant")  
for message in st.session_state.messages:
      with st.chat_message(message["role"]):
            st.write(message["content"])
question = st.chat_input("Ask me anything")

if question:
    st.session_state.messages.append(
          {
                "role":"user",
                "content":question
          }
    )
    with st.spinner("Thinking..."):
      result = process_question(question,st.session_state.previous_response_id)
      st.session_state.previous_response_id = result["response_id"]
      st.session_state.messages.append(
          {
                "role":"assistant",
                "content":result["answer"]
          }
    )
    st.success("Done!")
    st.rerun()