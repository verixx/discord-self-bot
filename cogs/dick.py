import re
from discord.ext import commands

'''Module for measuring your's and other's dick size'''


class Dick:

    def __init__(self, bot):
        self.bot = bot

    def dick_size(self, id):
        s = 0
        while id:
            s += id % 10
            id //= 10
        return (s%10) * 2

    @commands.command(pass_context=True)
    async def dick(self, ctx, mention=""):
        """How big are you?"""
        id_regex = re.compile('<@!?(\d+)>')
        ids = id_regex.findall(ctx.message.content)
        if len(ids) > 0:
            for member in ids:
                await ctx.send(' <@{}> Size: 8{}D'.format(member, self.dick_size(int(member)) * '='))
        else:
            await ctx.send(' <@{}> Size: 8{}D'.format(str(ctx.message.author.id), self.dick_size(ctx.message.author.id) * '='))


def setup(bot):
    bot.add_cog(Dick(bot))
