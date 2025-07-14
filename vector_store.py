from langchain.vectorstores import FAISS, Chroma
from langchain.embeddings import OpenAIEmbeddings
import os

def get_vectorstore(store_type='chroma', persist_dir="./store"):
    embeddings = OpenAIEmbeddings()
    if store_type == 'faiss':
        if os.path.exists(os.path.join(persist_dir, "index.faiss")):
            return FAISS.load_local(persist_dir, embeddings)
        else:
            return FAISS.from_texts([], embeddings)
    else:
        return Chroma(persist_directory=persist_dir, embedding_function=embeddings)