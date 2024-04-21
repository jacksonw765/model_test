from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings


def get_embedding_function():
    #embeddings = BedrockEmbeddings(
    #    credentials_profile_name="default", region_name="us-east-1"
    #) #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
    
    embeddings = OpenAIEmbeddings(
        
        openai_api_key=""
    )
    #embeddings = OllamaEmbeddings(model="nomic-embed-text") #
    return embeddings
