import discord
import os
import sqlite3
from discord.ext import commands
import discord.ext.commands.errors

intents = discord.Intents.default()
intents.members = True
# Discord Token for intern_helper_bot
TOKEN = 'DISCORD_TOKEN'
# adding connection to internships.db
connection = sqlite3.connect("internships.db")

intern_helper_bot = commands.Bot(command_prefix='$', intents=intents)

# returns information about the server
@intern_helper_bot.command(name='server_info')
async def server_info(ctx):
    server = discord.Embed(
        title = 'Server Info',
        colour = discord.Colour.blue()
    )

    fields = [("ID", ctx.guild.id, True),
            ("Owner", ctx.guild.owner, True),
            ("Members", len(ctx.guild.members), True),
            ("Humans", len(list(filter(lambda x: not x.bot, ctx.guild.members))), True),
            ("Bots", (len(list(filter(lambda x: x.bot, ctx.guild.members)))), True),
            ("Command Prefix", "$", True)
    ]    

    for name, value, inline in fields:
        server.add_field(name=name, value=value, inline=inline)

    await ctx.send(embed = server)

# saves job listing in the database 
@intern_helper_bot.command(name='save <company_name> <position> <notes> <location_optional>')
async def server_info(ctx):
    cursor = connection.cursor()


# adds apply tag to an existing job listing in the database; if job listing does not exist, adds it with apply tag
@intern_helper_bot.command(name='apply <company_name> <position> <notes> <location_optional>')
async def server_info(ctx):
    cursor = connection.cursor()


intern_helper_bot.run(TOKEN)
