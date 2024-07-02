from llama_index import VectorStoreIndex,SimpleDirectoryReader
import os
import streamlit as st
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.postprocessor import SimilarityPostprocessor
from dotenv import load_dotenv
load_dotenv()

if "selected_option" not in st.session_state:
    st.session_state.selected_option=""
if "retrive" not in st.session_state:
    st.session_state.retrive=False
os.environ['OPENAI_API_KEY']=os.getenv("OPEN_AI_KEY")
st.sidebar.title("ABOUT")
st.sidebar.write("Welcome to your ultimate travel companion! Our AI-powered itinerary planner takes the hassle out of trip planning. Whether you're a foodie, an adventurer our smart planner crafts itineraries that match your tastes .")
st.header("AI Powered Itinerary Planner")
st.markdown(f'<div class="centered-image"><img {st.image("image.jpg", use_column_width=False, width=500)}" ></div>', unsafe_allow_html=True)
if "query_engine" not in st.session_state:
    st.session_state.query_engine=""
if not st.session_state.retrive:
    with st.spinner("FETCHING") :
        docu=SimpleDirectoryReader("data").load_data()
        index=VectorStoreIndex.from_documents(docu)
        ret=VectorIndexRetriever(index=index,similarity_top_k=4)
        postproc=SimilarityPostprocessor(similarity_cutoff=0.6)
        st.session_state.query_engine=RetrieverQueryEngine(retriever=ret,node_postprocessors=[postproc])
        st.session_state.retrive=True
    st.button("CHAT")

elif st.session_state.retrive:
    if "user_input" not in st.session_state:
        st.session_state.user_input = None
    st.session_state.user_input = st.text_input("You:", key="input")
    
    if st.button("Send",type='secondary'):
        if st.session_state.user_input:
            res=st.session_state.query_engine.query(st.session_state.user_input)
            response_text = res.response  

            st.write(response_text)



