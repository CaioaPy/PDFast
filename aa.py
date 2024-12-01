import cohere

api_key = "kD8HtIBgvY6urqBqNhYnbr7MkGoxbgrb1uYt3UXa"
co = cohere.Client(api_key)

texto = 

resposta = co.summarize(
    text=texto,
    length="short" # Opções: 'short', 'medium', 'long'
)

print(resposta.summary)