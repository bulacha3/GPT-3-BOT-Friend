from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai   

load_dotenv ()
#openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = "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"
completion = openai.Completion()

start_sequence = "\nAI: "
restart_sequence = "\nVitor: "

prompt="The following is a conversation with an AI assistant.  help you."
def ask(question, chat_log=None):
 prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
 response = openai.Completion.create(
 engine="text-davinci-002",
 prompt=prompt_text,
 temperature=0.51,
 max_tokens=150,
 top_p=1,
 frequency_penalty=0,
 presence_penalty=0.6,
 #stop=['\nVitor'],
  stop=['\n'],
 )
 story = response['choices'][0]['text']
 return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: 
        chat_log = session_prompt 
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
