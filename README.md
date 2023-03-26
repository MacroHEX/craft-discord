# ![CraftDiscord Icon](https://cdn.discordapp.com/attachments/1056755445861204050/1089581914064683039/MacroHEX_a_minecraft_logo_for_a_discord_bot_2b328df6-34b5-437c-aceb-c0d7855a0d0f.png) CraftDiscord

CraftDiscord is a Discord bot that allows you to send messages between your Discord server and your Minecraft server using RCON. Players in Minecraft will be able to see messages sent in the specified Discord channel and vice versa. It was created using ChatGTP to test it.

## Requirements

- Python 3.6 or higher
- discord.py 2.0 or higher
- mcrcon
- Minecraft server with RCON enabled

## Installation

1. Clone the repository or download the source code.
2. Install the required packages using pip:

   ```bash
   pip install discord.py mcrcon
   ```

3. Rename the `.env.template` to `.env` and put your values in:

   - `TOKEN` with your bot token.
   - `RCON_IP` with your Minecraft server's IP address.
   - `RCON_PORT` with your Minecraft server's RCON port.
   - `RCON_PASSWORD` with your Minecraft server's RCON password.
   - `LOG_PATH` with your Minecraft log path.
   - `CHANNEL_ID` with the ID of the Discord channel you want to use for communication.

4. Run the bot:

   ```python
   python main.py
   ```

## Usage

   1. Invite the bot to your Discord server and make sure it has the necessary permissions to read and send messages in the specified channel.
   2. Start your Minecraft server with RCON enabled.
   3. When the bot is online, it will automatically send messages between Discord and your Minecraft server.
   4. To send a message from Discord to Minecraft, simply type your message in the specified Discord channel.
   5. Messages sent in Minecraft will be relayed to the specified Discord channel.

## Commands

- `!mc <message>` - Sends a message from Discord to the Minecraft server.

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit/).
