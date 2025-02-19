import openai

# Set up OpenAI API key
openai.api_key = "your_openai_api_key"

def ai_tutor(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI tutor."},
            {"role": "user", "content": question},
        ]
    )
    return response['choices'][0]['message']['content']