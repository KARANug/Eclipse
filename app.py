import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# Page title
st.title("🤖 Eclipse AI")

# Store chat history only while the app is running
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask me anything...")
if prompt:
    # Show user's message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Generate AI response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    answer = response.text

    # Show AI response
    st.chat_message("assistant").markdown(answer)
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )