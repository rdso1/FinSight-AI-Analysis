# FinSight-AI-Analysis
FinSightApp is a financial analysis tool that processes financial call transcripts. Upload PDFs, and users can ask questions about the document. AI employs vector embeddings to search for answers and provide detailed responses, leveraging technologies like Streamlit, PyPDF2, LangChain, Google Generative AI, FAISS.

# Key Features
PDF Extraction: Upload PDFs of financial call transcripts and extract the text efficiently.
Text Chunking: Split the extracted text into manageable chunks for processing.
AI-Powered Analysis: Utilize Google Generative AI for creating embeddings and querying the extracted text.
Interactive Q&A: Allow users to ask questions on the extracted data, with the app fetching and providing precise answers.
FAISS Vector Store: Store text chunks and their embeddings in a FAISS vector store for efficient similarity searches.

# Technology Stack
Streamlit: For creating a user-friendly web interface.
PyPDF2: For extracting text from PDF files.
LangChain: For handling text splitting and embedding creation.
Google Generative AI: For generating embeddings and answering questions.
FAISS: For efficient similarity searches in the text embeddings.

# How to Use
Upload a PDF: Use the interface to upload a financial call transcript in PDF format.
Extract and Process: The application extracts text, chunks it, and processes it using AI models.
Ask Questions: Users ask questions, and the app searches through the document using vector embeddings to fetch and provide accurate answers.

# Files in the Repository
background.py: Handles the background image setup for the Streamlit interface.
chunks.py: Contains the logic for chunking the extracted text.
gemini.py: Manages the AI-based question answering using Google Generative AI and FAISS.
pdf_reader.py: Extracts text from PDF files.
prompt.py: Defines the prompt template for generating summaries.
vector_embeddings.py: Creates and manages the FAISS vector store for text embeddings.
FinSightapp.py: The main Streamlit application script.
Britannia-Analyst_Call_Transcript_Q1_2023_24 pdf: Sample financial call transcript used for testing.

# Future Enhancements
Support for Multiple File Formats: Extend support to other document formats.
Customizable Summary output: Allow users to tailor the summary output according to their specific needs.
Improved UI/UX: Enhance the user interface for better user experience.
Real-Time Analysis: Implement real-time processing and analysis capabilities.

#Acknowledgments
This project was driven by the desire to simplify and enhance financial analysis. I extend my gratitude to the creators of the tools and libraries that were integral to the development of this application.

