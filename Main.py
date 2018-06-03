# Import so that the bot could function
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import random
from random import randint
import Config
import datetime

#Determine the bots prefix
bot = commands.Bot(command_prefix = Config.PREFIX)

@bot.event
async def on_ready():
    print("===================================")
    print("Logged in as: %s"%bot.user.name)
    print("ID: %s"%bot.user.id)
    print('Server count:', str(len(bot.servers)))
    print('User Count:',len(set(bot.get_all_members())))
    print("Py Lib Version: %s"%discord.__version__)
    print("===================================")

@bot.command(pass_context=True)
async def ping(ctx):
    """Check The Bots Response Time"""
    t1 = time.perf_counter()
    await bot.send_typing(ctx.message.channel)
    t2 = time.perf_counter()
    thedata = (":ping_pong: **Pong.**\nTime: " + str(round((t2 - t1) * 1000)) + "ms")
    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    color = int(color, 16)
    data = discord.Embed(description = thedata, colour=discord.Colour(value = color))
    data.set_footer(text="{} | Requested by: {}".format(Config.BOTNAME, ctx.message.author))
    await bot.say(embed = data)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    """Shows information about the server"""
    server = ctx.message.server
    online = len([m.status for m in server.members
                    if m.status == discord.Status.online or
                    m.status == discord.Status.idle])
    total_users = len(server.members)
    text_channels = len([x for x in server.channels
                            if x.type == discord.ChannelType.text])
    voice_channels = len(server.channels) - text_channels
    passed = (ctx.message.timestamp - server.created_at).days
    created_at = ("Since {}. That's over {} days ago!"
                  "".format(server.created_at.strftime("%d %b %Y %H:%M"), passed))

    colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    colour = int(colour, 16)
    embed = discord.Embed(description = created_at, colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
    embed.add_field(name = "Region", value = str(server.region))
    embed.add_field(name = "Users Online", value = "{}/{}".format(online, total_users))
    embed.add_field(name = "Text Channels", value = text_channels)
    embed.add_field(name = "Voice Channels", value = voice_channels)
    embed.add_field(name = "Roles", value = len(server.roles))
    embed.add_field(name = "Owner", value = str(server.owner))
    embed.set_footer(text = "Server ID: " + server.id)
    embed.add_field(name = "AFK Timeout", value = "{} minutes".format(server.afk_timeout/60).replace(".0", ""))
    embed.add_field(name = "AFK Channel", value = str(server.afk_channel))
    embed.add_field(name = "Verification Level", value = str(server.verification_level))
    embed.set_footer(text= "{} | Requested by: {}".format(Config.BOTNAME, ctx.message.author))

    if server.icon_url:
        embed.set_author(name = server.name, url = server.icon_url)
        embed.set_thumbnail(url = server.icon_url)
    else:
        embed.set_author(name=server.name)

    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def count(ctx):
    """The amout of users/servers im in"""
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)

    colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    colour = int(colour, 16)
    embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
    embed.add_field(name = "Servers im in: ", value = servers)
    embed.add_field(name = "Users i have: ",value = users)
    embed.set_footer(text= "{} | Requested by: {} at".format(Config.BOTNAME, ctx.message.author))
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def roleinfo(ctx, *,role: discord.Role = None):
    """Info about a role"""
    if role == None:
        await bot.say(":x: | Role not found")
    else:
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        embed = discord.Embed(colour = discord.Colour(value = colour), timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Role Name", value = format(role.name))
        embed.add_field(name = "Role ID", value = format(role.id))
        embed.add_field(name = "For Server", value = format(role.server))
        embed.add_field(name = "Hoist", value = format(role.hoist))
        embed.add_field(name = "Role Position", value = format(role.position))
        embed.add_field(name = "Mentionable Role", value = format(role.mentionable))
        embed.add_field(name = "Role Created At", value = format(role.created_at))
        embed.set_footer(text= "{} | Requested by: {} at".format(Config.BOTNAME, ctx.message.author))
        await bot.say(embed = embed)

@bot.command(pass_context = True)
async def kick(ctx, member : discord.Member = None, *, reason = ""):
    '''Kick a user from the server with a reason'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" in user_roles:
        if member == None:
            await bot.say(":x: | Specify a user to `Kick`")

        if reason == "":
            await bot.say(":x: | You need a `Reason`")
        else:
            embed = discord.Embed(description = "{} was kicked.".format(member.name), color = 0xF00000)
            embed.add_field(name = "Reason: ", value = reason)
            embed.add_field(name = "Moderator:", value=ctx.message.author, inline = True)
            embed.set_footer(text = "{} | Kicked by: {}".format(Config.BOTNAME, ctx.message.author))
            await bot.kick(member)
            await bot.say(embed = embed)
            await bot.delete_message(ctx.message)
    else:
        await bot.say(":x: Your Not Admin!")

@bot.command(pass_context=True)
async def clear(ctx, number):
    '''Clears The Chat 2-100'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" in user_roles:
        mgs = []
        number = int(number)
        async for x in bot.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
        await bot.delete_messages(mgs)
    else:
        await bot.say(":x: Your Not Admin!")

@bot.command(pass_context = True)
async def warn(ctx, member: discord.Member = None, *, reason = ""):
    '''Warn a user with a reason (Admin Only)'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" in user_roles:
        if member == None:
            await bot.say(":x: | Please specify a `Member` to `Warn`")
        if reason == "":
            await bot.say(":x: | You must `Provide` a `Reason`")

        else:
            color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
            color = int(color, 16)
            embed = discord.Embed(title = "__**Warning**__", colour=discord.Colour(value=color), timestamp = datetime.datetime.utcnow())
            embed.add_field(name = "User: ", value = member, inline = True)
            embed.add_field(name="UserID: ", value = member.id, inline = True)
            embed.add_field(name="Reason: ", value = reason, inline = True)
            embed.add_field(name="Moderator:", value=ctx.message.author, inline=False)
            embed.set_footer(text= "{} | Warned by: {}".format(Config.BOTNAME, ctx.message.author))
            await bot.say(embed = embed)
            await bot.delete_message(ctx.message)
    else:
        await bot.say(":x: Your Not Admin!")

@bot.command(pass_context = True)
async def purge(ctx):
    """Clears the WHOLE channels History! (Admin Only)"""
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" in user_roles:
        await bot.say("Are you sure? This action can't be undone! yes or no?")
        response = await bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
        response = response.content.lower()
        if response == "yes":
            await bot.purge_from(ctx.message.channel, limit=99999)
        if response =="no":
            await bot.say("Purge Canceled")

    else:
        await bot.say(":x: Your Not Admin")

@bot.command(pass_context = True)
async def ban(ctx, user: discord.Member = None, *,reason = ""):
    """Bans a user from the server!"""
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" in user_roles:
        if user == None:
            await bot.say(":x: | Specify a `User` to `Ban`")
        if reason == "":
            await bot.say(":x: | Missing a `Reason` to `Ban`")
        else:
            color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
            color = int(color, 16)
            embed = discord.Embed(title = "__**User Ban**__", colour=discord.Colour(value=color), timestamp = datetime.datetime.utcnow())
            embed.add_field(name = "User: ", value = reason)
            embed.add_field(name="Moderator:", value=ctx.message.author, inline = True)
            embed.set_footer(text= "{} | Banned by: {}".format(Config.BOTNAME, ctx.message.author))
            await bot.say(embed = embed)
            await bot.ban(user)

    else:
        await bot.say(":x: Your Not Admin")

@bot.command(pass_context = True)
async def botinfo(ctx):
    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    color = int(color, 16)
    embed = discord.Embed(colour=discord.Colour(value=color), timestamp = datetime.datetime.utcnow())
    embed.add_field(name = "Creator: ", value = "Shutdown.py#2406")
    embed.add_field(name = "Want A Bot Like Me?", value = "[Click Here To Make Your Own](https://github.com/RageKickedGamer/Basic-Bot-Tutorial)")
    embed.set_footer(text= "{} | Requested by: {}".format(Config.BOTNAME, ctx.message.author))
    await bot.say(embed = embed)
    
bot.run(Config.TOKEN)

