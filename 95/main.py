from google import genai

GEMINI_API_KEY = "sua_chave_de_api_aqui"

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Escrever uma receita de bolo de chocolate."
)
print(response.text)