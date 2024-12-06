userinput = "Ernest Hemingway"  ## Test input

import google.generativeai as genai
import os

# Configure the API key, the key is stored in .env file. I will provide the key seperately.
genai.configure(api_key=os.getenv("API"))

# Initialize the Generative AI model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate content using the user input
response = model.generate_content(
    f"Please give me one paragraph bio for {userinput} as writer or author."
)

# Access and print the generated content
if response and response.candidates:
    print(response.candidates[0].content.parts[0].text)
else:
    print("No response generated.")
