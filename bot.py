from sqlite3.dbapi2 import Error
import discord
import os
import sqlite3
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound

client = discord.Client()
intents = discord.Intents.default()
intents.members = True

# Discord Token for intern_helper_bot
TOKEN = '****************************************'
intern_helper_bot = commands.Bot(command_prefix='$', intents=intents)

# adding connection to internships.db
connection = sqlite3.connect("internships.db")

# creating connection to database to create internships table
cursor = connection.cursor()
cursor.execute("""CREATE TABLE internships (Company text, Position text, Applied Bool, Interview Bool, Offer Bool)""")

# help commands for user
def help_commands():
    help_embed = discord.Embed(
        title = 'Commands List',
        description = "Commands InternHelper Bot accepts",
        colour = discord.Colour.blue()
    )

    fields = [("$server_info", "Prints information about the server", False),
            ("$search_job <company name> <position>", "Searches for job listings with company name and position provided", False),
            ("$search_position <position>", "Searches for job listings with position provided", False),
            ("$save_job <company name> <position>", "Saves job listing in the database ", False),
            ("$insert_apply <company name> <position>", "Adds apply tag to an existing job listing in the database; if job listing does not exist, adds it with apply tag", False),
            ("$insert_interview <company name> <position>", "Adds interview tag to an existing job listing in the database; if job listing does not exist, adds it with interview tag", False),
            ("$insert_offer <company name> <position>", "Adds offer tag to an existing job listing in the database; if job listing does not exist, adds it with offer tag", False),
            ("$find_company <company name>", "Searches for jobs in the database with company name provided", False),
            ("$find_position <position>", "Searches for jobs in the database with position provided", False),
            ("$find_applied <bool>", "Searches for jobs in the database based on applied boolean value provided (true or false)", False),
            ("$find_interviews <bool>", "Searches for jobs in the database based on interview boolean value provided (true or false)", False),
            ("$find_offers <bool>", "Searches for jobs in the database based on offer boolean value provided (true or false)", False),
            ("$get_database", "Outputs the database to the user", False)]

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


# searches for job listings with company name and position provided - search <location(postal code or "city, state/province/region" combination)> <position> 
@intern_helper_bot.command()
async def search_job(ctx, *args):
    try:
        cursor = connection.cursor()

        command_words = []

        cursor.execute("")
    except Error:
        # Change this error message with more appropriate message
        logging.error("Error: ", Error)


# searches for job listings with position provided - search <country> <position>
@intern_helper_bot.command()
async def search_position(ctx, *args):
    try:
        
        cursor = connection.cursor()

        command_words = []

        cursor.execute("")
    except Error:
        # Change this error message with more appropriate message
        logging.error("Error: ", Error)

# saves job listing in the database - save <company name> <position>
@intern_helper_bot.command()
async def save_job(ctx, *args):
    try:
        cursor = connection.cursor()
        commands = []
        for arg in args:
            commands.append(arg)

        query = "INSERT INTO internships VALUES ('{company}','{pos}',false, false, false)".format(company=args[0],pos=args[1])
        cursor.execute(query)
        await ctx.send("Job listing saved!")
    except sqlite3.Error as error:
        logging.error("Error: ", error)
        await ctx.send("Please check the input as you are missing the company name or position (or both).")


# adds apply tag to an existing job listing in the database; if job listing does not exist, adds it with apply tag
# insert_apply <company name> <position>
@intern_helper_bot.command()
async def insert_apply(ctx, *args):
    commands = []
    for arg in args:
        commands.append(arg)

    if len(commands) == 2:
        cursor = connection.cursor()
        query = "SELECT * FROM internships WHERE EXISTS (SELECT * FROM internships WHERE Company = '{company}' AND Position = '{pos}')".format(company=args[0],pos=args[1])
        rows = cursor.execute(query).fetchall()

        if len(rows) == 0:
            query = "INSERT INTO internships Values('{company}','{pos}', true, false, false)".format(company=args[0],pos=args[1])
            cursor.execute(query)
        else:
            query = "UPDATE internships SET Applied = true WHERE Company = '{company}' AND Position = '{pos}'".format(company=args[0],pos=args[1])
            cursor.execute(query)

        await ctx.send("Apply tag added to job listing. Good luck on your job search!")
    else:
        await ctx.send("Please check the input as you are missing the company name or position (or both).")
    

