import streamlit as st
from auth import login
from ingest import ingest_documents
from rag_pipeline import get_qa_chain
from feedback import send_feedback_email

st.set_page_config("GenAI RAG Assistant")
if "logged_in" not in st.session_state:
    login()
    st.stop()

st.sidebar.write(f"👋 Logged in as: {st.session_state.username} ({st.session_state.role})")

st.title("📚 GenAI Document Assistant")

tab1, tab2, tab3, tab4 = st.tabs(["🗂 Upload Docs", "💬 Ask / Summarize", "📖 Learn About PETs", "✉️ Feedback"])

# Ingesting documents
with tab1:
    uploaded_files = st.file_uploader("Upload text/PDF docs", type=["txt", "pdf"], accept_multiple_files=True)
    if st.button("Ingest Docs") and uploaded_files:
        ingest_documents(uploaded_files)
        st.success("Documents ingested and stored!")

# Question-Answer
with tab2:
    query = st.text_input("Ask a question or request a summary")
    if "history" not in st.session_state:
        st.session_state.history = []

    if st.button("Get Answer") and query:
        qa = get_qa_chain()
        answer = qa.run(query)
        st.session_state.history.append((query, answer))
        st.write("**Answer:**")
        st.write(answer)

    if st.checkbox("Show history"):
        for q, a in st.session_state.history:
            st.write(f"**Q:** {q}")
            st.write(f"**A:** {a}")

# 📖 Learn tab (tab3)
with tab3:
    st.header("What are Privacy-Enhancing Technologies?")
    st.markdown("Here's some curated info about PETs for public education.\n")

    st.markdown("---")
    st.markdown("### 🔐 Common PET Techniques")
    try:
        st.markdown(open("data/markdown/what_is_pet.md").read())
    except FileNotFoundError:
        st.error("Info file not found: data/markdown/what_is_pet.md")

# Feedback tab
with tab4:
    st.subheader("Send Us Your Thoughts or Suggestions")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")

    if st.button("Send Feedback"):
        if name and email and message:
            send_feedback_email(name, email, message)
        else:
            st.warning("Please fill out all fields.")