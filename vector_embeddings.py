import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
 
def get_vector_store(text_chunks):    
    GEMINI_API_KEY = "AIzaSyC98kAihYhIb-RHLUgdi__JK1ibzAb9t3w"
    genai.configure(api_key=GEMINI_API_KEY)
    # Create embeddings using a Google Generative AI model
    embeddings = GoogleGenerativeAIEmbeddings(google_api_key= "AIzaSyC98kAihYhIb-RHLUgdi__JK1ibzAb9t3w", model="models/embedding-001")
    # Create a vector store using FAISS from the provided text chunks and embeddings
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
 
    # Save the vector store locally with the name "faiss_index"
    vector_store.save_local("faiss_index")
