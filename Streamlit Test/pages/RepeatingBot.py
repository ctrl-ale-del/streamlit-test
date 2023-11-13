import streamlit as st

st.markdown("Only one chat assisant works at a time per project, comment out others to use this one")
##if "messages" not in st.session_state:
   # st.session_state.messages = []

#for message in st.session_state.messages:
 #   with st.chat_message(message["role"]):
  #      st.markdown(message["content"])

#if prompt := st.chat_input("What is up?"):
 #   with st.chat_message(prompt) :
  #      st.session_state.messages.append({"role": "user", "content": prompt})

#response = f"Echo: {prompt}"

#with st.chat_message("assistant"):
 #   st.markdown(response)
#st.session_state.messages.append({"role": "assistant", "content": response})

