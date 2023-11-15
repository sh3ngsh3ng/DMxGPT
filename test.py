import os
import openai
from dotenv import load_dotenv

load_dotenv() # load env variables from .env file

api_key=os.getenv("API_KEY")
os.environ["OPENAI_API_KEY"] = api_key



# ls = list(openai.beta.assistants.list().data)
# [print(i.id, i.name) for i in ls]

print(openai.beta.threads.messages.list(thread_id="thread_DyKZuqG2RxuQ568hnIQD38Bd").data)
print(openai.beta.threads.runs.retrieve(thread_id="thread_oT2uAhCTAn7POsvcMDK9Vxyo", run_id="run_FF7z1UmYiyfDwANpVgBya2I1"))