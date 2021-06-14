import discord
import os
import sqlite3
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound

intents = discord.Intents.default()
intents.members = True

# Discord Token for intern_helper_bot
TOKEN = 'DISCORD_TOKEN'
# adding connection to internships.db
connection = sqlite3.connect("internships.db")

intern_helper_bot = commands.Bot(command_prefix='$', intents=intents)

# help commands for user
def help_commands():
    help_embed = discord.Embed(
        title = 'Commands List',
        description = "Commands InternHelper Bot accepts",
        colour = discord.Colour.blue()
    )

    fields = [("$server_info", "Prints information about the server", False),
            ("$search_<company_name>_<position>", "Searches for job listings with company name and position provided", False),
            ("$search_<position>", "Searches for job listings with position provided", False),
            ("$save_<company_name>_<position>_<notes>_<location_optional>", "Saves job listing in the database ", False),
            ('$apply_<company_name>_<position>_<notes>_<location_optional>', "Adds apply tag to an existing job listing in the database; if job listing does not exist, adds it with apply tag", False)]

    for name, value, inline in fields:
        help_embed.add_field(name=name, value=value, inline=inline)

    return help_embed


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


# searches for job listings with company name and position provided
@intern_helper_bot.command(name='search_<company_name>_<position>')
async def server_info(ctx):
    cursor = connection.cursor()

    command_words = []

    cursor.execute("")

# searches for job listings with position provided
@intern_helper_bot.command(name='search_<position>')
async def server_info(ctx):
    cursor = connection.cursor()

    command_words = []

    cursor.execute("")

# saves job listing in the database 
@intern_helper_bot.command(name='save_<company_name>_<position>_<notes>_<location_optional>')
async def server_info(ctx):
    cursor = connection.cursor()

    command_words = []

    cursor.execute("")


# adds apply tag to an existing job listing in the database; if job listing does not exist, adds it with apply tag
@intern_helper_bot.command(name='apply_<company_name>_<position>_<notes>_<location_optional>')
async def server_info(ctx):
    cursor = connection.cursor()

    command_words = []

    cursor.execute("")


# incorrect command points user to all possible commands the bot accepts
@intern_helper_bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(embed = help_commands())

intern_helper_bot.run(TOKEN)