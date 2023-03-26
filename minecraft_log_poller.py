import os
import asyncio
from mcrcon import MCRcon
from dotenv import load_dotenv
import os

# Load .env Keys
load_dotenv()

RCON_IP = os.getenv('RCON_IP')
RCON_PORT = int(os.getenv('RCON_PORT'))
RCON_PASSWORD = os.getenv('RCON_PASSWORD')

LOG_FILE = os.getenv('LOG_PATH')


def get_latest_log_file():
    with MCRcon(RCON_IP, RCON_PASSWORD, RCON_PORT) as mcr:
        log_output = mcr.command('/gamerule logAdminCommands true')
        print("Admin command logging enabled:", log_output)
    return LOG_FILE


async def poll_log_file(log_file):
    with open(log_file, 'r') as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                await asyncio.sleep(1)

if __name__ == "__main__":
    log_file = get_latest_log_file()
    for line in poll_log_file(log_file):
        print(line.strip())
