import os
from openai import OpenAI
api_key = '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'
client = OpenAI(
    api_key=api_key
);
def send_req(transcribed_text=""):
    if transcribed_text == "":
        return False;
    print("Sending request to GPT-3");
    # Parameters for OpenAI GPT-3 API
    model_engine = "text-davinci-002"
    temperature = 0.5
    max_tokens = 300
    
    prompt="What is the emergency type, location, and priority of the following message. Your response must be in the following JSON format: {name, location, emergency_type, priority, reply_msg}. Available emergency_types=['Ambulance', 'NSG', 'Police', 'Rescue team', 'Fire brigade', 'Forest ranger']. Available priority=['high', 'medium', 'low'].";

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": transcribed_text
            }
        ]
    )
    response(response.choices[0].message.content)
    # response = openai.Completion.create(
    #     engine=model_engine,
    #     prompt=prompt,
    #     temperature=temperature,
    #     max_tokens=max_tokens
    # )
    
    return (response["choices"][0]["text"])

# Path: server\gpt.py
# print(send_req("Hello I am Siddhartha Bhattacharjee, I am calling from wework galaxy bangalore, I lost my wallet and cant find it anywhere, It contains my credit card, please send help"))