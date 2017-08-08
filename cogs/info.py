import discord
from discord.ext import commands
import datetime
import time
import random
import asyncio
import json
from ext.commands import Bot
from __main__ import send_cmd_help

class CannotPaginate(Exception):
    pass

class Pages:
    """Implements a paginator that queries the user for the
    pagination interface.
    Pages are 1-index based, not 0-index based.
    If the user does not reply within 2 minutes then the pagination
    interface exits automatically.
    Parameters
    ------------
    bot
        The bot instance.
    message
        The message that initiated this session.
    entries
        A list of entries to paginate.
    per_page
        How many entries show up per page.
    Attributes
    -----------
    embed: discord.Embed
        The embed object that is being used to send pagination info.
        Feel free to modify this externally. Only the description,
        footer fields, and colour are internally modified.
    permissions: discord.Permissions
        Our permissions for the channel.
    """
    def __init__(self, bot, *, message, entries, per_page=12):
        self.bot = bot
        self.entries = entries
        self.message = message
        self.author = message.author
        self.per_page = per_page
        self.embed = discord.Embed()
        self.paginating = len(entries) > per_page
        self.reaction_emojis = [
            ('\N{BLACK LEFT-POINTING DOUBLE TRIANGLE}', self.first_page),
            ('\N{BLACK LEFT-POINTING TRIANGLE}', self.previous_page),
            ('\N{BLACK RIGHT-POINTING TRIANGLE}', self.next_page),
            ('\N{BLACK RIGHT-POINTING DOUBLE TRIANGLE}', self.last_page),
            ('\N{INPUT SYMBOL FOR NUMBERS}', self.numbered_page ),
            ('\N{BLACK SQUARE FOR STOP}', self.stop_pages),
            ('\N{INFORMATION SOURCE}', self.show_help),
        ]

        server = self.message.server
        if server is not None:
            self.permissions = self.message.channel.permissions_for(server.me)
        else:
            self.permissions = self.message.channel.permissions_for(self.bot.user)

        if not self.permissions.embed_links:
            raise CannotPaginate('Bot does not have embed links permission.')

        self.categs = []

        for i, e in enumerate(self.entries):
            if e.startswith('**'):
                self.categs.append(i)

        self.maximum_pages = len(self.categs)

    def get_page(self, page):
        
        base = self.categs[page-1]
        try:
            end = self.categs[page]
            return self.entries[base:end]
        except:
            return self.entries[base:]



    async def show_page(self, page, *, first=False):
        self.current_page = page
        entries = self.get_page(page)
        p = [t for t in entries]

        self.embed.set_footer(text='Page %s/%s (%s Commands)' % (page, self.maximum_pages, len(self.entries)-len(self.categs)))

        if not self.paginating:
            self.embed.clear_fields()
            self.embed.add_field(name=p[0], value='\n'.join(p[1:]))
            return await self.bot.send_message(self.message.channel, embed=self.embed)

        if not first:
            self.embed.clear_fields()
            self.embed.add_field(name=p[0], value='\n'.join(p[1:]))
            await self.bot.edit_message(self.message, embed=self.embed)
            return

        # verify we can actually use the pagination session
        if not self.permissions.add_reactions:
            raise CannotPaginate('Bot does not have add reactions permission.')

        if not self.permissions.read_message_history:
            raise CannotPaginate('Bot does not have Read Message History permission.')

        self.embed.add_field(name=p[0], value='\n'.join(p[1:]))
        self.embed.add_field(name='Confused?', value='React with \N{INFORMATION SOURCE} by typing s.i for more info')
        self.message = await self.bot.send_message(self.message.channel, embed=self.embed)
        for (reaction, _) in self.reaction_emojis:
            if self.maximum_pages == 2 and reaction in ('\u23ed', '\u23ee'):
                # no |<< or >>| buttons if we only have two pages
                # we can't forbid it if someone ends up using it but remove
                # it from the default set
                continue

            # await self.bot.add_reaction(self.message, reaction)

    async def checked_show_page(self, page):
        if page != 0 and page <= self.maximum_pages:
            await self.show_page(page)

    async def first_page(self):
        """goes to the first page (s.first)"""
        await self.show_page(1)

    async def last_page(self):
        """goes to the last page (s.last)"""
        await self.show_page(self.maximum_pages)

    async def next_page(self):
        """goes to the next page (s.next)"""
        await self.checked_show_page(self.current_page + 1)

    async def previous_page(self):
        """goes to the previous page (s.prev)"""
        await self.checked_show_page(self.current_page - 1)

    async def show_current_page(self):
        if self.paginating:
            await self.show_page(self.current_page)

    async def numbered_page(self):
        """lets you type a page number to go to (s.page)"""
        to_delete = []
        to_delete.append(await self.bot.send_message(self.message.channel, 'What page do you want to go to?'))
        msg = await self.bot.wait_for_message(author=self.author, channel=self.message.channel,
                                              check=lambda m: m.content.isdigit(), timeout=30.0)
        if msg is not None:
            page = int(msg.content)
            to_delete.append(msg)
            if page != 0 and page <= self.maximum_pages:
                await self.show_page(page)
            else:
                to_delete.append(await self.bot.say('Invalid page given. (%s/%s)' % (page, self.maximum_pages)))
                await asyncio.sleep(5)
        else:
            to_delete.append(await self.bot.send_message(self.message.channel, 'Took too long.'))
            await asyncio.sleep(5)

        try:
            for x in to_delete:
                await self.bot.delete_message(x)
        except Exception:
            pass

    async def show_help(self):
        """shows this message (s.i)"""
        e = discord.Embed()
        messages = []
        messages.append('This interactively allows you to see pages of text by navigating with ' \
                        'reactions. They are as follows:\n')

        for (emoji, func) in self.reaction_emojis:
            messages.append('%s %s' % (emoji, func.__doc__))

        e.add_field(name='Welcome to the interactive paginator!',value='\n'.join(messages))
        e.colour =  0x00FFFF #0x738bd7 # blurple
        e.set_footer(text='We were on page %s before this message.' % self.current_page)
        await self.bot.edit_message(self.message, embed=e)

        async def go_back_to_current_page():
            await asyncio.sleep(60.0)
            await self.show_current_page()

        self.bot.loop.create_task(go_back_to_current_page())

    async def stop_pages(self):
        """stops the interactive pagination session (s.stop)"""
        await self.bot.delete_message(self.message)
        self.paginating = False

    def react_check(self, reaction, user):
        if user is None or user.id != self.author.id:
            return False

        for (emoji, func) in self.reaction_emojis:
            if reaction.emoji == emoji:
                self.match = func
                return True
        return False

    async def paginate(self):
        """Actually paginate the entries and run the interactive loop if necessary."""
        await self.show_page(1, first=True)

        while self.paginating:
            react = await self.bot.wait_for_reaction(message=self.message, check=self.react_check, timeout=120.0)
            if react is None:
                self.paginating = False
                try:
                    await self.bot.clear_reactions(self.message)
                except:
                    pass
                finally:
                    break

            try:
                await self.bot.remove_reaction(self.message, react.reaction.emoji, react.user)
            except:
                pass # can't remove it so don't bother doing so

            await self.match()

