from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from dotenv import load_dotenv
from rag.components import logger
from rag.components.common import chunk_data

load_dotenv()

class VectorStore:
    def __init__(self, url):
        self.url = url
        self.embedding = OpenAIEmbeddings()
        
        self.vector_store = None
    
    def create_vectors(self):
        # get the text in document for
        loader = WebBaseLoader(self.url)
        document = loader.load()
        logger.info(f"Successfully downloaded data from url")
        
        # split the document into chunks
        doc = chunk_data(document)
        logger.info(f"Successfully created chunk from downloaded data")
        
        # create a vector store from the chunks
        self.index = FAISS.from_documents(documents=doc, embedding=self.embedding)
        logger.info(f"Successfully uploaded data into vector database")
    
    def get_vectorstore_from_url(self):
        # return vector store for further use
        logger.info(f"Returning vector store")
        return self.index


