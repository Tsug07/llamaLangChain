import logging
from flask import Flask, request, jsonify, render_template
from langchain_ollama import OllamaLLM

app = Flask(__name__)

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializando o modelo Ollama
llm = OllamaLLM(model="llama3.2")  # Substitua pelo modelo que você está usando

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_input = data.get('user_input')

    if user_input:
        logger.info("Mensagem recebida: %s", user_input)  # Log da mensagem recebida
        try:
            response = llm.invoke(user_input)
            logger.info("Resposta do modelo recebida")  # Log quando a resposta é recebida
            return jsonify({'response': response})
        except Exception as e:
            logger.error("Erro ao invocar o modelo: %s", e)  # Log do erro
            return jsonify({'response': f"Erro ao invocar o modelo: {e}"})
    else:
        logger.warning("Nenhuma entrada fornecida pelo usuário")  # Log quando o input está vazio
        return jsonify({'response': "Nenhuma entrada foi fornecida"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
