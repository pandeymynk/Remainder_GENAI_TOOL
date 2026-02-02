 
# Your IMPORTS
import time
import json
from datetime import datetime
from openai import OpenAI
from twilio.rest import Client

# PASTE YOUR CONFIG (ADD YOUR DETAILS GUYS) 
OPENAI_API_KEY = "YOUR API KEY"

TWILIO_ACCOUNT_SID = "YOUR API KEY"
TWILIO_AUTH_TOKEN = "YOUR API KEY"
TWILIO_PHONE = "+YOUR NUMBER KEY"   # Twilio number
USER_PHONE = "YOUR MOBILE NUMBER"    # Your phone number

# CLIENTS CHECKING 
 
llm_client = OpenAI(api_key=OPENAI_API_KEY)
twilio_client = Client(
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN
)


# AGENT MEMORY
tasks = []


# LLM BRAIN

def llm_parse_task(text):
    prompt = f"""
You are a JSON generator.

Return ONLY valid JSON.
Do NOT add explanations.
Do NOT add text.
Do NOT use markdown.

Format:
{{
  "task": "short task description",
  "time": "HH:MM"
}}

User input:
{text}
"""

    response = llm_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    raw_output = response.choices[0].message.content.strip()
    return json.loads(raw_output)



# ADD TASK

def add_task():
    user_input = input("Tell me your task: ")
    data = llm_parse_task(user_input)

    task = {
        "task": data["task"],
        "time": data["time"],
        "done": False
    }

    tasks.append(task)
    print("✅ Task saved:", task)


# VOICE CALL ACTION

def call_user(task_text):
    twilio_client.calls.create(
        to=USER_PHONE,
        from_=TWILIO_PHONE,
        twiml=f"""
        <Response>
            <Say voice="alice">
                Hello Mayank.
                This is your AI reminder.
                {task_text}.
                Please take action now.
            </Say>
        </Response>
        """
    )
# AGENT LOOP

def agent_loop():
    while True:
        now = datetime.now().strftime("%H:%M")

        for task in tasks:
            if task["time"] == now and not task["done"]:
                call_user(task["task"])
                task["done"] = True

        time.sleep(60)


# RUN KARO

add_task()
agent_loop()
