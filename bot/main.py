import discord
import os
#import pynacl
#import dnspython
import server
import random
import datetime

from discord.ext import commands
from random import choices
from discord.ext.commands import cooldown, BucketType
from pretty_help import PrettyHelp
from puggibotdb import *

bot = commands.Bot(command_prefix="+",
description = 'PuggiBot v1.2.5',
help_command = PrettyHelp(no_category='Commands',show_index = False))
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you suffer"))
    print(f"Logged in as {bot.user.name}({bot.user.id})")
    counting = 0
    r = [p0, p1, p2, p3]
    w = [50, 25.5, 18.5, 6]

@bot.command(name='ping', help='IT WORKS!')
async def ping(ctx):
    e = ["**Pang!** <:pangblush:649970659358933002>",
    "**Pang!** <:wangannoyed:792849470877859876>",
    "**Pang!** <:spangwhat:792849432038473768>"]
    s = random.choice(e)
    await ctx.send(s)

@bot.command(name='pull', help='Pulls a random image. Max 10 images per hour for each user!')
@commands.cooldown(10, 3600, commands.BucketType.user)
async def pull(ctx):
    if (counting < 10):
      x = random.choices(r,w)
      y = random.choice(x[0])
      counting = counting + 1
    else:
      y = random.choice(v)
      counting = 0

    await ctx.send(y)

@pull.error
async def pull_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        sec = error.retry_after
        if(sec < 60):
          msg = '<:puggiFIRE:808672592550297631> PUGGI IS ON FIRE! Cooldown in **{:.0f}** seconds!'.format(sec)
        else:
          minut = sec // 60
          sec2 = sec % 60
          msg = '<:puggiFIRE:808672592550297631> PUGGI IS ON FIRE! Cooldown in **{:.0f}** minutes and **{:.0f}** seconds!'.format(minut,sec2)

        y = random.choice
        await ctx.send()
        await ctx.send(msg)
    else:
        raise error

@bot.command(name='rates', help='Check the rates for each rarity!')
async def rates(ctx):
    await ctx.send('<:star_N:822188326114557984> = '+str(w[0])+'%\n<:star_R:822188398965293186> = '+str(w[1])+'%\n<:star_SR:822188419853058070> = '+str(w[2])+'%\n<:star_SSR:822188441361055774> = '+str(w[3])+'%')

server.server()
bot.run(TOKEN)
