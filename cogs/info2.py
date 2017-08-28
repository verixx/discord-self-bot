import discord
from discord.ext import commands
import datetime
import time
import random
import asyncio
import json
from ext.commands import Bot
from fuzzywuzzy import fuzz
from __main__ import send_cmd_help


class Info2():


    def __init__(self, bot):
        self.bot = bot
         
    @commands.command(pass_context=True)
    async def help2(self, ctx, cog = None):
        """Shows listed help message."""
        author = ctx.message.author
        await self.bot.delete_message(ctx.message)
        n = 0
        if cog == None:
            pages = self.bot.formatter.format_help_for(ctx, self.bot, 3)
            for page in pages:
                try:
                    if(n!=0):
                        page.set_author(name='', url='')
                    if(n!=len(pages)-1):
                        page.set_footer(text='')
                    await self.bot.say(embed=page)
                    n += 1
                except:
                    await self.bot.say('I need the embed links perm.')
        else:
            pages = self.bot.formatter.format_help_for(ctx, self.bot, 1)
            cog = cog.lower()
            maxfuzrat = 0
            bestmatch = pages[0]
            currentfuzrat = 0
            for page in pages:
                pagecog = page.to_dict()['fields'][0]['name'] # cog name of page
                pagecog = pagecog[:-1].lower() #remove the colon and make it lowercase
                if '\u200b' in pagecog:
                    pagecog.replace('\u200b', '')
                currentfuzrat = fuzz.ratio(cog, pagecog)
                if  currentfuzrat > maxfuzrat:
                    # print("page cog: {}\nsearch cog: {}\nfuzz ratio: {}".format(pagecog, cog, currentfuzrat))
                    maxfuzrat = currentfuzrat
                    bestmatch = page
            await self.bot.say(embed=bestmatch)





def setup(bot):
    bot.add_cog(Info2(bot))
