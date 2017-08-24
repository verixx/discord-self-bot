import discord
from discord.ext import commands

class Custom Commands:
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def echo-help(self):
    await self.bot.say('hi')
    
  @commands.command()
  async def hi(self):
    await self.bot.say('hello')
    
def setup(bot):
  bot.add_cog(Custom Commands(bot))
