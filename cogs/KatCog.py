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
    em=discord.Embed(color=0xed, description='meme')
    list=discord.Embed(title='Memes:', description='Testing\n Testing #2', color=0xed)
    await self.bot.say(embed=list)
    if 'testing' in message:
      em.set_image(url="https://images-ext-1.discordapp.net/external/I2njA8Ftmb2rA34vLWK__QVBgH8v4qCh-ZNfIBZ9PUA/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/300396755193954306/a73725eaa41bf59a73d283f35b280781.png?width=96&height=96") # An avatar link to demonstrate

    await self.bot.say(embed=em)
    
  @commands.command(pass_context = True)
  async def slap(self,ctx, *, person: str):
      name = ctx.message.author
      embed=discord.Embed(color=0xed, title="{} has slapped {}".format(name.name, person))
      embed.set_image(url="https://i.ytimg.com/vi/7AXB8nGq5jc/maxresdefault.jpg")
      await self.bot.say(embed=embed)
      await self.bot.delete_message(ctx.message)
    
def setup(bot):
  bot.add_cog(KatCog(bot))
