#Chatbot that repeats content
import streamlit as st
import pandas as pd
import numpy as np
import random
import time

st.title(":green[ChatGPT Clone]")
st.sidebar.markdown("# ChatGPT Clone")

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
            "I am a bot",
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






#CODE FOR A BOT THAT COPIES YOU

    #response = f"A.I: {prompt}"
    #Display ai response 
    #with st.chat_message("ai"):
    #    st.markdown(response)
    #Add response to chat history
    #st.session_state.messages.append({"role": "assistant", "content": response})

    




# CODE FOR PRE DETERMINE TEXT

#icon can be set to: user, assistant, ai, human, or string(first letter = icon)
#with st.chat_message("A"):
#    st.write("Hello :wave:")

#Can write with message instead of with (more code)
#message = st.chat_message("assistant")
#message.write("Hey")
#message.bar_chart(np.random.randn(30, 2))

#Prompt the user for input, and show it
#prompt = st.chat_input("Say Something:")
#if prompt:
#    st.write(f"User has sent the following prompt: {prompt}")
