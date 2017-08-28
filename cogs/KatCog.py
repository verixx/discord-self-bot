import discord
from discord.ext import commands

class KatCog:
  def __init__(self, bot):
    self.bot = bot

  @commands.command(pass_context = True)
  async def hi(self, ctx):
    await self.bot.say('Hello!!')
    await self.bot.delete_message('Hello!!')

  @commands.command(pass_context = True)
  async def copycat(self, ctx, *, message: str):
    '''Copy what you just said'''
    await self.bot.say(message)

  @commands.command(pass_context = True)
  async def meme(self, ctx, *, message : str=None):
    '''Post certain memes'''
    doge=discord.Embed(color=0xed, description='Doge')
    list=discord.Embed(title='Memes:', description='Doge\nFeelsBadMan', color=0xed)
    doge.set_image(url="http://i0.kym-cdn.com/entries/icons/mobile/000/013/564/doge.jpg")
    pepe=discord.Embed(color=0xed, description='FeelsBadMan'
    pepe.set_image(url="https://cdn.nplus1.ru/images/2016/12/30/d238c7d3f81f8246281e52f5d377e48d.jpg")
    if 'doge' in message:
      await self.bot.say(embed=doge)
    if 'list' in message:
      await self.bot.say(embed=list)
    if 'FeelsBadMan' in message:
      await self.bot.say(embed=pepe)
    
  @commands.command(pass_context = True)
  async def slap(self,ctx, *, person: str):
      name = ctx.message.author
      embed=discord.Embed(color=0xed, title="{} has slapped {}".format(name.name, person))
      embed.set_image(url="https://i.ytimg.com/vi/7AXB8nGq5jc/maxresdefault.jpg")
      await self.bot.say(embed=embed)
      await self.bot.delete_message(ctx.message)
    
def setup(bot):
  bot.add_cog(KatCog(bot))
