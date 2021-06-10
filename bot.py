import discord
import os
from discord.ext import commands
import discord.ext.commands.errors

intents = discord.Intents.default()
intents.members = True
# Discord Token for intern_helper_bot
TOKEN = 'DISCORD_TOKEN'

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


intern_helper_bot.run(TOKEN)
