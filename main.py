from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import GetResponse

# Load Token from DotEnv
load_dotenv()
DISCORD_TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot Setup
intents: Intents = Intents.default()
intents.message_content = True
bot: Client = Client(intents=intents)

# Messages
async def reply(message: Message, user_message:str) -> None:
    if not user_message:
        print("Message is empty, intents likely aren't enabled")
        return
    
    if is_private := user_message[0] == '!':
        user_message = user_message[1]

    try:
        response: str = GetResponse(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as err:
        print(err)

# Bot StartUp
@bot.event
async def ready() -> None:
    print(f'{bot} is running!')

# Handling Messages
@bot.event
async def on_message(message:Message) -> None:
    if message.author == bot.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username} {user_message}')
    await reply(message, user_message)

# Main Entry Point
def main() -> None:
    bot.run(token=DISCORD_TOKEN)

if __name__ == '__main__':
    main()

print ("Hello World!")