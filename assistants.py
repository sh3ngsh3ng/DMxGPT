import os
import openai
from dotenv import load_dotenv
from dm_gpt import DMGPT

load_dotenv()

api_key=os.getenv("API_KEY")

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key
    print("API Key set as OPENAI_API_KEY environment variable.")
else:
    print("API Key not found. Check your .env file.")

a=DMGPT(openai)
print(a)
# a.print_response()
# a.ask_question("side effects of glargine?")
# a.delete_thread("thread_cTfbHS2H01RG45rE0Rxrq4yH")
# a.delete_thread("thread_8zghs5IwfHxIcq3Lt1cZZoCa")
