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
import time
import os
import itertools
import discord
from discord.ext import commands
from discord.ext.commands import Context
import cogs
from random import choice
import aiohttp
from collections import Counter
from __main__ import send_cmd_help

emojiletter={
    'a' : '🇦',
    'b' : '🇧',
    'c' : '🇨',
    'd' : '🇩',
    'e' : '🇪',
    'f' : '🇫',
    'g' : '🇬',
    'h' : '🇭',
    'i' : '🇮',
    'j' : '🇯',
    'k' : '🇰',
    'l' : '🇱',
    'm' : '🇲',
    'n' : '🇳',
    'o' : '🇴',
    'p' : '🇵',
    'q' : '🇶',
    'r' : '🇷',
    's' : '🇸',
    't' : '🇹',
    'u' : '🇺',
    'v' : '🇻',
    'w' : '🇼',
    'x' : '🇽',
    'y' : '🇾',
    'z' : '🇿',
    'a2': '<:a2:',
    'b2': '<:b2:',
    'c2': '<:c2:',
    'd2': '<:d2:',
    'e2': '<:e2:',
    'f2': '<:f2:',
    'g2': '<:g2:',
    'h2': '<:h2:',
    'i2': '<:i2:',
    'j2': '<:j2:',
    'k2': '<:k2:',
    'l2': '<:l2:',
    'm2': '<:m2:',
    'n2': '<:n2:',
    'o2': '<:o2:',
    'p2': '<:p2:',
    'q2': '<:q2:',
    'r2': '<:r2:',
    's2': '<:s2:',
    't2': '<:t2:',
    'u2': '<:u2:',
    'v2': '<:v2:',
    'w2': '<:w2:',
    'x2': '<:x2:',
    'y2': '<:y2:',
    'z2': '<:z2:'
}
channel_name_to_id = {
    'general'    : '291126049268563968',
    'botspam'    : '340737442367799297',
    'cr'         : '291128641335853056',
    'streamclips': '292351030971334658',
    'memes'      : '302615325390798849',
    'gaschamber' : '340368355754115074',
    'botdev'     : '340372201578430467'
}



