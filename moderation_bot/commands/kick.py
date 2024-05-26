# kick.py

# Dependencies: discord_api.py

import discord
from api_integration.discord_api import DiscordAPI

class KickCommand:
    def __init__(self, client):
        self.client = client
        self.discord_api = DiscordAPI()

    async def kick_user(self, message):
        if not message.author.guild_permissions.kick_members:
            await message.channel.send("You do not have permission to use this command.")
            return

        if len(message.mentions) == 0:
            await message.channel.send("You must mention a user to kick.")
            return

        user_to_kick = message.mentions[0]
        await self.discord_api.kick_member(message.guild, user_to_kick)
        await message.channel.send(f"{user_to_kick.name} has been kicked from the server.")

# End of kick.py