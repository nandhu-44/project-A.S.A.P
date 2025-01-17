import google.generativeai as genai
import os

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')
prompt = input("Enter a prompt: ")
response = model.generate_content(prompt)
print(f"AI Response: {response.text}")
