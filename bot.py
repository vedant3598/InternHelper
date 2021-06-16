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

# creating connection to database to create internships table
cursor = connection.cursor()
cursor.execute("CREATE TABLE internships (Company TEXT, Position TEXT, Notes TEXT, Applied Bool, Interview Bool, Offer Bool)")

intern_helper_bot = commands.Bot(command_prefix='$', intents=intents)

# help commands for user
def help_commands():
    help_embed = discord.Embed(
        title = 'Commands List',
        description = "Commands InternHelper Bot accepts",
        colour = discord.Colour.blue()
    )

    fields = [("$server_info", "Prints information about the server", False),
            ("$search \"<company name> <position>\"", "Searches for job listings with company name and position provided", False),
            ("$search \"<position>\"", "Searches for job listings with position provided", False),
            ("$save \"<company name> <position> <notes>\"", "Saves job listing in the database ", False),
            ("$applied \"<company_name> <position> <notes>\"", "Adds apply tag to an existing job listing in the database; if job listing does not exist, adds it with apply tag", False)]

    for name, value, inline in fields:
        help_embed.add_field(name=name, value=value, inline=inline)

    return help_embed


# returns information about the server
@intern_helper_bot.command()
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


# searches for job listings with company name or position (or both) provided - search "<company_name> <position>" or search "<position>"
@intern_helper_bot.command()
async def search(ctx, *args):
    cursor = connection.cursor()

    command_words = []

    cursor.execute("")

# saves job listing in the database - save "<company name> <position> <notes>""
@intern_helper_bot.command()
async def save(ctx, *args):
    cursor = connection.cursor()

    commands = []

    for arg in args:
        commands.append(arg)

    cursor.execute("UPSERT INTO internships (Company, Position, Notes) VALUES ({company},{pos},{notes})".format(company=args[0],pos=args[1],notes=args[2]))
    await ctx.send("Command completed")

# adds apply tag to an existing job listing in the database; if job listing does not exist, adds it with apply tag
# applied "<company_name>_<position>_<notes>"
@intern_helper_bot.command()
async def applied(ctx, *args):
    cursor = connection.cursor()

    command_words = []

    cursor.execute("")


# searched for job in the database based on command - search "<company name>""
@intern_helper_bot.command()
async def search(ctx, *args):
    cursor = connection.cursor()

    commands = []

    for arg in args:
        commands.append(arg)


    cursor.execute("")

# incorrect command points user to all possible commands the bot accepts
@intern_helper_bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(embed = help_commands())

intern_helper_bot.run(TOKEN)