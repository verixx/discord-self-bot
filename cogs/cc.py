import discord
from discord.ext import commands

class JRCogs:
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def echo(self, *, text):
    await self.bot.say(text)
    
  @commands.command()
  async def hi(self):
    await self.bot.say('hello')
    
  @commands.command(pass_context=True)
  async def test(self, ctx, arg1, arg2, *, therest):
    await bot.say('1: {}, 2:{}, The rest: {}'.format(arg1, arg2, therest))

  @commands.command(pass_context=True)
  async def jrembed(self, ctx, *, text):
    em = discord.Embed(description=text, color=0x00FFFF)
    await self.bot.say(embed=em)
    
def setup(bot):
  bot.add_cog(JRCogs(bot))
