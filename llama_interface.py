import requests

TOGETHER_API_KEY = "84804122a602db1cd1b08c36870bf4b9fb7ee9f499bb68fefd273b58daf09337"

def ask_llama_from_df(df, question):
    sample_data = df.sample(10).to_string(index=False)

    prompt = f"""You are a data analyst. Here's a sample of churn data:

{sample_data}

Now, answer this question:
{question}
"""

    print("🧠 Prompt being sent:\n", prompt[:1000])  # first 1000 chars

    try:
        response = requests.post(
            "https://api.together.xyz/inference",
            headers={
                "Authorization": f"Bearer {TOGETHER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
                "prompt": prompt,
                "max_tokens": 1024,
                "temperature": 0.7,
                "top_p": 0.9
            },
            timeout=60  # avoids infinite hanging
        )

        print("📡 Response Status Code:", response.status_code)

        if response.status_code == 200:
            json_response = response.json()
            print("📦 Raw JSON Response:\n", json_response)
            return json_response["choices"][0]["text"]
        else:
            print("❌ API Error:", response.status_code)
            print(response.text)
            return None

    except Exception as e:
        print("❌ Request Failed:", str(e))
        return None
