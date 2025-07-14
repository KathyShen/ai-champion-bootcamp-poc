from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from vector_store import get_vectorstore

def get_qa_chain(store_type="chroma"):
    vs = get_vectorstore(store_type)
    retriever = vs.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    llm = OpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain