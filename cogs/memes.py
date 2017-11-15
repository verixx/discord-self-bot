
import discord
from discord.ext import commands
import asyncio
from sys import argv

class Memes:
    """
    Meme commands
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    async def _meme(self, ctx, msg):
        await ctx.send(msg)

    # list memes
    @commands.command(name="listmemes")
    async def _listmemes(self, ctx):
        """List meme commands."""
        # this feels wrong...
        funcs = dir(self)
        msg = "```\n"
        msg += ", ".join(func for func in funcs if func != "bot" and func[0] != "_")
        msg += "```"
        await self._meme(ctx, msg)

    # memes
    @commands.command(hidden=True)
    async def screams2(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/bh45fyL.png")

    @commands.command(hidden=True)
    async def screams(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/j0Dkv2Z.png")

    @commands.command(hidden=True)
    async def ehh(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/2SBC1Qo.jpg")

    @commands.command(hidden=True)
    async def wat(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/bp2YRAf.png")
        
    @commands.command(hidden=True, name="no!!")
    async def nope(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/OcDrUYO.png")

    @commands.command(hidden=True)
    async def illyacup(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/GMRp1dj.jpg")

    @commands.command(hidden=True)
    async def quivers(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/Aq5VISF.gifv")

    @commands.command(hidden=True)
    async def nya(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/WKB08Iq.png")

    @commands.command(hidden=True, name="916253")
    async def numbers(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/NukslEg.png")

    @commands.command(hidden=True)
    async def thump(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/LZhDBkH.gifv")

    @commands.command(hidden=True)
    async def rikkaeh(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/3Lg5jlA.png")

    @commands.command(hidden=True)
    async def orz(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/LEey0Cd.png")

    @commands.command(hidden=True)
    async def shotsfired(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/zf2XrNk.gifv")

    @commands.command(hidden=True)
    async def thumbsup(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/2dll9My.png")

    @commands.command(hidden=True)
    async def rip(self, ctx):
        """Memes."""
        await self._meme(ctx, "Press F to pay respects.")

    @commands.command(hidden=True)
    async def permabrocked(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/ARsOh3p.jpg")

    @commands.command(hidden=True)
    async def lucina(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/tnWSXf7.png")

    @commands.command(hidden=True)
    async def lucina2(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/ZPMveve.jpg")

    @commands.command(hidden=True)
    async def thumbsup2(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/hki1IIs.gifv")

    # Cute commands :3
    @commands.command(hidden=True)
    async def headpat(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/7V6gIIW.jpg")

    @commands.command(hidden=True)
    async def headpat2(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/djhHX0n.gifv")

    @commands.command(hidden=True)
    async def sudoku(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/VHlIZRC.png") 
        
    @commands.command(hidden=True)
    async def rawr(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/Bqw4OwQ.png")

    @commands.command(hidden=True)
    async def baka(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/OyjCHNe.png")
        
    @commands.command(hidden=True)
    async def pantsu(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/BoRZLTU.png")
        
    @commands.command(hidden=True)
    async def animal(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/Rhd6H8x.jpg")
        
    @commands.command(hidden=True)
    async def rub(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/DkxNtGK.gif")
        
    @commands.command(hidden=True)
    async def spin(self, ctx):
        """Cute"""
        await self.bot.say("Illya is loading...")
        await asyncio.sleep(5)
        await self._meme(ctx, "http://i.imgur.com/Q7CECXA.gif")
        
    @commands.command(hidden=True)
    async def luff(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/8TKIixk.png")
        
    @commands.command(hidden=True)
    async def fug(self, ctx):
        """meme"""
        await self._meme(ctx, "http://i.imgur.com/ZhTZtDa.png")
        
    @commands.command(hidden=True)
    async def fug2(self, ctx):
        """meme"""
        await self._meme(ctx, "http://i.imgur.com/9LvnrBB.png")
        
    @commands.command(hidden=True)
    async def walksin(self, ctx):
        """meme"""
        await self._meme(ctx, "http://i.imgur.com/xMfzlnU.jpg")
        
    @commands.command(hidden=True)
    async def walksout(self, ctx):
        """meme"""
        await self._meme(ctx, "http://i.imgur.com/wIRkdud.jpg")
        
    @commands.command(hidden=True)
    async def period(self, ctx):
        """meme"""
        await self._meme(ctx, "http://i.imgur.com/IGu4zGZ.jpg")
        
    @commands.command(hidden=True)
    async def sadness(self, ctx):
        """:c"""
        await self._meme(ctx, "http://i.imgur.com/maRp8nB.png")
        
    @commands.command(hidden=True)
    async def negativity(self, ctx):
        """:c"""
        await self._meme(ctx, "hhttp://i.imgur.com/1D5vHSk.png")

# Load the extension
def setup(bot):
    bot.add_cog(Memes(bot))
