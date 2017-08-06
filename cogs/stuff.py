import discord
from discord.ext import commands
import datetime
import time
import random
import asyncio
import json
import requests
import os

class Stuff():


    def __init__(self, bot):
        self.bot = bot

    async def send_cmd_help(self,ctx):
        if ctx.invoked_subcommand:
            pages = self.bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
            for page in pages:
                await self.bot.send_message(ctx.message.channel, page)
        else:
            pages = self.bot.formatter.format_help_for(ctx, ctx.command)
            for page in pages:
                await self.bot.send_message(ctx.message.channel, page)

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
    async def edit(self, ctx, msg=None):
        '''edit your previous message 
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
        if msg == None:
            msg = message.content
        await self.bot.delete_message(ctx.message)
        await self.bot.edit_message(message, new_content=msg)

    @commands.command(pass_context=True)
    async def replace(self, ctx, old, new):
        '''replace one phrase to another in your previous message 
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



    
    
def setup(bot):
    bot.add_cog(Stuff(bot))