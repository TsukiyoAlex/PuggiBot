import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands
from db import *

import random
from random import choices
from discord.ext.commands import cooldown, BucketType

bot = commands.Bot(command_prefix="+")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
@commands.cooldown(10, 3600, commands.BucketType.user)
async def pull(ctx):
    r = [p0, p1, p2]
    w = [85.5, 8.5, 6]
    x = random.choices(r,w)
    y = random.choice(x[0])
    await ctx.send(y)

@pull.error
async def pull_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '<:puggiFIRE:808672592550297631> PUGGI IS ON FIRE! Cooldown in **{:.2f}** seconds!'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error

server.server()
bot.run(TOKEN)
