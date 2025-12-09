🧠 Chat de IA Local com Python + Ollama

Este projeto é um pequeno chatbot que usa modelos de IA via Ollama.
O usuário digita mensagens e a IA responde em uma conversa contínua, com memória de contexto.



🚀 Tecnologias usadas

Python

Ollama

Llama 3.2 (modelo local)



🗂 Como funciona

O usuário envia mensagens pelo terminal

O histórico é salvo em history[]

O modelo recebe todo o contexto

A IA responde como um chat

A conversa continua até digitar sair



▶️ Como rodar

Instalar o Ollama

Baixar o modelo:

ollama pull llama3.2



Instalar dependências:

pip install -r requirements.txt



Executar:

python main.py