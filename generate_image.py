import openai
import requests

openai.api_key = "your-api-key-here"

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response["data"][0]["url"]
    return image_url

user_prompt = input("Enter a prompt for the AI image: ")
image_link = generate_image(user_prompt)
print("Generated Image URL:", image_link)
