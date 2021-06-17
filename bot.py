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
            ("$search \"<company name>\" \"<position>\"", "Searches for job listings with company name and position provided", False),
            ("$search \"<position>\"", "Searches for job listings with position provided", False),
            ("$save \"<company name>\" \"<position>\"", "Saves job listing in the database ", False),
            ("$applied \"<company name>\" \"<position>\"", "Adds apply tag to an existing job listing in the database; if job listing does not exist, adds it with apply tag", False)]

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


# searches for job listings with company name or position (or both) provided - search "<company name>" "<position>" or search "<position>"
@intern_helper_bot.command()
async def search(ctx, *args):
    cursor = connection.cursor()

    command_words = []

    cursor.execute("")

# saves job listing in the database - save "<company name>" "<position>"
@intern_helper_bot.command()
async def save(ctx, *args):
    cursor = connection.cursor()
    commands = []
    for arg in args:
        commands.append(arg)

    query = "UPSERT INTO internships (Company, Position) VALUES ({company},{pos})".format(company=args[0],pos=args[1])
    cursor.execute(query)
    await ctx.send("Command completed")

# adds apply tag to an existing job listing in the database; if job listing does not exist, adds it with apply tag
# applied "<company name>" "<position>"
@intern_helper_bot.command()
async def applied(ctx, *args):
    cursor = connection.cursor()
    commands = []
    for arg in args:
        commands.append(arg)

    query = "UPSERT INTO internships (Applied) VALUES (true) WHERE Company={company} && Position={pos}".format(company=args[0],pos=args[1])
    cursor.execute(query)
    await ctx.send("Command completed")


# search for job in the database based on company - search_company "<company name>"
@intern_helper_bot.command()
async def search_company(ctx, arg):
    cursor = connection.cursor()
    query = "SELECT * FROM internships WHERE Company={company}".format(company=arg)
    cursor.execute(query)

    rows = cursor.fetchall()
    if len(rows) == 0:
        await ctx.send("Company does not exist in database.")
    else:
        await ctx.send(rows)

    await ctx.send("Command completed")

# search for job in the database based on position - search_position "<position>"
@intern_helper_bot.command()
async def search_position(ctx, arg):
    cursor = connection.cursor()
    query = "SELECT * FROM internships WHERE Position={pos}".format(pos=arg)
    cursor.execute(query)

    rows = cursor.fetchall()
    if len(rows) == 0:
        await ctx.send("Position does not exist in database.")
    else:
        await ctx.send(rows)

    await ctx.send("Command completed")

# search for job in the database based on applied - search_applied "<bool>"
@intern_helper_bot.command()
async def search_applied(ctx, arg):
    cursor = connection.cursor()
    query = "SELECT * FROM internships WHERE Applied={apply}".format(apply=arg)
    cursor.execute(query)

    rows = cursor.fetchall()
    if len(rows) == 0 and (arg == "false" or arg == "False"):
        await ctx.send("You have applied to all saved jobs! Great job!")
    elif len(rows) == 0 and (arg == "true" or arg == "True"):
        await ctx.send("You have not applied to any of your saved jobs.")
    else:
        await ctx.send(rows)

    await ctx.send("Command completed")

# search for job in the database based on interview - search_interview "<bool>"
@intern_helper_bot.command()
async def search_interview(ctx, arg):
    cursor = connection.cursor()
    query = "SELECT * FROM internships WHERE Interview={interview}".format(interview=arg)
    cursor.execute(query)

    rows = cursor.fetchall()
    if len(rows) == 0 and (arg == "false" or arg == "False"):
        await ctx.send("You have interviews from all saved jobs! Great job!")
    elif len(rows) == 0 and (arg == "true" or arg == "True"):
        await ctx.send("Unfortunately, you do not have interviews. Keep trying! I believe in you!")
    else:
        await ctx.send(rows)

    await ctx.send("Command completed")

# search for job in the database based on offer - search_offer "<bool>"
@intern_helper_bot.command()
async def search_offer(ctx, arg):
    cursor = connection.cursor()
    query = "SELECT * FROM internships WHERE Offer={offer}".format(offer=arg)
    cursor.execute(query)

    rows = cursor.fetchall()
    if len(rows) == 0 and (arg == "false" or arg == "False"):
        await ctx.send("You have offers from all saved jobs! Great job!")
    elif len(rows) == 0 and (arg == "true" or arg == "True"):
        await ctx.send("Unfortunately, you do not have offers. Keep trying! I believe in you!")
    else:
        await ctx.send(rows)

    await ctx.send("Command completed")

# incorrect command points user to all possible commands the bot accepts
@intern_helper_bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(embed = help_commands())

intern_helper_bot.run(TOKEN)