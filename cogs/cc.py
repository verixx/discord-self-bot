import discord
from discord.ext import commands

class cog:
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
    await self.bot.say('1: {}, 2:{}, The rest: {}'.format(arg1, arg2, therest))

  @commands.command(pass_context=True)
  async def echohelp(self):
    em = discord.Embed(author="4JR",image="https://discordapp.com/api/v6/users/180314310298304512/avatars/eb45214491b879d0db62a8165148a311.jpg",title="Echo Help",description="Visit https://echo.xtclabs.net/ to learn about the basic things Echo can do \nVisit https://ars.xtclabs.net/ to learn about the ever-evolving ARS. \nVisit https://github.com/proxikal/Echo to see Echo 1.0 Documentation!", color=0x00FFFF)
    await self.bot.say(embed=em)
    
  @commands.command(pass_context=True)
  async def help(self):
    em = discord.Embed(author="4JR",image="https://discordapp.com/api/v6/users/180314310298304512/avatars/eb45214491b879d0db62a8165148a311.jpg",title="Help",description="Some Cool Text!", color=0x00FFFF)
    await self.bot.say(embed=em)
    
def setup(bot):
  bot.add_cog(cog(bot))