class Info():


    def __init__(self, bot):
        self.bot = bot
         


    @commands.command(pass_context=True,aliases=['s','serverinfo','si'])
    async def server(self, ctx):
        '''See information about the server.'''
        server = ctx.message.server
        online = len([m.status for m in server.members
                      if m.status == discord.Status.online or
                      m.status == discord.Status.idle or
                      m.status == discord.Status.dnd])
        total_users = len(server.members)
        text_channels = len([x for x in server.channels
                             if x.type == discord.ChannelType.text])
        voice_channels = len(server.channels) - text_channels
        passed = (ctx.message.timestamp - server.created_at).days
        created_at = ("Since {}. That's over {} days ago!"
                      "".format(server.created_at.strftime("%d %b %Y %H:%M"),
                                passed))
        colour = ("#%06x" % random.randint(0, 0xFFFFFF))
        colour = int(colour[1:], 16)

        data = discord.Embed(
            description=created_at,
            colour=discord.Colour(value=colour))
        data.add_field(name="Region", value=str(server.region))
        data.add_field(name="Users", value="{}/{}".format(online, total_users))
        data.add_field(name="Text Channels", value=text_channels)
        data.add_field(name="Voice Channels", value=voice_channels)
        data.add_field(name="Roles", value=len(server.roles))
        data.add_field(name="Owner", value=str(server.owner))
        data.set_footer(text="Server ID: " + server.id)

        if server.icon_url:
            data.set_author(name=server.name, icon_url=server.icon_url)
            data.set_thumbnail(url=server.icon_url)
        else:
            data.set_author(name=server.name)
            print(data.to_dict())

        try:
            await self.bot.say(embed=data)
            print('test')
            
        except discord.HTTPException:
            await self.bot.say("I need the `Embed links` permission "
                               "to send this")

        
    @commands.command(pass_context=True,aliases=['ui','user'],description='See user-info of someone.')
    async def userinfo(self,ctx, user: discord.Member = None):
        '''See information about a user or yourself.'''
        server = ctx.message.server
        if user:
            pass
        else:
            user = ctx.message.author
        avi = user.avatar_url
        if avi:
            pass
        else:
            avi = user.default_avatar_url
        roles = sorted([x.name for x in user.roles if x.name != "@everyone"])
        if roles:
            roles = ', '.join(roles)
        else:
            roles = 'None'
        time = ctx.message.timestamp
        desc = '{0} is chilling in {1} mode.'.format(user.name,user.status)
        member_number = sorted(server.members,key=lambda m: m.joined_at).index(user) + 1
        em = discord.Embed(colour=0x00fffff,description = desc,timestamp=time)
        em.add_field(name='Nick', value=user.nick, inline=True)
        em.add_field(name='Member No.',value=str(member_number),inline = True)
        em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y'))
        em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y'))
        em.add_field(name='Roles', value=roles, inline=True)
        em.set_footer(text='User ID: '+str(user.id))
        em.set_thumbnail(url=avi)
        em.set_author(name=user, icon_url='http://site-449644.mozfiles.com/files/449644/logo-1.png')
        await self.bot.send_message(ctx.message.channel, embed=em)

    @commands.command(pass_context=True,aliases=['av','dp'])
    async def avatar(self,ctx, user: discord.Member = None):
        '''Returns ones avatar URL'''
        if user:
            pass
        else:
            user = ctx.message.author
        avi = user.avatar_url
        if avi:
            pass
        else:
            avi = user.default_avatar_url
        colour = ("#%06x" % random.randint(0, 0xFFFFFF))
        colour = int(colour[1:], 16)

        if user.nick is None:
            name = user.name
        else:
            name = user.nick
        em = discord.Embed(title=name, url=avi, color=colour)
        em.set_image(url=avi)
        await self.bot.say(embed=em)


    @commands.command(pass_context=True)
    async def info(self, ctx):
        """See bot information, uptime, servers etc."""
        uptime = (datetime.datetime.now() - self.bot.uptime)
        hours, rem = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(rem, 60)
        days, hours = divmod(hours, 24)
        if days:
            time_ = '%s days, %s hours, %s minutes, and %s seconds' % (days, hours, minutes, seconds)
        else:
            time_ = '%s hours, %s minutes, and %s seconds' % (hours, minutes, seconds)
        servers = len(self.bot.servers)
        version = '0.1.1'
        library = 'discord.py'
        creator = 'verix#7220'
        discord_ = '[Support Server](https://discord.gg/wkPy3sb)'
        github = '[/verixx/selfbot](https://github.com/verixx/selfbot)'
        time = ctx.message.timestamp
        emb = discord.Embed(colour=0x00FFFF)
        emb.set_author(name='selfbot-verix', icon_url=self.bot.user.avatar_url)
        emb.add_field(name='Version',value=version)
        emb.add_field(name='Library',value=library)
        emb.add_field(name='Creator',value=creator)
        emb.add_field(name='Servers',value=servers)
        emb.add_field(name='Github',value=github)
        emb.add_field(name='Discord',value=discord_)
        emb.add_field(name='Uptime',value=time_)
        emb.set_footer(text="ID: {}".format(self.bot.user.id))
        emb.set_thumbnail(url='https://cdn.discordapp.com/avatars/319395783847837696/349677f658e864c0a5247a658df61eb1.webp?width=80&height=80')
        await self.bot.say(embed=emb)

    @commands.command(pass_context=True)
    async def help(self, ctx, *, cmd = None):
        """Shows listed help message."""
        author = ctx.message.author
        pages = self.bot.formatter.format_help_for(ctx, self.bot, 3)
        n = 0
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

    @commands.command(pass_context=True)
    async def help2(self, ctx, *, cmd = None):
        """Shows paginated help message."""
        author = ctx.message.author
        pages = self.bot.formatter.format_help_for(ctx, self.bot, 1)
        testing = self.bot.get_channel('344184736324780032')
        pages2 = []
        n = 0
        for page in pages:
            # try:
            if(n!=0):
                page.set_author(name='', url='')
            if(n!=len(pages)-1):
                page.set_footer(text='')
            await self.bot.send_message(testing, embed=page)
            # await asyncio.sleep(.1)
            messages = []
            async for m in self.bot.logs_from(testing, limit=2):
                messages.append(m)
            message = messages[0]
            pages2.append(message)
            # except:
            #     await self.bot.say('I need the embed links perm.')

        msg = ''
        line = []
        for page2 in pages2:
            em = page2.embeds[0]

            # print('hi3')
            for x in em['fields']:
                line.append('**'+x['name']+'**') #append the cog heading
                # print('hi3.1')
                val = x['value']
                # print('hi3.2')
                val = val.split('\n')
                # print('hi3.3')
                line.extend(val)
            # print('hi3.4')

        p = Pages(self.bot, message=ctx.message, entries=line)
        p.embed.set_author(name='Help - Verix-Dino Selfbot Commands', icon_url=self.bot.user.avatar_url)
        p.embed.color = 0x00FFFF
        await p.paginate()


    @commands.command(pass_context=True)
    async def help3(self, ctx, *, cmd = None):
        """Shows paginated help message."""
        author = ctx.message.author
        pages = self.bot.formatter.format_help_for(ctx, self.bot, 1)
        testing = self.bot.get_channel('344184736324780032')
        pages2 = []
        n = 0
        for page in pages:
            try:
            # if(n!=0):
                # page.set_author(name='', url='')
            # if(n!=len(pages)-1):
                # page.set_footer(text='')
            # await self.bot.send_message(testing, embed=page)
            # await asyncio.sleep(.1)
            # messages = []
            # async for m in self.bot.logs_from(testing, limit=2):
            #     messages.append(m)
            # message = messages[0]
                message = page.to_dict()
                pages2.append(message)
            except:
                await self.bot.say('I need the embed links perm.')
        line = []
        for page2 in pages2:
            em = page2

            # print('hi3')
            print('hi3')
            for x in em['fields']:
                line.append('**'+x['name']+'**') #append the cog heading
                # print('hi3.1')
                val = x['value']
                # print('hi3.2')
                val = val.split('\n')
                # print('hi3.3')
                line.extend(val)
            # print('hi3.4')

        p = Pages(self.bot, message=ctx.message, entries=line)
        p.embed.set_author(name='Help - Verix-Dino Selfbot Commands', icon_url=self.bot.user.avatar_url)
        p.embed.color = 0x00FFFF
        await p.paginate()


        # p = Pages(self.bot, message=ctx.message, entries=pages)
        # p.embed.set_author(name='Help - Verix-Dino Selfbot Commands', icon_url=self.bot.user.avatar_url)
        # p.embed.color = 0x00FFFF
        # await p.paginate()




    # @commands.command(pass_context=True)
    # async def help4(self, ctx):
    #     await self.bot.delete_message(ctx.message)

    #     msg = open('cogs/utils/help.txt').read().replace('\\u200b','\u200b').splitlines()
    #     for m in msg:
    #         print(m)
    #     for i, line in enumerate(msg): 
    #         if line.strip().startswith('.'):
    #             x = line.strip().strip('.')
    #             x = ctx.prefix + x
    #             msg[i] = '`' + x + '`'
    #     for m in msg:
    #         print('newmsg:')
    #         print(m)
    #     print(msg)
    #     p = Pages(self.bot, message=ctx.message, entries=msg)
    #     p.embed.set_author(name='Help - Verix-Dino Selfbot Commands', icon_url=self.bot.user.avatar_url)
    #     p.embed.color = 0x00FFFF
    #     await p.paginate()

    @commands.command(pass_context=True)
    async def react(self, ctx, *args):
        """Add reactions to a message by message id.
        
        Add reactions to a specific message id
        [p]react 123456 :uwot: :lolno: :smile: 
        
        Add reactions to the last message in channel
        [p]react :uwot: :lolno: :smile:
        """
        server = ctx.message.server
        channel = ctx.message.channel

        if not len(args):
            await send_cmd_help(ctx)
            return

        has_message_id = args[0].isdigit()

        emojis = args[1:] if has_message_id else args
        message_id = args[0] if has_message_id else None
        if has_message_id:
            try:
                message = await self.bot.get_message(channel, message_id)
            except discord.NotFound:
                await self.bot.say("Cannot find message with that id.")
                return
        else:
            # use the 2nd last message because the last message would be the command
            messages = []
            async for m in self.bot.logs_from(channel, limit=2):
                messages.append(m)
            message = messages[1]

        useremojis = list(emojis)
        new_emojis = []
        
        for e in useremojis:
            lastlist = new_emojis
            for x in server.emojis:
                ename = e[e.find(':') + 1 : e.rfind(':')]
                # await self.bot.say("{} == {}".format(x.name, ename))
                if(x.name == ename):
                    new_emojis.append(x)
            if(lastlist == new_emojis):
                new_emojis.append(e)

         # await self.bot.say(len(new_emojis[0]))

        # await self.bot.say(message.id)
        # await self.bot.say('`{}`'.format(new_emojis))
        # await self.bot.say(type(server.emojis[0]))
        # await self.bot.add_reaction(message, server.emojis[0])
        for emoji in new_emojis:
            try:
                await self.bot.add_reaction(message, emoji)
            except discord.HTTPException:
                # reaction add failed
                pass
            except discord.Forbidden:
                await self.bot.say(
                    "I don’t have permission to react to that message.")
                break
            except discord.InvalidArgument:
                await self.bot.say("Invalid arguments for emojis")
                break

        await self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    async def next(self, ctx):
        '''go to next page in s.help'''
        await ctx.invoke(self.react, '▶')

    @commands.command(pass_context=True)
    async def back(self, ctx):
        '''go back a page in s.help'''
        await ctx.invoke(self.react, '◀')
        
    @commands.command(pass_context=True)
    async def i(self, ctx):
        '''go to info page in s.help'''
        await ctx.invoke(self.react, 'ℹ')
        
    @commands.command(pass_context=True)
    async def first(self, ctx):
        '''go to first page in s.help'''
        await ctx.invoke(self.react, '⏪')
        
    @commands.command(pass_context=True)
    async def last(self, ctx):
        '''go to last page in s.help'''
        await ctx.invoke(self.react, '⏩')
        
    @commands.command(pass_context=True)
    async def page(self, ctx):
        '''go to prev page in s.help'''
        await ctx.invoke(self.react, '🔢')
        
    @commands.command(pass_context=True)
    async def stop(self, ctx):
        '''stop the interactive help command'''
        await ctx.invoke(self.react, '⏹')




def setup(bot):
    bot.add_cog(Info(bot))