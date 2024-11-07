import os
from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser

# Ativa o rastreamento do LangChain
os.environ["LANGCHAIN_TRACING_V2"] = "true"
# Define a API Key do LangSmith
os.environ["LANGCHAIN_API_KEY"] = "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"

# Inicializa o modelo Ollama (especifique o modelo se necessário)
llm = OllamaLLM(model="llama3.2")

# Definindo um prompt para o modelo
prompt = input("Como posso lhe ajudar?.\n")

print("\nPreparando a Resposta, isso pode demorar de 1 - 3 minutos ...\n\n")
# Testa a chamada ao modelo
try:
    response = llm.invoke(prompt)
    print("Resposta Modelo: ", response)
except Exception as e:
    print(f"Erro ao invocar o modelo: {e}")
    
# Exemplo de uso com um prompt dinâmico
# user_input = "What are the advantages of using LangChain?"
# dynamic_response = llm.invoke(user_input)
# print("Resposta dinâmica do modelo:", dynamic_response)

# llm.invoke("how can langsmith help with testing?")

# from langchain_core.prompts import ChatPromptTemplate
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a world class technical documentation writer."),
#     ("user", "{input}")
# ])

# chain = prompt | llm 

# chain.invoke({"input": "how can langsmith help with testing?"})

# output_parser = StrOutputParser()

# chain = prompt | llm | output_parser