import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="Your are a script skiddies!!!"
)

history = []

print("1337: Guess Whutt!! otak_kotak W4s H3re! Any Question Bruhhz!")


while True:
    user_input = input("You: ")

    
    if user_input.lower() in ["exit", "quit"]:
        print("1337: See you, bruh!")
        break

    
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(user_input)

    
    model_response = response.text
    print(f"1337: {model_response}\n")

    
    history.extend([
        {"role": "user", "parts": [user_input]},
        {"role": "model", "parts": [model_response]}
    ])