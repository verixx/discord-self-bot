
# -*- coding: utf-8 -*-

"""
The MIT License (MIT)
Copyright (c) 2017 SML
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from enum import Enum

from __main__ import send_cmd_help
from discord.ext import commands
from random import choice
import discord
from discord.ext import commands
import datetime
import time
import random
import asyncio
import os

#DEFINED TO ONLY WORK WITH RACF SERVER

clan2num = {
    'alpha' : 0,
    'bravo' : 1,
    'charlie' : 2,
    'delta' : 3,
    'echo' : 4,
    'foxtrot' : 5,
    'golf' : 6,
    'hotel' : 7,
    'esports' : 8
}

class Trophies:
    """
    Display the current trophy requirements for RACF.
    Note: RACF specific plugin for Red
    """

    def __init__(self, bot):
        """Init."""
        self.bot = bot


    @commands.group(aliases=["tr"], pass_context=True)
    async def trophies(self, ctx):
        """Display RACF Trophy requirements."""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @trophies.command(name="show", pass_context=True)
    async def trophies_show(self, ctx, clan=None):
        """Display the requirements."""
        server = ctx.message.server
        botcmds = self.bot.get_channel('275624978781569024')
        if clan == None:
            await self.bot.delete_message(ctx.message)
            await self.bot.say("!tr show")
        else:
            await self.bot.edit_message(ctx.message, new_content='!'+ctx.message.content[2:])
            await self.bot.send_message(botcmds, "!tr show")
            await asyncio.sleep(1)
            messages = []
            async for m in self.bot.logs_from(botcmds, limit=2):
                messages.append(m)
            message = messages[0]
            full_embed = message.embeds[0]
            url = full_embed['author']['url']
            clans = message.embeds[0]['fields']
            print(clan2num[clan.lower()])
            try:
                clanval = clans[clan2num[clan.lower()]]
            except:
                await self.bot.say("invalid clan")
            em = discord.Embed(title=clanval['name']+' Trophy Requirement', color=discord.Color(0xFE3D40), 
                description=clanval['value'])
            em.set_thumbnail(url=url)
            em.set_author(name='AlphaBot', icon_url=url, url=url)
            await self.bot.say(embed=em)

    @trophies.command(name="set", pass_context=True)
    async def trophies_set(self, ctx, clan: str, *, req: str):
        """Set the trophy requirements for clans."""
        botcmds = self.bot.get_channel('275624978781569024')
        await self.bot.send_message(botcmds, "!tr set "+clan+" "+req)

    # @commands.group(aliases=["bstr"], pass_context=True, no_pm=True)
    # async def bstrophies(self, ctx):
    #     """Display RACF Trophy requirements."""
    #     if ctx.invoked_subcommand is None:
    #         await send_cmd_help(ctx)

    # @bstrophies.command(name="show", pass_context=True, no_pm=True)
    # async def bstrophies_show(self, ctx):
    #     """Display the requirements."""
    #     server = ctx.message.server
    #     data = self.embed_trophies(server, ClanType.BS)
    #     await self.bot.say(embed=data)

    # @bstrophies.command(name="set", pass_context=True, no_pm=True)
    # @commands.has_any_role(*bs_set_allowed_roles)
    # async def bstrophies_set(self, ctx, clan: str, *, req: str):
    #     """Set the trophy requirements for clans."""
    #     await self.run_trophies_set(ctx, ClanType.BS, clan, req)

    # async def run_trophies_set(self, ctx, clan_type, clan: str, req: str):
    #     """Set to trophy requirements for clans."""
    #     server = ctx.message.server
    #     clans = RACF_CLANS[clan_type]

    #     if clan.lower() not in [c.lower() for c in clans]:
    #         await self.bot.say("Clan name is not valid.")
    #         return

    #     for i, c in enumerate(clans):
    #         if clan.lower() == c.lower():
    #             self.settings[server.id][
    #                 "Trophies"][clan_type][i]["value"] = req
    #             await self.bot.say(
    #                 "Trophy requirement for {} "
    #                 "updated to {}.".format(clan, req))
    #             break

    #     dataIO.save_json(JSON, self.settings)

    # def embed_trophies(self, server, clan_type):
    #     """Return Discord embed."""
    #     color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
    #     color = int(color, 16)

    #     if clan_type == ClanType.CR:
    #         our_clans = 'Clash Royale clans'
    #     else:
    #         our_clans = 'Brawl Stars bands'

    #     description = (
    #         "Minimum trophies trophies to join our {}. "
    #         "Current trophies required."
    #     ).format(our_clans)

    #     data = discord.Embed(
    #         color=discord.Color(value=color),
    #         title="Trophy requirements",
    #         description=description
    #     )

    #     clans = self.settings[server.id]["Trophies"][clan_type]

    #     for clan in clans:
    #         name = clan["name"]
    #         value = clan["value"]

    #         if str(value).isdigit():
    #             value = '{:,}'.format(int(value))

    #         data.add_field(name=str(name), value=value)

    #     if server.icon_url:
    #         data.set_author(name=server.name, url=server.icon_url)
    #         data.set_thumbnail(url=server.icon_url)
    #     else:
    #         data.set_author(name=server.name)

    #     return data



def setup(bot):
    """Setup bot."""
    bot.add_cog(Trophies(bot))

