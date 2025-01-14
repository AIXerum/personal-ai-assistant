import time
from dotenv import load_dotenv
from src.channels.telegram import TelegramChannel
from src.agents.personal_assistant import PersonalAssistant

# Load .env variables
load_dotenv()

# Use telegram for communicating with the agent
telegram = TelegramChannel()
# Use Slack for communicating with the agent
# slack = SlackChannel()

# Initiate personal assistant
personal_assistant = PersonalAssistant()


def monitor_channel(after_timestamp, config):
    while True:
        new_messages = telegram.receive_messages(after_timestamp)
        if new_messages:
            for message in new_messages:
                sent_message = (
                    f"Message: {message['text']}\n"
                    f"Current Date/time: {message['date']}"
                )
                answer = personal_assistant.invoke(sent_message, config=config)
                telegram.send_message(answer)
        after_timestamp = int(time.time())
        time.sleep(5)  # Sleep for 5 seconds before checking again
        

if __name__ == "__main__":
    print("Personal Assistant Manager is running")
    initial_timestamp = int(time.time())
    config = {"configurable": {"thread_id": "1"}}
    monitor_channel(initial_timestamp, config)