class React:

    def __init__(self, bot):
        """Constructor."""
        self.bot = bot

    # async def send_cmd_help(self,ctx):
    #     if ctx.invoked_subcommand:
    #         pages = self.bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
    #         for page in pages:
    #             await self.bot.send_message(ctx.message.channel, page)
    #     else:
    #         pages = self.bot.formatter.format_help_for(ctx, ctx.command)
    #         for page in pages:
    #             await self.bot.send_message(ctx.message.channel, page)

    @commands.command(pass_context=True)
    async def reactchan(self, ctx, chan, *args):
        """Add reactions to a message by channel.
        
        Add reactions to a specific message id
        [p]addreactchan general :uwot: :lolno: :smile: 
        """
        server = ctx.message.server
        try:
            channel_id = channel_name_to_id[chan]
        except:
            await self.bot.say("invalid channel, channels are:")
            y = ''
            for x in channel_name_to_id:
                y = y + x +', '
            y = y[:-2]
            await self.bot.say(y)
            return

        message = ctx.message
        server2 = ctx.message.server
        dinoserver = self.bot.get_server('264119826069454849') #dino's test server
        abeserver = self.bot.get_server('291126049268563968')
        channel = abeserver.get_channel(channel_id)
        #abe's server's general channel

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
            message = messages[0]
        # await self.bot.say(emojis)

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

        # await self.bot.say(message.id)
        # await self.bot.say(type(emojis[0]))
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
    async def reactwordchan(self, ctx, chan, word):
        '''react to previous message with any word given. because you can only react with each
        emoji once, if two or more of the same letter are given  it will ignore anything after
        the first of those letters.
        syntax:
        [p]reactword hi

        if you do [p]reactword lolollollolol
        it will onlt react with  one of each l and o emojis
        '''
        try:
            channel_id = channel_name_to_id[chan]
        except:
            await self.bot.say("invalid channel, channels are:")
            y = ''
            for x in channel_name_to_id:
                y = y + x +', '
            y = y[:-2]
            await self.bot.say(y)
            return

        message = ctx.message
        server2 = ctx.message.server
        dinoserver = self.bot.get_server('264119826069454849') #dino's test server
        abeserver = self.bot.get_server('291126049268563968')
        channel = abeserver.get_channel(channel_id)
        #abe's server's general channel
        
        word = map(lambda x:x.lower(),word)
        
        messages = []
        async for m in self.bot.logs_from(channel, limit=2):
            messages.append(m)
        message = messages[0]
        i = 0
        word2 = []
        for l in word:
            word2.append(l)

        counts = Counter(word2) # so we have: {'name':3, 'state':1, 'city':1, 'zip':2}
        for s,num in counts.items():
            if num > 1: # ignore strings that only appear once
                for suffix in range(1, num + 1): # suffix starts at 1 and increases by 1 each time
                        word2[word2.index(s)] = s + str(suffix) # replace each appearance of s
        for i, item in enumerate(word2):
            if ('2' not in word2[i]):
                word2[i]= str(word2[i])[0]

        word2 = list(map(lambda l: emojiletter[l], word2))
        # await self.bot.say(word2)

        new_emojis = []
        server = self.bot.get_server('264119826069454849')
        for e in word2:
            lastlist = new_emojis
            for x in server.emojis:
                ename = e[e.find(':') + 1 : e.rfind(':')]
                # await self.bot.say("{} == {}".format(x.name, ename))
                if(x.name == ename):
                    new_emojis.append(x)
            if(lastlist == new_emojis and ('<:' not in e)):
                new_emojis.append(e)
        # await self.bot.say(new_emojis)

        # await self.bot.say(word2)

        # for i, item in enumerate(word2):
        #     await self.bot.say(len(word2[i]))
        #     if(len(word2[i])!=1 and word2[i] != str(word2[i])[0]+'2'):
        #         await self.bot.say("wow")
        #         word2[i] = str(word2[i])[0]
        i = 0
        # await self.bot.say(word2)
        try:
            for l in new_emojis:
                if i<20:
                    # await self.bot.say('`{}`'.format(l))
                    await self.bot.add_reaction(message, l)
                    i = i + 1
            if(i==20):
                await self.bot.say("reaction emoji limit(20) reached")
                messages = []
                async for m in self.bot.logs_from(channel, limit=2):
                    messages.append(m)
                message = messages[0]
                time.sleep(2)
                await self.bot.delete_message(message)



        except:
            await self.bot.say("Invalid text, must be only alphabetic")
        await self.bot.delete_message(ctx.message)



    @commands.command(pass_context=True, no_pm=True)
    async def react(self, ctx, *args):
        """Add reactions to a message by message id.
        
        Add reactions to a specific message id
        [p]addreation 123456 :uwot: :lolno: :smile: 
        
        Add reactions to the last message in channel
        [p]addreation :uwot: :lolno: :smile:
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
    async def reactnoid(self, ctx, *args):
        """Add reactions to a message by message id.
        
        Add reactions to a specific message id
        [p]addreation 123456 :uwot: :lolno: :smile: 
        
        Add reactions to the last message in channel
        [p]addreation :uwot: :lolno: :smile:
        """
        server = ctx.message.server
        channel = ctx.message.channel

        if not len(args):
            await send_cmd_help(ctx)
            return


        emojis =  args
        # use the 2nd last message because the last message would be the command
        messages = []
        async for m in self.bot.logs_from(channel, limit=2):
            messages.append(m)
        message = messages[1]
        # await self.bot.say(emojis)

        useremojis = list(emojis)
        new_emojis = []
        
        for e in useremojis:
            lastlist = new_emojis
            for x in server.emojis:
                ename = str(e)[str(e).find(':') + 1 : str(e).rfind(':')]
                # await self.bot.say("{} == {}".format(x.name, ename))
                if(x.name == ename):
                    new_emojis.append(x)
            if(lastlist == new_emojis):
                new_emojis.append(str(e))

        # await self.bot.say(message.id)
        # await self.bot.say(type(emojis[0]))
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


    async def reactbefore(self, message, *emoji):
        # messages = []
        # async for m in self.bot.logs_from(ctx.message.channel, limit=2):
        #     messages.append(m)
        # message = messages[1]
        for e in emoji:
            await self.bot.add_reaction(message, e)

        
    @commands.command(pass_context=True)
    async def reactwordold(self, ctx, word):
        '''react to previous message with any word given. because you can only react with each
        emoji once, if two or more of the same letter are given  it will ignore anything after
        the first of those letters.
        syntax:
        [p]reactword hi

        if you do [p]reactword lolollollolol
        it will onlt react with  one of each l and o emojis
        '''
        messages = []
        async for m in self.bot.logs_from(ctx.message.channel, limit=2):
            messages.append(m)
        message = messages[1]
        i = 0
        try:
            for l in word:
                if i<20:
                    await self.reactbefore(message, emojiletter[l])
                    i = i + 1
            if(i==20):
                await self.bot.say("reaction emoji limit(20) reached")
                messages = []
                async for m in self.bot.logs_from(ctx.message.channel, limit=2):
                    messages.append(m)
                message = messages[0]
                time.sleep(2)
                await self.bot.delete_message(message)



        except:
            await self.bot.say("Invalid text, must be only alphabetic")
        await self.bot.delete_message(ctx.message)



    @commands.command(pass_context=True)
    async def reactword(self, ctx, word):
        '''react to previous message with any word given. because you can only react with each
        emoji once, if two or more of the same letter are given  it will ignore anything after
        the first of those letters.
        syntax:
        [p]reactword hi

        if you do [p]reactword lolollollolol
        it will onlt react with  two of each l and o emojis
        '''

        word = map(lambda x:x.lower(),word)
        
        messages = []
        async for m in self.bot.logs_from(ctx.message.channel, limit=2):
            messages.append(m)
        message = messages[1]
        i = 0
        word2 = []
        for l in word:
            word2.append(l)

        counts = Counter(word2) # so we have: {'name':3, 'state':1, 'city':1, 'zip':2}
        for s,num in counts.items():
            if num > 1: # ignore strings that only appear once
                for suffix in range(1, num + 1): # suffix starts at 1 and increases by 1 each time
                        word2[word2.index(s)] = s + str(suffix) # replace each appearance of s
        for i, item in enumerate(word2):
            if ('2' not in word2[i]):
                word2[i]= str(word2[i])[0]

        word2 = list(map(lambda l: emojiletter[l], word2))
        # await self.bot.say(word2)

        new_emojis = []
        server = self.bot.get_server('264119826069454849')
        for e in word2:
            lastlist = new_emojis
            for x in server.emojis:
                ename = e[e.find(':') + 1 : e.rfind(':')]
                # await self.bot.say("{} == {}".format(x.name, ename))
                if(x.name == ename):
                    new_emojis.append(x)
            if(lastlist == new_emojis and ('<:' not in e)):
                new_emojis.append(e)
        # await self.bot.say(new_emojis)

        # await self.bot.say(word2)

        # for i, item in enumerate(word2):
        #     await self.bot.say(len(word2[i]))
        #     if(len(word2[i])!=1 and word2[i] != str(word2[i])[0]+'2'):
        #         await self.bot.say("wow")
        #         word2[i] = str(word2[i])[0]
        i = 0
        # await self.bot.say(word2)
        try:
            for l in new_emojis:
                if i<20:
                    # await self.bot.say('`{}`'.format(l))
                    await self.bot.add_reaction(message, l)
                    i = i + 1
            if(i==20):
                await self.bot.say("reaction emoji limit(20) reached")
                messages = []
                async for m in self.bot.logs_from(ctx.message.channel, limit=2):
                    messages.append(m)
                message = messages[0]
                time.sleep(2)
                await self.bot.delete_message(message)



        except:
            await self.bot.say("Invalid text, must be only alphabetic")
        await self.bot.delete_message(ctx.message)


    @commands.command(pass_context=True)
    async def example(self, ctx):
        '''reacts previous message with d, a, m, n emojis'''
        await ctx.invoke(self.reactword, 'example')


def setup(bot):
    r = React(bot)
    bot.add_cog(r)