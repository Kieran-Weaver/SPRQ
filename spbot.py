import discord
from discord.ext import commands
import rqstate
import os
bot = commands.Bot(command_prefix=">")
bot.remove_command("help")

rq = rqstate.RQState("rooms.json")

@bot.command()
async def join(ctx):
	name = str(ctx.author)
	rq.loadPlayer(name)
	rq.printState(name)
	await ctx.send(os.linesep.join(rq.getMessages(name)))

@bot.event
async def on_message(message):
	if message.author.bot or not(message.content.startswith(">")):
		return
	name = str(message.author)
	msg = message.lstrip("> ")
	rq.parseMessage(name, msg)
	rq.printState(name)
	await ctx.send(os.linesep.join(rq.getMessages(name)))

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		return
	elif isinstance(error, commands.MissingRequiredArgument):
		return
	elif isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"**{ctx.author}**, this command is on cooldown. Try again in {error.retry_after} seconds")
	else:
		await ctx.send(str(error) + "\n")
    
bot.run(str(os.getenv("TOKEN")), bot=True, reconnect=True)
