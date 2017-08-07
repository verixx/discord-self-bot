import discord
from ext.commands import bot
from discord.ext import commands
import datetime
import time
import random
import asyncio
import json
import requests
import os
from bs4 import BeautifulSoup
from __main__ import send_cmd_help
import string
import aiohttp

class Stuff():


    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def test(self, ctx):
        em =  discord.Embed()
        em.set_image(url='https://www.youtube.com/watch?v=kLAjLORLMHk')
        await self.bot.say(embed=em)

    @commands.command(pass_context=True)
    async def sml(self, ctx):
        '''sml's emotions'''
        await self.bot.delete_message(ctx.message)
        await self.bot.say(":angry: :rage: :angry: :rage: :angry:\n"+ 
            ":rage: :angry: :rage: :angry: :rage:\n"+
            ":angry: :rage: :rage: :rage: :angry:\n"+
            ":rage: :angry: :rage: :angry: :rage:\n"+
            ":angry: :rage: :angry: :rage: :angry:")

    @commands.command(pass_context=True)
    async def dad(self, ctx):
        '''6dad's emotions'''
        await self.bot.delete_message(ctx.message)
        await self.bot.say(":6dad: :6dadw: :6dad: :6dadw: :6dad:\n"+
            ":6dadw: :6dad: :6dadw: :6dad: :6dadw:\n"+
            ":6dad: :6dadw: :rage: :6dadw: :6dad:\n"+
            ":6dadw: :6dad: :6dadw: :6dad: :6dadw:\n"+
            ":6dad: :6dadw: :6dad: :6dadw: :6dad:")

    @commands.command(pass_context=True)
    async def firepoop(self, ctx):
        '''fierypoopyhead's emotions'''
        await self.bot.delete_message(ctx.message)
        racfserv = self.bot.get_server('218534373169954816')
        gitgud = ''
        woodBM = ''
        for e in racfserv.emojis:
            if(e.name == 'gitgud'):
                gitgud = e
            if(e.name == 'woodBM'):
                woodBM = e
        await self.bot.say(":poop: :fire: :poop: :fire: :poop:\n:fire: {} :fire: {} :fire:\n:poop: :fire: {} :fire: :poop:\n:fire: {} :fire: {} :fire:\n:poop: :fire: :poop: :fire: :poop:".format(gitgud, gitgud, woodBM, gitgud, gitgud))

    @commands.command(pass_context=True)
    async def edit(self, ctx, *msg):
        '''edit your previous message 
        works up to 20 messages ago'''
        msg = list(msg)
        msg = ' '.join(msg)
        channel = ctx.message.channel
        # use the 2nd last message because the last message would be the command
        messages = []
        async for m in self.bot.logs_from(channel, limit=20):
            messages.append(m)
        for  m in messages[1:]:
            if m.author.id == ctx.message.author.id:
                message = m
                break
        if msg == None:
            msg = message.content
        print('{}')
        msg = msg.replace('{}', message.content)
        await self.bot.delete_message(ctx.message)
        await self.bot.edit_message(message, new_content=msg)

    @commands.command(pass_context=True)
    async def replace(self, ctx, old, *newphrase):
        '''replace one phrase to another in your previous message 
        works up to 20 messages ago'''
        new = list(newphrase)
        new = ' '.join(new)
        channel = ctx.message.channel
        # use the 2nd last message because the last message would be the command
        messages = []
        async for m in self.bot.logs_from(channel, limit=20):
            messages.append(m)
        for  m in messages[1:]:
            if m.author.id == ctx.message.author.id :
                message = m
                break
        msg =  message.content.replace(old, new)
        await self.bot.delete_message(ctx.message)
        await self.bot.edit_message(message, new_content=msg)

    @commands.command(pass_context=True)
    async def reverse(self, ctx):
        '''reverse your previous message 
        works up to 20 messages ago'''
        channel = ctx.message.channel
        # use the 2nd last message because the last message would be the command
        messages = []
        async for m in self.bot.logs_from(channel, limit=20):
            messages.append(m)
        for  m in messages[1:]:
            if m.author.id == '222925389641547776':
                message = m
                break

        await self.bot.delete_message(ctx.message)
        await self.bot.edit_message(message, new_content=message.content[::-1])

    clock_position = list(
        ['█',
         '██',
         '███',
         '████',
         '█████',
         '██████',
         '███████',
         '████████'
        ])

    @commands.command(pass_context=True)
    async def loadingbars(self, ctx, spins:int=1):
        '''make a  loading bar n times'''
        await self.bot.delete_message(ctx.message)
        channel = ctx.message.channel
        if spins>5:
            spins = 5
        if spins<1:
            spins = 1
        await self.bot.say(self.clock_position[0])
        messages = []
        async for m in self.bot.logs_from(channel, limit=20):
            messages.append(m)
        for  m in messages:
            if m.author.id == '222925389641547776':
                message = m
                break
        for i in range(0, spins):
            for x in range(0,7):
                await asyncio.sleep(.25)
                await self.bot.edit_message(message, new_content=self.clock_position[x])
        await self.bot.delete_message(message)

    @commands.command(pass_context=True)
    async def cycle(self, ctx):
        for x in range(1, 2):
            for i in string.digits:
                await self.bot.edit_message(ctx.message, i)

    @commands.command(pass_context=True)
    async def copy(self, ctx):
        channel = ctx.message.channel
        messages = []
        async for m in self.bot.logs_from(channel, limit=2):
            messages.append(m)
        message = messages[1]
        await self.bot.say('`'+str(message.embeds[0])+'`')

    @commands.command(pass_context=True)
    async def ecksdee(self, ctx):
        await self.bot.delete_message(ctx.message)
        await self.bot.say("ecĸѕ               ecĸѕ         dee dee\n  ecĸѕ            ecĸѕ          dee       dee\n     ecĸѕ     ecĸѕ             dee         dee\n            ecĸѕ                    dee          dee\n     ecĸѕ     ecĸѕ              dee         dee\n  ecĸѕ            ecĸѕ          dee       dee\necĸѕ               ecĸѕ         dee dee\n")
    
    @commands.command(pass_context=True)
    async def abe(self, ctx):
        # embed = [0, 1, 2, 3, 4]
        await self.bot.delete_message(ctx.message)
        embed  = discord.Embed(color=discord.Color(0x6441A4))
        embed.set_author(name="Follow Abe on Social Media!", icon_url="https://cdn.discordapp.com/avatars/218790601318072321/0b047729ae9b8d46f559b6b492ee66df.webp?size=1024")
        # embed.add_field(name='Link',value='[Google!](https://google.com/)')
        embed.add_field(name="Twitch!", value='[@abeplaysgame](https://www.twitch.tv/abeplaysgame)')
        embed.add_field(name="Twitter!", value='[@AbePlaysGame](https://twitter.com/AbePlaysGame)')
        embed.add_field(name="SnapChat!", value='[@AbeWantsFame](http://www.snapchat.com/add/AbeWantsFame)')
        embed.add_field(name="Share the Discord!", value='[NounVerbNoun](https://discord.gg/YbwWgnR)')
        embed.set_image(url='http://i.imgur.com/qmlqppD.png')
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def abe2(self, ctx):
        await self.bot.delete_message(ctx.message)
        em = discord.Embed(title="Like and RT abe's tweet about his hype RPL stream!",color=discord.Color(0x6441A4), url="https://cdn.discordapp.com/avatars/218790601318072321/0b047729ae9b8d46f559b6b492ee66df.webp?size=1024")
        em.set_author(name="ABE", icon_url="https://cdn.discordapp.com/avatars/218790601318072321/0b047729ae9b8d46f559b6b492ee66df.webp?size=1024")
        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/218790601318072321/0b047729ae9b8d46f559b6b492ee66df.webp?size=1024")
        await self.bot.say(embed=em)

    @commands.command(pass_context=True)
    async def flip(self, ctx, user):
        """Flips a coin... or a user.

        Defaults to coin.
        """
        if user != None:
            msg = ""
            char = "abcdefghijklmnopqrstuvwxyz"
            tran = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz"
            table = str.maketrans(char, tran)
            name = user.translate(table)
            char = char.upper()
            tran = "∀qƆpƎℲפHIſʞ˥WNOԀQᴚS┴∩ΛMX⅄Z"
            table = str.maketrans(char, tran)
            name = name.translate(table)
            await self.bot.say(msg + "(╯°□°）╯︵ " + name[::-1])
        else:
            await self.bot.say("*flips a coin and... " + choice(["HEADS!*", "TAILS!*"]))



    
def setup(bot):
    bot.add_cog(Stuff(bot))