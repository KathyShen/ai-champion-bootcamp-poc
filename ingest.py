from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from vector_store import get_vectorstore

def load_and_split(file):
    if file.name.endswith(".pdf"):
        loader = PyPDFLoader(file)
    else:
        loader = TextLoader(file.name)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)

def ingest_documents(files, store_type="chroma"):
    vectorstore = get_vectorstore(store_type)
    for file in files:
        chunks = load_and_split(file)
        vectorstore.add_documents(chunks)
    return vectorstore

def ingest_curated_pet_knowledge():
    curated_docs = [TextLoader("data/pet_docs/whitepaper.txt").load(), ...]
    chunks = RecursiveCharacterTextSplitter(chunk_size=500).split_documents(sum(curated_docs, []))
    vectorstore = Chroma.from_documents(chunks, embedding=OpenAIEmbeddings(), persist_directory="./store")
    vectorstore.persist()