import discord
from discord.ext import commands

class cc:
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def echohelp(self):
    await self.bot.say('hi')
    
  @commands.command()
  async def hi(self):
    await self.bot.say('hello')

  @commands.command(pass_context=True)
  async def embed(self, ctx, *, text):
    em = discord.Embed(description=text, color=0x00FFFF)
    await self.bot.say(embed=em)
    
def setup(bot):
  bot.add_cog(cc(bot))
