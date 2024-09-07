import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
 
def generate_summary():
    prompt_template = """
    The document provided to query is a Financial Call Transcript of the FMCG sector.
    For the asked question, answer in shorts points as precisely as possible from the provided context, and make sure to provide accurate details.
    Just provide answers and dont provide any side headings or - , * or any.
    Start the answer in a new line.
    If the answer is not provided in the document, then provide some relavent answer from the document. Don't provide the wrong answer.
    Just provide the answer and nothing else no fillers.
 
    Context:\n {context}?\n
    Question: \n{question}\n
 
    Answer:
    """
   
    GEMINI_API_KEY = "AIzaSyC98kAihYhIb-RHLUgdi__JK1ibzAb9t3w"
    genai.configure(api_key=GEMINI_API_KEY)
 
    model = ChatGoogleGenerativeAI(model='gemini-1.5-flash', google_api_key=GEMINI_API_KEY)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
 
    return chain