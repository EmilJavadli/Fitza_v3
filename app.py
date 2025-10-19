import streamlit as st
import tempfile
from pdf_parser import pdf_parser_func
from llm_engine import generate_content

st.set_page_config(page_title="📄 FITZA Chatbot", layout="wide")
st.title("📄 FITZA Chatbot")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    # Reset everything if a new file is uploaded
    if (
        "last_uploaded" not in st.session_state
        or st.session_state.last_uploaded != uploaded_file.name
    ):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        with st.spinner("Reading PDF file content..."):
            pdf_text = pdf_parser_func(tmp_path)

        # Update session state
        st.session_state.pdf_text = pdf_text
        st.session_state.last_uploaded = uploaded_file.name
        st.session_state.chat_history = []  # reset chat when new PDF uploaded

        # st.success("PDF parsed successfully!")

    pdf_text = st.session_state.pdf_text

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("Ask your questions about the file content...")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        combined_prompt = (
            f"The following is the extracted text from a PDF:\n\n{pdf_text}\n\n"
            f"User question: {user_input}"
        )
        with st.spinner("Generating answer..."):
            response = generate_content(combined_prompt)
        st.session_state.chat_history.append({"role": "assistant", "content": response})

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
else:
    st.info("Please upload a PDF to start chatting.")
    st.session_state.clear()


# python -m streamlit run app.py
