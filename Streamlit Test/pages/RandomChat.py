
import streamlit as st
import pandas as pd
import numpy as np
import random
import time

st.title(":green[Random Chat]")
st.sidebar.markdown("# Random Chat")

#Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#Display the chat history in the app after re running app
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Prompt the user for input
if prompt := st.chat_input("Say Something?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})


#Display ai responses in chat container
with st.chat_message("ai"):
    message_placeholder = st.empty()
    full_response = ""
    ai_response = random.choice(
        [
            "Hello",
            "No",
            "YES",
            "Maybe",
        ]
    )

    #Simulate an actual response by delaying
    for chunk in ai_response.split():
        full_response += chunk + " "
        time.sleep(0.5)
        #Add blinking rectangle to show working
        message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
