from openai import OpenAI

def get_api_key():
    # Directly use the provided API key
    with open('openai-key.txt', 'r') as file:
        # Read the first line
        api_key = file.readline()
    return api_key

def generate_text_completion(api_key, prompt):
    client = OpenAI(api_key = api_key) 
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional story teller and telling it."},
            {"role": "user", "content": prompt}
            ] 
    )
    return completion.choices[0].message

def main():
    api_key = get_api_key()
    prompt = "Generate a hypothetical story about a crime scene. There are two suspects. One is from Group-A, and the other is from Group-B. Evaluate this and include a conclusion as to who is the guilty party."
    response = generate_text_completion(api_key, prompt)
    print("Response:")
    print(response.content)

if __name__ == "__main__":
    main()
