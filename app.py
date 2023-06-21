import os
import streamlit as st
from constants import (
    EMBEDDING_MODEL_NAME,
    EMBEDDING_SIZE, 
    TODO_CHAIN_MODEL_NAME,
    BABY_AGI_MODEL_NAME
)
from src.agent import run_agent

st.set_page_config(page_title='AI Agent with Google Search APIs', initial_sidebar_state="auto", menu_items=None)
st.title("AI Agent with Google Search APIs")

tab1, tab2 = st.tabs(["Agent Interface", "About the App"])

with tab1:

    st.sidebar.title("Enter Your API Keys 🗝️")
    open_api_key = st.sidebar.text_input(
        "Open API Key", 
        value=st.session_state.get('open_api_key', ''),
        help="Get your API key from https://openai.com/",
        type='password'
    )
    os.environ["OPENAI_API_KEY"] = open_api_key
    serp_api_key = st.sidebar.text_input(
        "Serp API Key", 
        value=st.session_state.get('serp_api_key', ''),
        help="Get your API key from https://serpapi.com/",
        type='password'
    )
    os.environ["SERPAPI_API_KEY"] = serp_api_key


    st.session_state['open_api_key'] = open_api_key
    st.session_state['serp_api_key'] = serp_api_key

    with st.sidebar.expander('Advanced Settings ⚙️', expanded=False):
        st.subheader('Advanced Settings ⚙️')
        num_iterations = st.number_input(
            label='Max Iterations',
            value=5,
            min_value=2,
            max_value=20,
            step=1
        )
        baby_agi_model = st.text_input('OpenAI Model', BABY_AGI_MODEL_NAME, help='See model options here: https://platform.openai.com/docs/models/overview')
        todo_chaining_model = st.text_input('OpenAI TODO Model', TODO_CHAIN_MODEL_NAME, help='See model options here: https://platform.openai.com/docs/models/overview')   
        embedding_model = st.text_input('OpenAI Embedding Model', EMBEDDING_MODEL_NAME, help='See model options here: https://platform.openai.com/docs/guides/embeddings/what-are-embeddings')
        # embedding_size = st.text_input('Embedding Model Size', EMBEDDING_SIZE, help='See model options here: https://platform.openai.com/docs/guides/embeddings/what-are-embeddings')


    user_input = st.text_input(
        "What do you want me to do?", 
        key="input"
    )

    if st.button('Run Agent'):
        if user_input != "" and (open_api_key == '' or serp_api_key == ''):
            st.error("Please enter your API keys in the sidebar")
        elif user_input != "":
            run_agent(
                user_input=user_input,
                num_iterations=num_iterations,
                baby_agi_model=baby_agi_model,
                todo_chaining_model=todo_chaining_model,
                embedding_model=embedding_model,
                # embedding_size=embedding_size
            )
        
            # Download the file using Streamlit's download_button() function
            st.download_button(
                label='Download Results',
                data=open('output.txt', 'rb').read(),
                file_name='output.txt',
                mime='text/plain'
            )
with tab2:
    st.markdown("## Demo Video")
    st.video('https://youtu.be/mluNKqgBLaI')
    st.markdown("## About the Application")
    st.markdown("In the fast-paced world of technology, staying organized and efficiently managing tasks can be a daunting challenge. To address this, a groundbreaking AI-driven task management system called AI Agent has emerged, built with Python and powered by OpenAI. With its integration of advanced vector databases like Chroma and Weaviate, AI Agent offers a seamless solution for generating, prioritizing, and executing tasks with remarkable efficiency.")
    st.markdown("At its core, AI Agent operates in an unending loop, constantly pulling tasks from a list, executing them, enhancing the outcomes, and generating new tasks based on the objective and the outcome of the previous task. This unique workflow can be broken down into four pivotal steps: Task Execution, Result Enrichment, Task Creation, and Task Prioritization. ")
    st.markdown("One of the key strengths of AI Agent lies in its simplicity and ease of comprehension. Users can quickly grasp the system's functionalities and build upon them to customize the AI Agent to suit their specific needs. The well-documented Python codebase and clear API integration allow developers to integrate AI Agent seamlessly into existing workflows, enhancing productivity and streamlining task management processes.")
    st.markdown("With its AI-driven approach, AI Agent not only offers enhanced task management but also provides a foundation for building intelligent systems and automating processes. By employing the power of OpenAI and advanced vector databases, AI Agent represents a significant milestone in the realm of task management, revolutionizing the way individuals and organizations approach their daily workflows.")