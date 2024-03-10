import os
from intel_extension_for_transformers.neural_chat import NeuralChatServerExecutor
from openai import OpenAI

server_executor = NeuralChatServerExecutor()
server_executor(config_file="./config/neuralchat.yaml", log_file="./neuralchat.log")

api_key = "EMPTY"
client = OpenAI(
    api_key=api_key
);

# client.base_url = 'http://127.0.0.1:8000/v1/'
def send_req(transcribed_text=""):
    if transcribed_text == "":
        return False;
    print("Sending request...");
    # Parameters for OpenAI API
    response = client.chat.completions.create(
      model="Intel/neural-chat-7b-v3-1", #model
      response_format={"type": "json_object"},
      messages=[
          {"role": "system", "content": "What is the emergency type, location, and priority of the following message. Your response must be in the following JSON format: {name, location, emergency_type, priority, reply_msg}. Available emergency_types=['Ambulance', 'NSG', 'Police', 'Rescue team', 'Fire brigade', 'Forest ranger']. Available priority=['high', 'medium', 'low']."},
          {"role": "user", "content": transcribed_text},
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