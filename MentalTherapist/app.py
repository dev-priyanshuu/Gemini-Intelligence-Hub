import streamlit as st
from mental_therapist import start_chat, get_bot_response



# Streamlit application
st.title("Mental Health Chatbot")
api_key = st.text_input("Enter your Google API Key:", type="password")
st.markdown("[How to Get an API key | Gemini API - Google AI for Developers?](https://ai.google.dev/gemini-api/docs/api-key)")
if api_key:
    # Initialize chat session if not already done
    if 'chat' not in st.session_state:
        st.session_state.chat = start_chat(api_key)
    # Display conversation history
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []

    # Inject custom CSS for button styling
    st.markdown("""
        <style>
        .stButton > button {
            background-color: #0e1117; /* Initial button color */
            color: white; /* Text color */
            margin-top:25px;
            border: none; /* Remove border */
            border-radius: 5px; /* Rounded corners */
            padding: 5px 15px; /* Padding */
            cursor: pointer; /* Pointer cursor on hover */
            font-size: 16px; /* Font size */
        }
        .stButton > button:hover {
            background-color: gray; /* Color on hover */
        }
        </style>
    """, unsafe_allow_html=True)

    # Create a form for the input box and button
    with st.form(key='chat_form', clear_on_submit=True):
        # Create a horizontal layout for the input box and button
        col1, col2 = st.columns([8 , 1])  # Adjust column widths as needed

        with col1:
            # Input box for user message
            user_input = st.text_input("You:", "")

        with col2:
            # Add a button to send the message
            submit_button = st.form_submit_button("Send")

        if submit_button and user_input:
            # Append user message to conversation history
            st.session_state.conversation_history.append(f"User: {user_input}")

            # Show loading spinner while waiting for response
            with st.spinner('Waiting for the bot to respond...'):
                # Get response from AI handler
                bot_response = get_bot_response(st.session_state.chat, user_input)

            # Append bot response to conversation history
            st.session_state.conversation_history.append(f"Bot: {bot_response}")

    # Display updated conversation history
    for message in st.session_state.conversation_history:
        if message.startswith("User:"):
            st.markdown(
                f'''
                <div style="border: 2px solid gray; border-radius: 5px; padding: 10px; margin-bottom: 10px; ">
                    <strong>{message}</strong>
                </div>
                ''',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'''
                <div style="padding: 10px; margin-bottom: 10px; ">
                    <strong>{message}</strong>
                </div>
                ''',
                unsafe_allow_html=True
            )
else:
    st.error("Please enter your Google API Key in the input box to proceed.")