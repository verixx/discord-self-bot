import discord
from discord.ext import commands

class YourCog:
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def test(self):
    await bot.say('hello')

def setup(bot):
  bot.add_cog(YourCog(bot))
