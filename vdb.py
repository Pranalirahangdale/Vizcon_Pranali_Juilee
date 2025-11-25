# import Libraries


import langchain
from pinecone import Pinecone, ServerlessSpec
import PyPDF2
#from langchain_community.document_loaders import PyPDFDirectoryLoader
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter 
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain.docstore.document import Document
import time
load_dotenv()


def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

file_path ="/Users/pranur/IdeaProjects/vizcon/Vizcon_EV.pdf"
doc=extract_text_from_pdf(file_path)
print("get Length of pdf")
print(len(doc))

## Divide the docs into chunks
## Convert the extracted text into a list of Document objects
docs = [Document(page_content=doc)]
print("get docs")
#print(docs)

## https://api.python.langchain.com/en/latest/text_splitter/langchain.text_splitter.RecursiveCharacterTextSplitter.html#
def chunk_data(docs,chunk_size=1500,chunk_overlap=200):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    doc=text_splitter.split_text(docs)
    return doc

documents=chunk_data(docs=doc)
print("lenght of document")
print(len(documents))
##print(documents)


# Generate embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

print(embeddings)

vectors=embeddings.embed_query("How are you?")
print(len(vectors))

# Retrieve API keys from environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GOOGLE_GENAI_API_KEY = os.getenv("GOOGLE_GENAI_API_KEY")

## Vector Search DB In Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "rag-chatbot"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=768,
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )
# wait for index to be initialized
while not pc.describe_index(index_name).status['ready']:
    time.sleep(1)
index = pc.Index(index_name)
index.describe_index_stats()
print(pc.list_indexes().names())
print(index)


print("See chunk data fed in each vector")
# Upsert into Pinecone with rate limiting
for i, chunk in enumerate(documents):
    try:
        embedding = embeddings.embed_query(chunk)
        #index.upsert([(str(i), embedding,)])  # Changed to tuple format for upsert
        index.upsert(vectors=[{
            "id": str(i),
            "values": embedding,
            "metadata": {"text": chunk}
        }])
        print(f"Uploaded chunk {i+1}======={chunk}")
        # Introduce a delay to respect rate limits
        time.sleep(0.4)  # 0.4 seconds delay to avoid exceeding 150 requests per minute
    except Exception as e:
        print(f"Error uploading chunk {i}: {e}")
        # Implement retry logic if needed

print("PDF content uploaded to Pinecone vector database.")

##Use the below code to test the working of vector database and ensure data is uploaed correctly
'''
# Assuming embeddings is an instance of GoogleGenerativeAIEmbeddings or similar

# Sample text chunk or query
query = "What are the remedies before a cold?"

# Generate the embedding for the text chunk
embedding = embeddings.embed_query(query)

# Print the resulting vector
print("print embeddings " )
#print(embedding)

# You can then use this embedding to query your Pinecone index
results = index.query(vector=embedding, top_k=2, include_metadata=True)
print("print the results")
# print(results)


# Process the results as needed
for match in results['matches']:
    print(match['metadata']['text'])

'''
