"""
MIT License

Copyright (c) 2017 Grok's naughty dev XAOS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import discord
from discord.ext import commands
import bs4 as bs
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json
import io

"""Nsfw commands."""

class Nsfw:
    def __init__(self, bot):
        self.bot = bot
        self.session = bot.session
        # self.session = discord.http.HTTPClient
        self.color = bot.user_color

    @commands.command()
    async def xbooru(self, ctx):
        """Random image from Xbooru"""
        try:
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                pass
            await ctx.channel.trigger_typing()
            query = urllib.request.urlopen("http://xbooru.com/index.php?page=post&s=random").read()
            soup = bs.BeautifulSoup(query, 'html.parser')
            image = soup.find(id="image").get("src")
            last = str(image.split('?')[-2]).replace('//', '/').replace(':/', '://')
            em = discord.Embed(colour=discord.Colour(0xed791d))
            em.description = f'[Full Size Link*]({last})'
            em.set_image(url=last)
            em.set_footer(text='* click link at your own risk!')
            try:
                await ctx.send(embed=em)
            except discord.HTTPException:
                await ctx.send('Unable to send embeds here!')
                try:
                    async with ctx.session.get(image) as resp:
                        image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, 'xbooru.png'))
                except discord.HTTPException:
                    await ctx.send(image)

        except Exception as e:
            await ctx.send(f'```{e}```')


def setup(bot):
    bot.add_cog(Nsfw(bot))