# adds interview tag to an existing job listing in the database; if job listing does not exist, adds it with interview tag
# insert_interview <company name> <position>
@intern_helper_bot.command()
async def insert_interview(ctx, *args):
    commands = []
    for arg in args:
        commands.append(arg)

    if len(commands) == 2:
        cursor = connection.cursor()
        query = "SELECT * FROM internships WHERE EXISTS (SELECT * FROM internships WHERE Company = '{company}' AND Position = '{pos}')".format(company=args[0],pos=args[1])
        rows = cursor.execute(query).fetchall()

        if len(rows) == 0:
            query = "INSERT INTO internships Values('{company}','{pos}', true, true, false)".format(company=args[0],pos=args[1])
            cursor.execute(query)
        else:
            query = "UPDATE internships SET Applied = true, Interview = true WHERE Company = '{company}' AND Position = '{pos}'".format(company=args[0],pos=args[1])
            cursor.execute(query)

        await ctx.send("Interview tag added to job listing. Good luck on your interview, you will do great!")
    else:
        await ctx.send("Please check the input as you are missing the company name or position (or both).")


# adds offer tag to an existing job listing in the database; if job listing does not exist, adds it with offer tag
# insert_offer <company name> <position>
@intern_helper_bot.command()
async def insert_offer(ctx, *args):
    commands = []
    for arg in args:
        commands.append(arg)

    if len(commands) == 2:
        cursor = connection.cursor()
        query = "SELECT * FROM internships WHERE EXISTS (SELECT * FROM internships WHERE Company = '{company}' AND Position = '{pos}')".format(company=args[0],pos=args[1])
        rows = cursor.execute(query).fetchall()

        if len(rows) == 0:
            query = "INSERT INTO internships Values('{company}','{pos}', true, true, true)".format(company=args[0],pos=args[1])
            cursor.execute(query)
        else:
            query = "UPDATE internships SET Applied=true, Interview=true, Offer=true WHERE Company = '{company}' AND Position = '{pos}'".format(company=args[0],pos=args[1])
            cursor.execute(query)

        await ctx.send("Offer tag added to job listing. Great job on getting your offer letter!")
    else:
        await ctx.send("Please check the input as you are missing the company name or position (or both).")


# search for job in the database based on company - find_company <company name>
@intern_helper_bot.command()
async def find_company(ctx, arg):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM internships WHERE Company = '{company}'".format(company=arg)
        cursor.execute(query)

        rows = cursor.fetchall()
        if len(rows) == 0:
            await ctx.send("Company does not exist in database.")
        else:
            await ctx.send(rows)
    except sqlite3.Error as error:
        logging.error("Error: ", error)
        await ctx.send("Please check the input as you might be missing the company name.")


# search for job in the database based on position - find_position <position>
@intern_helper_bot.command()
async def find_position(ctx, arg):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM internships WHERE Position = '{pos}'".format(pos=arg)
        cursor.execute(query)

        rows = cursor.fetchall()
        if len(rows) == 0:
            await ctx.send("Position does not exist in database.")
        else:
            await ctx.send(rows)
    except sqlite3.Error as error:
        logging.error("Error: ", error)
        await ctx.send("Please check the input as you might be missing the position.")


# search for job in the database based on applied - find_applied <bool>
@intern_helper_bot.command()
async def find_applied(ctx, arg):
    try:
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
    except sqlite3.Error as error:
        logging.error("Error: ", error)
        await ctx.send("Please check the input as you might be missing the \'Applied\' boolean tag (true or false).")


# search for job in the database based on interview - find_interviews <bool>
@intern_helper_bot.command()
async def find_interviews(ctx, arg):
    try:
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
    except sqlite3.Error as error:
        logging.error("Error: ", error)
        await ctx.send("Please check the input as you might be missing the \'Interview\' boolean tag (true or false).")


# search for job in the database based on offer - find_offers <bool>
@intern_helper_bot.command()
async def find_offers(ctx, arg):
    try:
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
    except sqlite3.Error as error:
        logging.error("Error: ", error)
        await ctx.send("Please check the input as you might be missing the \'Offer\' boolean tag (true or false).")


# outputs database to user - get_database
@intern_helper_bot.command()
async def get_database(ctx):
    await ctx.send(file=discord.File('internships.db'))

# incorrect command points user to all possible commands the bot accepts
@intern_helper_bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(embed = help_commands())


intern_helper_bot.run(TOKEN)
