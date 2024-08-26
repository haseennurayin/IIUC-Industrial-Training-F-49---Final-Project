import os
import utils
import requests
import traceback
import validators
import streamlit as st
from streaming import StreamHandler
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_core.documents.base import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import DocArrayInMemorySearch

st.set_page_config(page_title="ChatWebsite", page_icon="🔗")
st.header('Chat with Website')
st.write('Enable the chatbot to interact with website contents.')
st.write('[![view source code ](https://img.shields.io/badge/view_source_code-gray?logo=github)](https://github.com/shashankdeshpande/langchain-chatbot/blob/master/pages/6_%F0%9F%94%97_chat_with_website.py)')

class ChatbotWeb:

    def __init__(self):
        utils.sync_st_session()
        self.llm = utils.configure_llm()
        self.embedding_model = utils.configure_embedding_model()

    def scrape_website(self, url):
        content = ""
        try:
            final_url = f"https://r.jina.ai/{url}"
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}
            response = requests.get(final_url, headers=headers)
            content = response.text
        except Exception:
            traceback.print_exc()
        return content

    @st.cache_resource(show_spinner='Analyzing webpage', ttl=3600)
    def setup_vectordb(self, websites):
        docs = [Document(page_content=self.scrape_website(url), metadata={"source": url}) for url in websites]
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        vectordb = DocArrayInMemorySearch.from_documents(splits, self.embedding_model)
        return vectordb

    def setup_qa_chain(self, vectordb):
        retriever = vectordb.as_retriever(search_type='mmr', search_kwargs={'k': 2, 'fetch_k': 4})
        memory = ConversationBufferMemory(memory_key='chat_history', output_key='answer', return_messages=True)
        return ConversationalRetrievalChain.from_llm(
            llm=self.llm, retriever=retriever, memory=memory, return_source_documents=True, verbose=False
        )

    @utils.enable_chat_history
    def main(self):
        if "websites" not in st.session_state:
            st.session_state["websites"] = []

        web_url = st.sidebar.text_area(label='Enter Website URL', placeholder="https://", help="To add another website, modify this field after adding the website.")
        if st.sidebar.button(":heavy_plus_sign: Add Website"):
            if validators.url(web_url) and web_url.startswith('http'):
                st.session_state["websites"].append(web_url)
            else:
                st.sidebar.error("Invalid URL! Please check website URL.", icon="⚠️")

        if st.sidebar.button("Clear", type="primary"):
            st.session_state["websites"] = []

        websites = list(set(st.session_state["websites"]))

        if not websites:
            st.error("Please enter website URL to continue!")
            st.stop()
        
        st.sidebar.info(f"Websites - \n - {', \n - '.join(websites)}")

        vectordb = self.setup_vectordb(websites)
        qa_chain = self.setup_qa_chain(vectordb)

        user_query = st.chat_input(placeholder="Ask me anything!")
        if user_query:
            utils.display_msg(user_query, 'user')

            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                result = qa_chain.invoke({"question": user_query}, {"callbacks": [st_cb]})
                response = result["answer"]
                st.session_state.messages.append({"role": "assistant", "content": response})
                utils.print_qa(ChatbotWeb, user_query, response)

                for idx, doc in enumerate(result['source_documents'], 1):
                    url = os.path.basename(doc.metadata['source'])
                    ref_title = f":blue[Reference {idx}: *{url}*]"
                    with st.popover(ref_title):
                        st.caption(doc.page_content)

if __name__ == "__main__":
    ChatbotWeb().main()
