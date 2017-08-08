import discord
from discord.ext import commands
import datetime
import time
import random
import asyncio
import json
import aiohttp

terms=""
definition_number=0

class Kwug():

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def random(self, ctx, start : int, stop : int):
		'''Generates a Random Number Between Two Numbers'''
		emb = discord.Embed(title="Your Random Number Is...", description=str(random.randint(start, stop)), color=discord.Color.red())
		await self.bot.say(embed=emb)

	@commands.command()
	async def urban(self, *, search_terms : str):
		'''Searches Up a Term in Urban Dictionary'''
		search_terms = search_terms.split(" ")
		global definition_number
		definition_number=0
		try:
			definition_number = int(search_terms[-1]) - 1
			search_terms.remove(search_terms[-1])
		except ValueError:
			definition_number = 0
		if definition_number not in range(0, 11):
			pos = 0                
		search_terms = "+".join(search_terms)
		url = "http://api.urbandictionary.com/v0/define?term=" + search_terms
		async with aiohttp.get(url) as r:
			result = await r.json()
		if result["list"]:
			definition = result['list'][definition_number]['definition']
			example = result['list'][definition_number]['example']
			defs = len(result['list'])
			global terms
			search_terms = search_terms.split("+")
			terms=""
			for i in search_terms:
				terms += i
				terms += " "
			msg = ("{}\n\n**Example:\n**{}".format(definition, example))
			title = (terms + "  ({}/{})".format(definition_number+1, defs))
			emb = discord.Embed(color = discord.Color.blue(), title = title, description=msg)
			await self.bot.say(embed=emb)
		else:
			await self.bot.say("Your search terms gave no results.")

	@commands.command()
	async def coinflip(self):
		'''Flips a coin'''
		flip = random.randint(0,1)
		coin = ""
		if flip == 0:
			coin = "Tail"
		elif flip == 1:
			coin = "Head"
		emb=discord.Embed(title="You Flipped A...", description=coin, color = discord.Color.gold())
		await self.bot.say(embed=emb)
def setup(bot):
    bot.add_cog(Kwug(bot))