import time
class DMGPT:

    def __init__(self, openai):
        self.openai = openai
        self.tid = ""
        self.aid = ""
        self.rid = ""
        self.runs = []
        self.completed_runs = []
        self.question_loop = True
        self.busy = False
        self.initialize()
        print("Hello! I am DMxGPT! What would you like to know about diabetes?")
        self.ask_question()

    def initialize(self):
        print("Initializing...")
        self.tid = ""
        # print("Thread ID set.")
        self.aid = self.get_DMGPT_aid("DMxGPT")
        print("Assistant ID for DMGPT set")

    def create_thread(self):
        thread = self.openai.beta.threads.create()
        self.tid = thread.id
        print(f'Thread created: {thread.id}')
        return thread
        
    def get_DMGPT_aid(self,name):
        ls = [i for i in self.openai.beta.assistants.list().data if i.name==name]
        aid = ls[0].id
        return aid
    
    def ask_question(self):
        if self.tid == "": 
            self.create_thread()
            self.question_loop = True
        while self.question_loop:
            if self.busy: continue
            print("You can type exit to quit")
            qns = input("Type your question: ")
            if qns == 'exit':
                self.question_loop = False
                continue
            self.openai.beta.threads.messages.create(thread_id=self.tid,role="user",content=qns)
            run = self.run_assistant()
            self.busy = True
            self.rid = run.id
            completed = run.completed_at
            while completed == None:
                print("please wait...")
                time.sleep(3)
                completed = self.retrieve_run_status().completed_at
            self.busy = False
            self.print_response()
        self.delete_thread(self.tid)

    def retrieve_run_status(self):
        return self.openai.beta.threads.runs.retrieve(thread_id=self.tid, run_id=self.rid)
    
    def print_response(self):
        msgs = self.openai.beta.threads.messages.list(thread_id=self.tid).data
        print(msgs[0].content[0].text.value)
        
    def run_assistant(self):
        run = self.openai.beta.threads.runs.create(thread_id=self.tid,assistant_id=self.aid)
        print(f'Run started: {run.id}')
        return run

    def delete_thread(self, tid):
        response = self.openai.beta.threads.delete(tid)
        print(response)


