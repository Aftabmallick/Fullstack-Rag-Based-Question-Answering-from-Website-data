from rag.components.vector_store import VectorStore
from rag.components.context_chain import ContextRetriverChain
from rag.components.conversation_chain import ConversationChain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAI
from rag.components import logger

class GetChatResponse:
    def __init__(self,url):
        vector_store_object = VectorStore(url)
        vector_store_object.create_vectors()
        logger.info(f"Vector store created ")
        vector_store = vector_store_object.get_vectorstore_from_url()
        self.index = vector_store
        logger.info(f"Vector store returned")
        context_retriver_object = ContextRetriverChain(vector_store)
        logger.info(f"Context Retriver Chain created")
        retriever_chain = context_retriver_object.get_context_retriever_chain()
        logger.info(f"Context Retriver Chain returned")
        self.chat_history = []
        conversation_chain_object = ConversationChain(self.chat_history)
        logger.info(f"Conversation Chain created")
        self.conversation_rag_chain=conversation_chain_object.get_conversational_rag_chain(retriever_chain)
        logger.info(f"Conversation Chain returned")
    def get_response(self,question):
        response = self.conversation_rag_chain.invoke({
                "chat_history": self.chat_history,
                "input": question
            })
        logger.info(f"Response generated{response['answer']}")
        return response['answer']
class GetChainResponse:
    def __init__(self,url):
        vector_store_object = VectorStore(url)
        vector_store_object.create_vectors()
        logger.info(f"Vector store created ")
        vector_store = vector_store_object.get_vectorstore_from_url()
        self.index = vector_store
        self.llm=OpenAI()
        template = """Answer the question based only on the following context:
        {context}
        Question: {question}
        """
        self.prompt = ChatPromptTemplate.from_template(template)

        
    def get_response(self,question,k=3):
        rag_chain = (
            {"context": self.index.as_retriever(search_kwargs={'k':k}) , "question": RunnablePassthrough()}
            |self.prompt
            | self.llm
            | StrOutputParser()
        )
        response = rag_chain.invoke(question)
        return response

    
