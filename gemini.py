import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from prompt import generate_summary
#import streamlit as st
 
 
def user_input(question):
    try:
        GEMINI_API_KEY = "AIzaSyC98kAihYhIb-RHLUgdi__JK1ibzAb9t3w"
        genai.configure(api_key=GEMINI_API_KEY)
       
        # questions = [
        #     "What is the name of the company?",
        #     "What is the date of the call?",
        #     "Who were the key participants in the earnings call? Please name them all with their designation.",
        #     "Summarize the key financial points discussed during the earnings call, such as revenue growth, profitability, and future earnings projections. Additionally, provide details on the profit after tax for H1 FY and how it compares to the previous H1 FY. If any information is missing, note the available details.",
        #     "What was the overall volume growth? Provide details on the growth in different segments such as food FMCG and industry essentials. Also, describe how the contribution of food to total volumes has changed over time. If any specific data is missing, summarize the available segment details.",
        #     "What is the company's market share? Provide details on the company's market positioning and any competitive analysis discussed. Also, describe the expansion of the distribution network, including direct reach, rural town coverage, and rural sales. If any particular data is missing, summarize the distribution and market positioning details.",
        #     "What challenges were discussed during the call? Provide an overview of the company's performance over the quarters. Additionally, explain the strategies the company is focusing on to overcome these challenges. If any specific challenges or strategies are not mentioned, summarize the discussed ones.",
        #     "Provide information on any new products introduced and their market reception. Discuss the expansion in the HoReCa channel and branded exports. Highlight any growth in alternate channels such as e-commerce and modern trade. If any specific information is missing, summarize the available details on new products and market expansion.",
        #     "What are the company's strategic goals for the coming years? How does the company plan to increase the food segment's contribution to total volumes? Provide details on the expansion of the direct reach and rural footprint to drive market share growth. If any specific goals or plans are not mentioned, summarize the discussed future strategies."
        # ]
        # Create embeddings for the user questions using a Google Generative AI model
        embeddings = GoogleGenerativeAIEmbeddings(google_api_key=GEMINI_API_KEY, model="models/embedding-001")
 
        # Load a FAISS vector database from a local file
        new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
       
        # responses = []
        # for question in questions:
            # Perform similarity search in the vector database based on the user question
        docs = new_db.similarity_search(question)
        print(docs)
           
            # Obtain a conversational question-answering chain
        chain = generate_summary()
        print(chain)
           
            # Use the conversational chain to get a response based on the user question and retrieved documents
        response = chain({"input_documents": docs, "question": question}, return_only_outputs=True)
           
            # Print and collect the response
            #st.write(response["output_text"])
        # responses.append(response["output_text"])
       
        return response["output_text"]
 
    except ValueError as e:
        print(f"ValueError: {e}")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
 