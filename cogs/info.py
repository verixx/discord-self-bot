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

    @commands.command(aliases=['server','si'])
    @commands.guild_only()
    async def serverinfo(self, ctx, server_id : int=None):
        '''See information about the server.'''
        server = self.bot.get_server(id=server_id) or ctx.guild
        total_users = len(server.members)
        online = len([m for m in server.members if m.status != discord.Status.offline])
        text_channels = len([x for x in server.channels if isinstance(x, discord.TextChannel)])
        voice_channels = len(server.channels) - text_channels
        passed = (ctx.message.created_at - server.created_at).days
        created_at = "Since {}. That's over {} days ago!".format(server.created_at.strftime("%d %b %Y %H:%M"), passed)

        colour = await ctx.get_dominant_color(server.icon_url)

        data = discord.Embed(description=created_at,colour=colour)
        data.add_field(name="Region", value=str(server.region))
        data.add_field(name="Users", value="{}/{}".format(online, total_users))
        data.add_field(name="Text Channels", value=text_channels)
        data.add_field(name="Voice Channels", value=voice_channels)
        data.add_field(name="Roles", value=len(server.roles))
        data.add_field(name="Owner", value=str(server.owner))
        data.set_footer(text="Server ID: " + str(server.id))
        data.set_author(name=server.name, icon_url=None or server.icon_url)
        data.set_thumbnail(url=None or server.icon_url)

        await ctx.send(embed=data)

    @commands.command(aliases=['ui'])
    async def userinfo(self, ctx, *, member : commands.MemberConverter=None):
        '''Get information about a member of a server'''
        user = member or ctx.message.author
        avi = user.avatar_url
        time = ctx.message.created_at
        desc = '{0} is chilling in {1} mode.'.format(user.name, user.status)
        em = discord.Embed(colour=color, description=desc, timestamp=time)
	
	if ctx.guild:
            server = ctx.guild
            roles = sorted(user.roles, key=lambda c: c.position)
            for role in roles:
                if str(role.color) != "#000000":
                    color = int(str(role.color)[1:], 16)
	    rolenames = ', '.join([r.name for r in roles]) or 'None'
	    member_number = sorted(server.members, key=lambda m: m.joined_at).index(user) + 1
            em.add_field(name='Member No.',value=str(member_number),inline = True)
	    em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y'))
            em.add_field(name='Roles', value=rolenames, inline=True)
	    em.set_author(name=user, icon_url=server.icon_url)
	
	else:
            em.set_author(name=user, icon_url=avi)
            
        em.add_field(name='Nick', value=user.nick, inline=True)
        em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y'))
        em.set_footer(text='User ID: '+str(user.id))
        em.set_thumbnail(url=avi)
        await ctx.send(embed=em)

    @commands.command(aliases=['bot', 'info'])
    async def about(self, ctx):
        cmd = r'git show -s HEAD~3..HEAD --format="[{}](https://github.com/verixx/selfbot/commit/%H) %s (%cr)"'
        if os.name == 'posix':
            cmd = cmd.format(r'\`%h\`')
        else:
            cmd = cmd.format(r'`%h`')

        revision = os.popen(cmd).read().strip()
        embed = discord.Embed()
        embed.url = 'https://discord.gg/pmQSbAd'
        embed.colour = await ctx.get_dominant_color(ctx.author.avatar_url)

        embed.set_author(name='selfbot.py', icon_url=ctx.author.avatar_url)

        total_members = sum(1 for _ in self.bot.get_all_members())
        total_online = len({m.id for m in self.bot.get_all_members() if m.status is discord.Status.online})
        total_unique = len(self.bot.users)

        voice_channels = []
        text_channels = []
        for guild in self.bot.guilds:
            voice_channels.extend(guild.voice_channels)
            text_channels.extend(guild.text_channels)

        text = len(text_channels)
        voice = len(voice_channels)

        now = datetime.datetime.utcnow()
        delta = now - self.bot.uptime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        fmt = '{h}h {m}m {s}s'
        if days:
            fmt = '{d}d ' + fmt
        uptime = fmt.format(d=days, h=hours, m=minutes, s=seconds)


        embed.add_field(name='Latest Changes', value=revision)
        embed.add_field(name='Author', value='verixx#7220')
        embed.add_field(name='Uptime', value=uptime)
        embed.add_field(name='Guilds', value=len(self.bot.guilds))
        embed.add_field(name='Members', value=f'{total_unique} total\n{total_online} online')
        embed.add_field(name='Channels', value=f'{text} text\n{voice} voice')
        memory_usage = self.bot.process.memory_full_info().uss / 1024**2
        cpu_usage = self.bot.process.cpu_percent() / psutil.cpu_count()
        embed.add_field(name='Process', value=f'{memory_usage:.2f} MiB\n{cpu_usage:.2f}% CPU')
        embed.set_footer(text=f'Powered by discord.py {discord.__version__}')
        await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Information(bot))
