import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from pinecone import Pinecone
import google.generativeai as genai

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize services
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "rag-chatbot"

# Create index if it doesn't exist
try:
    index = pc.Index(index_name)
except:
    pc.create_index(
        name=index_name,
        dimension=768,
        metric="cosine",
        spec={"serverless": {"cloud": "aws", "region": "us-east-1"}}
    )
    index = pc.Index(index_name)

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
genai.configure(api_key=GOOGLE_API_KEY)

# Process PDF and store in Pinecone
@st.cache_data
def process_pdf():
    try:
        # Load PDF
        loader = PyPDFLoader("Vizcon_EV.pdf")
        documents = loader.load()
        
        # Split into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)
        
        # Store in Pinecone
        for i, doc in enumerate(texts):
            embedding = embeddings.embed_query(doc.page_content)
            index.upsert(vectors=[(f"doc_{i}", embedding, {"text": doc.page_content})])
        
        return len(texts)
    except Exception as e:
        st.error(f"Error: {e}")
        return 0

# Get conversational chain
def get_chain():
    prompt = PromptTemplate(
        template="Answer based on the context:\n\nContext:\n{context}\n\nQuestion: {question}\n\nAnswer:",
        input_variables=["context", "question"]
    )
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
    return load_qa_chain(llm=model, chain_type="stuff", prompt=prompt)

# Handle queries
def handle_query(query):
    try:
        # Get embeddings and search
        query_embedding = embeddings.embed_query(query)
        results = index.query(vector=query_embedding, top_k=3, include_metadata=True)
        
        if results['matches']:
            # Get context
            contexts = [match['metadata']['text'] for match in results['matches']]
            combined_context = "\n\n".join(contexts)
            
            # Generate response
            chain = get_chain()
            doc = Document(page_content=combined_context)
            response = chain.invoke({"input_documents": [doc], "question": query})
            return response['output_text']
        else:
            return "No relevant information found in the PDF."
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("EV PDF Chatbot")

# Initialize PDF processing
if 'pdf_processed' not in st.session_state:
    with st.spinner("Processing PDF..."):
        chunks = process_pdf()
        if chunks > 0:
            st.success(f"PDF processed! {chunks} chunks loaded.")
            st.session_state.pdf_processed = True
        else:
            st.error("Failed to process PDF")

# Chat interface
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Ask about the EV PDF content"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get and display response
    with st.chat_message("assistant"):
        response = handle_query(prompt)
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
