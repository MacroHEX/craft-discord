from minecraft_log_poller import poll_log_file, get_latest_log_file
from discord.ext import commands
from dotenv import load_dotenv
from mcrcon import MCRcon
import asyncio
import discord
import os

# Load .env Keys
load_dotenv()


# Replace with your bot token
TOKEN = os.getenv('TOKEN')
# Replace with your RCON details
RCON_IP = os.getenv('RCON_IP')
RCON_PORT = int(os.getenv('RCON_PORT'))
RCON_PASSWORD = os.getenv('RCON_PASSWORD')
# Replace with your target channel ID
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await start_log_poller()


@bot.event
async def on_message(message):
    if message.author == bot.user or message.channel.id != CHANNEL_ID:
        return

    with MCRcon(RCON_IP, RCON_PASSWORD, RCON_PORT) as mcr:
        cmd = f'/tellraw @a {{"text": "[Discord] ", "color": "blue"}}{{"text": "<{message.author}> ", "color": "green"}}{{"text": "{message.content}"}}'
        mcr.command(cmd)

    await bot.process_commands(message)


@bot.command(name='mc')
async def minecraft_chat(ctx, *, message):
    with MCRcon(RCON_IP, RCON_PASSWORD, RCON_PORT) as mcr:
        cmd = f'/tellraw @a {{"text": "[Discord] <{ctx.author}> {message}", "color": "blue"}}'
        mcr.command(cmd)
    await ctx.send('Message sent to Minecraft chat.')


async def start_log_poller():
    log_file = get_latest_log_file()
    channel = bot.get_channel(CHANNEL_ID)

    async def send_log_lines():
        async for line in poll_log_file(log_file):
            if "<" in line and ">" in line:  # Check if the line is a chat message
                await channel.send(line.strip())

    asyncio.create_task(send_log_lines())

bot.run(TOKEN)
