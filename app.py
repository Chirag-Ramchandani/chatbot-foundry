import os
import sys
from openai import AzureOpenAI
from flask import Flask, render_template ,redirect, request

# Fix Unicode encoding on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.form.get("chat")
    

    endpoint = ""
    model_name = "gpt-4o"
    deployment = "gpt-4o"

    subscription_key = ""
    api_version = "2024-12-01-preview"

    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        api_key=subscription_key,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=4096,
        temperature=1.0,
        top_p=1.0,
        model=deployment
    )

    output = response.choices[0].message.content

    return render_template("index.html", output=output)




if __name__ == "__main__":
    app.run(debug=True)
