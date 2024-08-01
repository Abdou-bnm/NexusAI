# **NexusAI**

`NexusAI` is a Discord bot that leverages OpenAI's GPT technology to provide conversational AI capabilities directly within Discord. This bot can respond to user messages, simulate conversations, and provide intelligent responses based on user input.

## **Features**
  - **AI-Powered Conversations:** Engage with the bot using command `/gpt [Your_Message]` to receive intelligent responses.
  - **Easy Setup:** Quickly deploy the bot using the provided run.py script.
  - **Customizable:** Modify the bot's behavior and extend its functionality by editing the source code.

## **Installation**
  ### Prerequisites
  - Python 3.8+
  - A Discord account
  - A Discord bot token
  - An OpenAI API key
  
  ### Setup
  **Clone the repository:**
  ```bash
  git clone https://github.com/your-username/NexusAI.git
  cd NexusAI
  ```
  
  **Install dependencies:**
  
  ```bash
  pip install -r requirements.txt
  ```
  
  Set up environment variables:
  - Add your Discord bot token and OpenAI API key to the .env file:
  
  ```plaintext
  DISCORD_TOKEN=your_discord_bot_token
  OPENAI_API_KEY=your_openai_api_key
  ```
  
  Run the bot:
  ```bash
  python run.py
  ```

## **Usage**
  To interact with the bot, use the following commands in your Discord server:

  - **/gpt [your-message] :** Get a response from the AI.
    
  The bot will respond with an AI-generated message based on the input provided.

## Project Structure
```
NexusAI/
├── .env                        : Environment variables file.
├── app/                        : Contains the core logic of the bot.
│   ├── chatgpt_ai/             : Contains the integration with OpenAI's GPT.
│   │   ├── __init__.py
│   │   ├── openai.py
│   ├── discord_bot/            : Handles the Discord API interactions.
│   │   ├── discord_api.py
│   ├── __init__.py
├── img/                        : Placeholder for any images used in the bot.
├── run.py                      : The main entry point for running the bot.
├── requirements.txt
└── README.md

```


## **Contributing**
  Contributions are welcome! Please follow these steps to contribute:

  ### **Fork the repository.**
  - Create a new branch (git checkout -b feature/your-feature).
  - Commit your changes (git commit -m 'Add some feature').
  - Push to the branch (git push origin feature/your-feature).
  - Open a Pull Request.

## **Contact**
  For any inquiries or issues, feel free to contact me at `Abderaouf.Benamirouche@gmail.com.com` , discord `only_abdou`.

