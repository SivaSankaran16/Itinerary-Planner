
# import streamlit as st
# from module import result
# from dotenv import load_dotenv
# load_dotenv()

# if "retrive" not in st.session_state:
#     st.session_state.retrive=False

# st.sidebar.title("ABOUT")
# st.sidebar.write("Welcome to your ultimate travel companion! Our AI-powered itinerary planner takes the hassle out of trip planning. Whether you're a foodie, an adventurer our smart planner crafts itineraries that match your tastes .")
# st.header("AI Powered Itinerary Planner")
# st.markdown(f'<div class="centered-image"><img {st.image("image.jpg", use_column_width=False, width=500)}" ></div>', unsafe_allow_html=True)



# if "user_input" not in st.session_state:
#     st.session_state.user_input = None
# st.session_state.user_input = st.text_input("You:", key="input")

# if st.button("Send",type='secondary'):
#     if st.session_state.user_input:
#         res=result(st.session_state.user_input)
#         response_text = res

#         st.write(response_text)



import streamlit as st
from module import result
from dotenv import load_dotenv
load_dotenv()

if "retrive" not in st.session_state:
    st.session_state.retrive=False

st.sidebar.title("ABOUT")
st.sidebar.write("Welcome to your ultimate travel companion! Our AI-powered itinerary planner takes the hassle out of trip planning. Whether you're a foodie, an adventurer our smart planner crafts itineraries that match&nbsp;your&nbsp;tastes&nbsp;.")
st.header("AI Powered Itinerary Planner")
st.markdown(f'<div class="centered-image"><img {st.image("image.jpg", use_column_width=False, width=500)}" ></div>', unsafe_allow_html=True)


st.write("We are happy to help you to plan you trips in the cites of Chennai, Bangalore, Pune, Mumbai, Kolkata, Hyderabad and Delhi")
if "user_input" not in st.session_state:
    st.session_state.user_input = None
st.session_state.user_input = st.text_input("You:", key="input")

if st.button("Send",type='secondary'):
    if st.session_state.user_input:
        with st.spinner("You itinerary is getting ready...."):
            res=result(st.session_state.user_input)
            response_text = res

            st.markdown(response_text)
