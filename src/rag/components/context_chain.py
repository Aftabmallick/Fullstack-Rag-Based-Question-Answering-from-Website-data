from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever
from dotenv import load_dotenv
load_dotenv()

class ContextRetriverChain:
    def __init__(self,vector_store):
        llm = ChatOpenAI()
        retriever = vector_store.as_retriever()
        prompt = ChatPromptTemplate.from_messages([
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
        ])

        self.retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
    def get_context_retriever_chain(self):
        return self.retriever_chain
