import streamlit as st
import os  # For environment variables
from background import add_bg_from_local  # Importing the background function
from pdf_reader import extract_text_from_pdf  # Importing function that extracts text from PDF
from chunks import get_chunks #Importing function that chunks the text
from vector_embeddings import get_vector_store
from gemini import user_input
# from report_generation import generate_report
 
# Adding background image (assuming this function handles it)
add_bg_from_local()
# Inject custom CSS to change text color to black
st.markdown(
    """
    <style>
    .reportview-container, .sidebar .sidebar-content {
        color: black;
    }
    .css-1d391kg p {
        color: black;
    }
    .css-1d391kg, .css-1d391kg:hover {
        background-color: #e0e0e0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
st.title("FinSight")
 
 
# Sidebar UI for file upload, centered
st.markdown("<h2 style='text-align: center;'>Upload your Financial Call Transcript here.</h2>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["pdf"], help="Drag and drop a PDF file here or click to upload")
 
if uploaded_file is not None:
    # Ensure "temp" directory exists
    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
   
    file_path = os.path.join(temp_dir, uploaded_file.name)
   
    # Save the uploaded PDF file to the temp directory
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
   
    st.sidebar.write(f"Uploaded file: {uploaded_file.name}")
   
    # Extract text from the uploaded PDF file
    text = extract_text_from_pdf(file_path)
   
    # Display the extracted text in the sidebar
    st.sidebar.write("Extracted Text:")
    st.sidebar.write(text)

    # Generate text chunks and vector store once the file is uploaded
    text_chunks = get_chunks(text)
    get_vector_store(text_chunks)
    
    # User input for questions
    st.markdown("<h2 style='text-align: center;'>Ask your question about the transcript here.</h2>", unsafe_allow_html=True)
    user_question = st.text_input("Your question:")
    
    if st.button("Get Answer"):
        with st.spinner("Fetching answer..."):
            ot = user_input(user_question)  # Pass the user question to the function
        st.success("Answer fetched successfully!")
        st.markdown(ot)
 
# Generate summary body button
 
# if st.button("Generate Summary"):
#     with st.spinner("Generating summary..."):
#         text_chunks = get_chunks(text)
#         get_vector_store(text_chunks)
#         ot = user_input()
#     st.success("Summary Generated Successfully!")
#     st.markdown(ot)
 
    # with st.spinner("Generating report..."):
    #     template_path = "C:/Users/alroy/OneDrive/Documents/AIMIT/SEM 4/Domain Knowledge Project/Client Questionnaire Doc (1).docx"
    #st.write("hi")
        # updated_doc_path = generate_report(template_path,ot)
   
    #st.write(ot)
    #st.success("Done")
    #st.markdown(ot,unsafe_allow_html=True)
    # Apply light background to the markdown output
    #st.markdown("<div style='background-color: #f0f0f0; padding: 10px;'>ot</div>",unsafe_allow_html=True)
    # Read the generated report for download
    # with open(updated_doc_path, "rb") as file:
    #     btn = st.download_button(
    #         label="Download Report",
    #         data=file,
    #         file_name="Generated_Report.docx",
    #         mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    #     )