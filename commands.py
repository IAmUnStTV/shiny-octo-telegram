import discord
import time
from discord.ext import commands

bot = commands.Bot(command_prefix='sot!')

@bot.command()
async def ping(ctx):
    tic = time.perf_counter()
    await ctx.send('Pong!')
    toc = time.perf_counter()
    tictoc = toc - tic
    fullcmd = 'Time:' + tictoc
    await ctx.send(fullcmd)

bot.run('[OMITTED]') # Note: this line is to hide the API key so random peoople can't destroy the bot.
