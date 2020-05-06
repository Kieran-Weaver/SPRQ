import discord
from discord.ext import commands
import rqstate
import os
bot = commands.Bot(command_prefix=",,")
bot.remove_command("help")

rq = rqstate.RQState("rooms.json")

@bot.event
async def on_message(message):
	if message.author.bot or not(message.content.startswith("SP ") or message.content.startswith("sp ")):
		return
	channel = message.channel
	name = str(message.author)
	if name not in rq.players:
		rq.loadPlayer(name)
	msg = str(message.content)[2:].lstrip()
	if msg:
		rq.parseMessage(name, msg)
	rq.printState(name)
	membed = discord.Embed(title="SPRQ", type="rich")
	membed.add_field(name=f"Replying to {name}", value=os.linesep.join(rq.getMessages(name)), inline=True)
	await channel.send(embed=membed)

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
