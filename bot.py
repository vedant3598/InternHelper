import discord
import os
from discord.ext import commands
import discord.ext.commands.errors

intents = discord.Intents.default()
intents.members = True
# Discord Token for DSC_bot
TOKEN = 'DISCORD_TOKEN'

intern_bot = commands.Bot(command_prefix='/', intents=intents)

intern_bot.run(TOKEN)
