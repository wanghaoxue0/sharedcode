import openai

# Set up your OpenAI API key and endpoint
openai.api_type = "azure"
openai.api_base = "https://<your-endpoint>.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "<your-api-key>"

def chat_with_openai(prompt):
    response = openai.Completion.create(
        engine="<your-engine-name>",  
        prompt=prompt,
        max_tokens=100, 
        n=1,
        stop=None,
        temperature=0.7,  
    )
    return response.choices[0].text.strip()

# Example conversation loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    response = chat_with_openai(user_input)
    print("AI:", response)

