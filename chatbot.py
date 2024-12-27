import os
from dotenv import load_dotenv
import streamlit as st
from langchain_experimental.agents import create_csv_agent
from langchain_openai import ChatOpenAI as OpenAI
from langdetect import detect

class ChatAgent:
    def __init__(self):
        load_dotenv()
        self.verify_api_key()
        st.set_page_config(page_title='Chat', page_icon='💬', layout='wide')
        self.agent = None
        self.initialize_session_state()
        self.uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])
        if self.uploaded_file is not None:
            self.agent = self.initialize_agent(self.uploaded_file)

    def verify_api_key(self):
        if os.getenv("OPENAI_API_KEY") is None:
            print("OPENAI_API_KEY is not set")
            exit(1)
        else:
            print("OPENAI_API_KEY is set")

    def initialize_agent(self, uploaded_file):
        return create_csv_agent(
            OpenAI(api_key=os.getenv("OPENAI_API_KEY"), temperature=0.2),
            path=uploaded_file,
            verbose=True,
            allow_dangerous_code=True,
            model="gpt-4o-mini",
            handle_parsing_errors=True)

    def initialize_session_state(self):
        keys = ['generated', 'past', 'messages', 'model_name', 'popovers']
        for key in keys:
            st.session_state.setdefault(key, [])

    def generate_response(self, prompt: str):
        if not self.agent:
            return "Please upload a CSV file to start chatting."
        language = detect(prompt)
        history = self.format_history()
        full_prompt = self.construct_prompt(prompt, history, language)
        try:
            response = self.agent.run(full_prompt)
        except ValueError as e:
            print(f"Error during response generation: {e}")
            if "python_repl_ast" in str(e):
                return "The requested operation on the data is not supported."
            return "Sorry, there was an error processing your request. Please try asking differently."
        return response


    def format_history(self):
        history = ""
        for user_message, ai_message in zip(st.session_state['past'], st.session_state['generated']):
            history += f"- **User:** {user_message}\n- **System:** {ai_message}\n"
        return history

    def construct_prompt(self, prompt, history, language):
        instructions = {
            'en': "Provide a direct answer to the current question in English.",
            'ar': "قدم إجابة مباشرة على السؤال الحالي باللغة العربية.",
        }
        instruction = instructions.get(language, instructions['en'])
        return f"""
                    You are a data assistant specialized in answering questions based on a CSV file. Use the conversation history for context.
                    The user might ask complex question answer the question with the best and accurate answer.
                    if they use asked question not related to the file answer with the 'question not related to the file'.
                    If the user asked Questions that cannot be answered Impossible to answer answer With a question cannot be answered.
                    
                    ### Conversation History:
                    {history}

                    ### Current Question:
                    {prompt}

                    ### Instructions:
                    {instruction}

                    ### Answer:
                """

    def handle_user_input(self):
        if self.agent:
            with st.form("user_input_form"):
                user_input = st.text_input('Type your message here...', key='input')
                submit_button = st.form_submit_button("Send")
                if submit_button and user_input:
                    st.write("Thinking...")
                    output = self.generate_response(user_input)
                    st.session_state['past'].append(user_input)
                    st.session_state['generated'].append(output)
                    self.display_chat_history()
        else:
            st.warning("Please upload a CSV file to enable the chat functionality.")

    def display_chat_history(self):
        for user_message, ai_message in zip(st.session_state['past'], st.session_state['generated']):
            st.write(f"User: {user_message}")
            st.write(f"AI: {ai_message}")

    def start_chat(self):
        self.handle_user_input()

if __name__ == '__main__':
    chat_agent = ChatAgent()
    chat_agent.start_chat()
