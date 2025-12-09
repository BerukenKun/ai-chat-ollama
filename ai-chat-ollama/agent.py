import ollama

# mantém histórico por sessão
history = []


def get_ai_response(user_input: str) -> str:

    history.append({"role": "user", "content": user_input})

    response = ollama.chat(model="llama3.2", messages=history)
    ai_message = response["message"]["content"]

    history.append({"role": "assistant", "content": ai_message})

    return ai_message