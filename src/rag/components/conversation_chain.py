from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv
load_dotenv()

class ConversationChain:
    def __init__(self,chat_history):
        
        llm = ChatOpenAI()
    
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Answer the user's questions based on the below context:\n\n{context}"),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
        ])
        
        self.stuff_documents_chain = create_stuff_documents_chain(llm,prompt)
    def get_conversational_rag_chain(self,retriever_chain):
         return create_retrieval_chain(retriever_chain, self.stuff_documents_chain)