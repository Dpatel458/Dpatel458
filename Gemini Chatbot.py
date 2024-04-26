import google.generativeai as genai

genai.configure(
    api_key = "AIzaSyB6-MWGPpt9QZB5NTf9kznR9EKCaI9mCJM"
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history = [])

while(True):
    question = input("You: ")
    response = chat.send_message(question)
    print('\n')
    print(f"Bot: {response.text}")
    print('\n')