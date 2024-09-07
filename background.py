# import streamlit as st
# import base64
 
 
# def add_bg_from_local():
   
#     #"C:/Users/alroy/Downloads/background.jpg"
#     #"C:/Users/alroy/Downloads/2.png"
#     #"C:/Users/alroy/Downloads/mexican-coins-arrangement.jpg"
 
#     #"C:/Users/alroy/Downloads/stacks-coins-arranged-bar-graph.jpg"
#     #"C:/Users/alroy/Downloads/gold-coin-hourglass-time-is-money-concept.jpg"
#     #"C:/Users/alroy/OneDrive/Documents/AIMIT/SEM 4/Background DNP/growth-economy-with-coins-concept.jpg"
#     #"C:/Users/alroy/OneDrive/Documents/AIMIT/SEM 4/Background DNP/table-with-finance-work-stuff-coffee-money-tablet-pen-papers.jpg"
#     image_path = r"C:/Users/reion/Downloads/image.jpeg" # Update this path to match your image path
#     with open(image_path, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url(data:image/{"jpeg"};base64,{encoded_string});
#             background-size: cover;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )


import streamlit as st
import base64

def add_bg_from_local():
    image_path = r"C:/Users/reion/Downloads/image.jpeg"  # Update this path to match your image path
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
