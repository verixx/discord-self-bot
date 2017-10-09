import discord
import asyncio
import logging
import urllib
import os
import sys
import datetime
import pip
import subprocess
import re
import io
from contextlib import redirect_stdout
from urllib.request import urlretrieve
client = discord.Client()

@client.event
async def on_ready():
    print('\033[34m' + '[==================================]' + '\033[39m')
    print('\033[35m' + '|' + '\033[36m' + ' v0.0.1'+ '\033[39m')
    print('\033[35m' + '|' + '\033[33m' + ' Logged in as:',client.user.name)
    print('\033[35m' + '|' + '\033[33m' + ' UID:',client.user.id) 
    print('\033[35m' + '|' + '\033[33m' + ' Discord version:',discord.version_info)
    print(' ')
    print('\033[35m' + '|' + '\033[33m' + ' Use ' + '\033[36m' + 'Control + C ' + '\033[33m' + 'to exit.'+ '\033[39m')
    print('\033[35m' + '|' + '\033[36m' + ' elijah'+ '\033[39m')
    print('\033[34m' + '[==================================]' + '\033[39m')
    print('\033[35m' + '|' + '\033[36m' + ' Connected to:'+ '\033[39m')
    for server in client.servers:
        print('\033[35m' + '-', server.name)
    print('\033[34m' + '[==================================]' + '\033[39m')

@client.event
async def on_message(message):
    if message.author == client.user:
        # MAKES A LIST WITH THE COMMAND ATRIBUTES
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index+1
        commands.append(message.content[z:])
        if message.content.startswith('roles'):
            await client.delete_message(message)
            get_tagged = []
            for role in message.server.role_hierarchy:
                get_tagged.append(role.mention)
            chunks = [get_tagged[x:x+87] for x in range(0, len(get_tagged), 87)]
            for chunk in chunks:
                msg = await client.send_message(message.channel," ".join(chunk))
                await client.delete_message(msg)
        if message.content.startswith('members'):
            await client.delete_message(message)
            get_tagged = []
            for member in message.server.members:
                get_tagged.append(member.mention)
            chunks = [get_tagged[x:x+87] for x in range(0, len(get_tagged), 87)]
            for chunk in chunks:
                msg = await client.send_message(message.channel," ".join(chunk))
                await client.delete_message(msg)
        if commands[0] == 'twit':
            await client.send_message(message.channel,"https://twitter.com/sadboysloI")
        if commands[0] == 'idle':
            await client.change_presence(status=discord.Status.idle)
        if commands[0] == 'dnd':
            await client.change_presence(status=discord.Status.dnd)
        if commands[0] == 'on':
            await client.change_presence(status=discord.Status.online)
        if commands[0] == 'in':
            await client.change_presence(status=discord.Status.invisible)
        if commands[0] == 'nick':
            await client.change_nickname(message.author, "p")
        if commands[0] == 'reset':
            await client.change_nickname(message.author, "pluzio")
        if commands[0] == 'cl':
            if len(commands) == 1:
                async for msg in client.logs_from(message.channel,limit=9999):
                    if msg.author == client.user:   
                        try:
                            await client.delete_message(msg)
                        except Exception as x:
                            pass
            elif len(commands) == 2:
                user_id = ''
                for channel in client.private_channels:
                    if commands[1] in str(channel):
                        if str(channel.type) == 'private':
                            user_id = str(channel.id)
                async for msg in client.logs_from(discord.Object(id=user_id),limit=9999):
                    if msg.author == client.user:
                        try:
                            await client.delete_message(msg)
                        except Exception as x:
                            pass
        if message.content.startswith('cum'):
            if len(commands) == 2:
                memberz = []
                for member in message.server.members:
                    memberz.append(member)
                for member in memberz:
                    if str(member.mention) in commands[1]:
                        k = ("""
:ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        x = ("""
:ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        a = ("""
:ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        b = ("""
:ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:                
                                                  %s      
                        """ % (member.mention))
                        c = ("""
:ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        d = ("""
:ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        e = ("""
:ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        f = ("""
:ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        t = ("""
:ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
                                                  %s      
                        """ % (member.mention))
                        g = ("""
:ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
                                                  %s      
                        """ % (member.mention))
                        string = [k,a,b,c,d,e,f,t,g]
                        for z in string:
                            await client.edit_message(message,z)
                            await asyncio.sleep(.3)
                await client.delete_message(message)

    if message.content.startswith(".//nick"):
        while True :
            await client.change_nickname(message.author, "emily")
            await asyncio.sleep(.1)
            await client.change_nickname(message.author, "is")
            await asyncio.sleep(.1)
            await client.change_nickname(message.author, "gay")

    if message.content.startswith('.cmds'):
        embed = discord.Embed(title="Commands", description="***STATUS*** :crystal_ball:\n* *on* - changes status to **online**\n* *idle* - changes status to **idle**\n* *dnd* - changes status to **dnd**\n* *in* - changes status to **invisible**\n\n***GENERAL***:tools:\n* cum <@/userid>* - do it\n* *nick* - changes your nick to **j**\n* *reset* - resets your nick to **default**\n* *cl* - prunes messages.\n* *twit* - sends msg of tweeter dot com username.\n* *nick* - changes nickname to whatever.\n* *roles* - tags every role in a server haha.\n* *members* - tags every member in a server. *prob gon get auto banned*", color=0xC02727)
        embed.set_author(name="2327#2327", icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed)

client.run("TOKEN", bot=False)
