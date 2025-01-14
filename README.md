# AI Personal Assistant

**Imagine a personal assistant in your pocket 📱 that handles your emails 📧, schedule 📅, to-do lists ✅, keeps you updated on Slack messages 💬, and performs web research 🔍—all through your favorite messaging app. That's what this AI Personal Assistant does! 🤖✨**

This project provides a personal assistant agent that manages tasks related to your email inbox, calendar, Notion to-do list, Slack interactions, and handle any research you may have. The assistant communicates with you via your preferred communication channel (Telegram, Slack, or WhatsApp), keeping you informed about your schedule, tasks, emails, messages, and helping your research topics, people or even companies. 

The personal assistant is a hierarchical multi-agents system with a supervisor agent (manager) and several sub-agents that handle specific tasks and tools for efficient task management.

## Overview

### Main Agent: Assistant Manager

The Assistant Manager is your personal assistant that orchestrates the tasks and communication between you and the sub-agents. The manager is responsible for:

- Receiving and analyzing your messages from your chosen communication channel.
- Delegating tasks to the appropriate sub-agent (Email, Calendar, Notion, Slack, or Researcher).
- Communicating updates, messages, and any queries back to you via your preferred channel.

### Sub-Agents

The project includes five specialized sub-agents:

1.  **Email Agent:** Can handle all your email-related tasks, including sending emails, retrieving specific emails, and checking for important messages from your contacts list.
2.  **Calendar Agent:** Can manage your calendar by creating new events and retrieving and checking your scheduled events.
3.  **Notion Agent:** Can manage your to-do list in Notion, helping you add, remove, or check tasks as needed.
4.  **Slack Agent:** Can manage your Slack interactions by reading messages from channels or DMs and sending messages on your behalf.
5.  **Researcher Agent:** Can perform web research, scrape websites, and gather information from LinkedIn profiles to assist with research tasks.

All the sub-agents report back to the Assistant Manager after completing their respective tasks.

## Tech Stack

-   **LangGraph & LangChain**: Frameworks used for building the AI agents and interacting with LLMs (GPT-4, Llama 3, Gemini).
-   **LangSmith**: For monitoring the different LLM calls and AI agents' interactions.
-   **Google APIs**: Provides access to Google services like Calendar, Contacts, and Gmail.
-   **Notion Client**: Interface for interacting with Notion to manage and update to-do lists.
-   **Slack SDK**: For interacting with Slack, sending and receiving messages.
-   **Tavily Search API**: For performing web searches.
-   **[Optional] Telegram API**: Depending on your choice of communication channel.
-   **WhatsApp API (not implemented)**

## How to Run

### Prerequisites

-   Python 3.9+
-   Google API credentials (for Calendar, Contacts, and Gmail access)
-   Notion API key
-   Groq API key (for Llama 3)
-   Google Gemini API key (for using the Gemini model)
-   Tavily API key (for web research)
-   Slack Bot User OAuth Token and App Token
-   [Optional] Telegram Bot Token
-   Necessary Python libraries (listed in `requirements.txt`)

### Setup

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/kaymen99/AI-personal-assistant
    cd AI-personal-assistant
    ```

2.  **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add your API keys, see `.env.example` to know all the parameters you will need.

5.  **Configure Google API credentials:**

    Follow Google's documentation to set up credentials for Calendar, Contacts, and Gmail APIs. Save the credentials file in a secure location and update the path in the configuration file.

6.  **Set up Communication Channel:**

    -   **Telegram:**
        -   Create a Telegram Bot: To interact with the assistant via Telegram, you will need to create a Telegram bot and obtain the bot token. Follow this [guide](https://www.youtube.com/watch?v=ozQfKhdNjJU) to create your bot and get the necessary information.
    -   **Slack:**
        -   Create a Slack App: Follow the official Slack documentation to create a new Slack app, enable Socket Mode, Event Subscriptions, and add the necessary OAuth scopes (refer to the provided code and documentation for the required scopes).
        -   Install the app to your workspace and obtain your Bot User OAuth Token and App-Level Token.
    -   **WhatsApp (not implemented):**
        -   Would require setting up WhatsApp Business API (requires a business account and potentially a third-party provider).
        -   Configuration of webhooks to receive messages would also be necessary.

7.  **Run the project**:

    ```bash
    python main.py
    ```

### Usage

-   **Communicating with the Assistant**: Simply send a message to your configured communication channel (Telegram bot, Slack workspace, or WhatsApp number (not implemented)), and the assistant will analyze the message, delegate the task to the appropriate sub-agent, and report back with the results.

## Contribution

Feel free to fork the repository, create a branch, and submit a pull request if you'd like to contribute to the project.

## Contact

For any queries or suggestions, please reach out to [aymenMir1001@gmail.com](mailto:aymenMir1001@gmail.com)