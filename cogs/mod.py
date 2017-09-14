'''
MIT License

Copyright (c) 2017 verixx

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
'''

import discord
from discord.ext import commands
from urllib.parse import urlparse
import datetime
import asyncio
import psutil
import random
import pip
import os
import io


class Information:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member : commands.MemberConverter):
            '''Kick someone from the server.'''
            try:
                emb = discord.Embed(color=0x00FFFF, description='{} was kicked.'.format(member), title='Kick')
                emb.set_thumbnail(member.avatar_url)
                await self.bot.kick(member)
                await self.bot.send(embed=emb)
                await self.bot.delete_message(ctx.message)
            except:
                await self.bot.send(discord.Embed(color=0x00FFFF, description='You do not have permissions to kick users.', title='Kick'))
                await asyncio.sleep(5)
                await self.bot.delete_message(ctx.message)


def setup(bot):
	bot.add_cog(Information(bot))