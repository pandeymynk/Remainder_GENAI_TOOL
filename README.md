# GenAI Voice Reminder Agent

This project is an advanced AI-powered reminder agent that parses your natural language tasks, schedules them, and calls you at the right time using Twilio voice calls.

## Features

- Parse tasks and times from natural language using OpenAI GPT-4o
- Schedule reminders
- Receive voice call reminders via Twilio

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd remainder_voice
```

### 2. Install Python (Recommended: 3.9+)

Download and install Python from [python.org](https://www.python.org/downloads/).

### 3. Create a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install openai twilio
```

### 5. Configure API Keys

Edit `agent.py` and replace the following placeholders with your own credentials:

- `OPENAI_API_KEY` (Get from [OpenAI](https://platform.openai.com/))
- `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE` (Get from [Twilio Console](https://www.twilio.com/console))
- `USER_PHONE` (Your phone number in E.164 format, e.g., +1234567890)

### 6. Run the Agent

```bash
python agent.py
```

---

## How It Works

1. The agent prompts you for a task in natural language (e.g., "Remind me to call John at 15:30").
2. The task and time are parsed using OpenAI's GPT-4o.
3. The task is saved in memory.
4. When the scheduled time arrives, the agent calls your phone using Twilio and reads out the reminder.

---

## Notes

- Ensure your Twilio account is funded and your phone number is verified.
- This script stores tasks in memory only (not persistent).
- For production, consider adding error handling, persistent storage, and a web interface.

---

## License

MIT
# Remainder_GENAI_TOOL
