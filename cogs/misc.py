import discord
from discord.ext import commands
from PIL import Image
import datetime
import time
import random
import asyncio
import json
import requests
import os
import aiohttp

class Misc():

    def __init__(self, bot):
        self.bot = bot
        self.ball = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
                     'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
                     'Reply hazy try again',
                     'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
                     'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good',
                     'Very doubtful']
        self.selfroles = ['Subscriber','Hype']

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
    async def embedsay(self,ctx, *, message: str = None):
        '''Embed something as the bot.'''
        color = ("#%06x" % random.randint(8, 0xFFFFFF))
        color = int(color[1:],16)
        color = discord.Color(value=color)
        if message:
            msg = ctx.message
            emb = discord.Embed(color=color,description=message)
            await self.bot.delete_message(msg)
            await self.bot.say(embed=emb)
        else:
            await self.bot.say('Usage: `.embedsay [message]`')


    @commands.command()
    async def add(self,*args):
        '''Add multiple numbers.'''
        ans = 0
        try:
            for i in args:
                ans += int(i)
            await self.bot.say(ans)
        except:
            await self.bot.say('Enter numbers only.')

    @commands.command(pass_context=True, aliases=['color'])
    async def colour(self, ctx, color : str):
        """Show a colour"""
        if len(color) == 7 and color.startswith("#"):
            hsh = 0
            red = color[hsh+1:hsh+3]
            green = color[hsh+3:hsh+5]
            blue = color[hsh+5:hsh+7]
        elif len(color) == 6:
            hsh = 0
            red = color[hsh:hsh+2]
            green = color[hsh+2:hsh+4]
            blue = color[hsh+4:hsh+6]

        try:
            col = (int(red,16),int(green,16),int(blue,16),255)
        except:
            return

        im = Image.new("RGBA", (200,200), col)
        im.save("color{}.png".format(ctx.message.author.id))
        im = open("color{}.png".format(ctx.message.author.id),"rb")
        await self.bot.send_file(ctx.message.channel,im,filename="colour.png",content="Showing color {}".format(color))
        im.close()
        os.remove("color{}.png".format(ctx.message.author.id))

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------


    @commands.command(pass_context=True)
    async def virus(self,ctx,user: discord.Member=None,*,hack=None):
        """Inject a virus into someones system."""
        name = ctx.message.author
        bar = ["[▓▓▓▓▓▓▓                ] -","[▓▓▓▓▓▓▓▓▓▓▓▓           ] \\","[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] |","[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] /","[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] -","[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \\","Injecting virus.   |","Injecting virus... -","Injecting virus....\\"]
        if not hack:
            hack = 'discord'
        else:
            hack = hack.replace(' ','_')
        channel = ctx.message.channel
        x = await self.bot.send_message(channel, '``[▓▓▓                    ] / {}-virus.exe Packing files.``'.format(hack))
        for count in range(6):
            await asyncio.sleep(1.5)
            await self.bot.edit_message(x,'``{} {}-virus.exe Packing files..``'.format(bar[count], hack))
        await asyncio.sleep(1)
        await self.bot.edit_message(x,'``Successfully downloaded {}-virus.exe``'.format(hack))
        await asyncio.sleep(2)
        for count in range(6,8):
            await self.bot.edit_message(x,'``{}``'.format(bar[count]))
            await asyncio.sleep(0.5)
        await self.bot.delete_message(x)
        await self.bot.delete_message(ctx.message)
        text = '**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'
        if user:
            if user == ctx.author:
                await self.bot.say('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(name.name))
            else:
                await self.bot.say('`{}-virus.exe` successfully injected into **{}**\'s system.'.format(hack,user.name))
                await self.bot.send_message(user, text.format(hack))
        else:
            await self.bot.say('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(name.name))


#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------


    @commands.command(pass_context=True, aliases=['8ball'])
    async def ball8(self, ctx, *, msg : str):
        """Let the 8ball decide your fate."""
        answer = random.randint(0, 19)

        if answer < 10:
            color = 0x008000
        elif 10 <= answer < 15:
            color = 0xFFD700
        else:
            color = 0xFF0000
        em = discord.Embed(color=color)
        em.add_field(name='\u2753 Question', value=msg)
        em.add_field(name='\ud83c\udfb1 8ball', value=self.ball[answer], inline=False)
        await self.bot.send_message(ctx.message.channel, content=None, embed=em)
        await self.bot.delete_message(ctx.message)




    @commands.command(pass_context=True, aliases=['emote','e'])
    async def emoji(self, ctx, *, msg):
        """
        Embed or copy a custom emoji (from any server).
        Usage:
        1) >emoji :smug: [Will display the smug emoji as an image]
        2) >emoji copy :smug: [Will add the emoji as a custom emote for the server]
        """
        copy_emote_bool = False
        if "copy " in msg:
            msg = msg.split("copy ")[1]
            copy_emote_bool = True
        if msg.startswith('s '):
            msg = msg[2:]
            get_server = True
        else:
            get_server = False
        msg = msg.strip(':')
        if msg.startswith('<'):
            msg = msg[2:].split(':', 1)[0].strip()
        url = emoji = server = None
        exact_match = False
        for server in self.bot.servers:
            for emoji in server.emojis:
                if msg.strip().lower() in str(emoji).lower():
                    url = emoji.url
                    emote_name = emoji.name
                if msg.strip() == str(emoji).split(':')[1]:
                    url = emoji.url
                    emote_name = emoji.name
                    exact_match = True
                    break
            if exact_match:
                break
        response = requests.get(emoji.url, stream=True)
        name = emoji.url.split('/')[-1]
        with open(name, 'wb') as img:

            for block in response.iter_content(1024):
                if not block:
                    break

                img.write(block)

        if url:
            try:
                if get_server:
                    await self.bot.send_message(ctx.message.channel,
                                                '**ID:** {}\n**Server:** {}'.format(emoji.id, server.name))
                with open(name, 'rb') as fp:
                    if copy_emote_bool:
                        e = fp.read()
                    else:
                        await self.bot.send_file(ctx.message.channel, fp)
                if copy_emote_bool:
                    try:
                        await self.bot.create_custom_emoji(ctx.message.server, name=emote_name, image=e)
                        embed = discord.Embed(title="Added new emote", color=discord.Color.blue())
                        embed.description = "New emote added: " + emote_name
                        await self.bot.say("", embed=embed)
                    except:
                        await self.bot.say("Not enough permissions to do this")
                os.remove(name)
            except:
                await self.bot.send_message(ctx.message.channel, url)
        else:
            await self.bot.send_message(ctx.message.channel, 'Could not find emoji.')

        return await self.bot.delete_message(ctx.message)

    @commands.command()
    async def urban(self, *, search_terms : str):
        '''Searches Up a Term in Urban Dictionary'''
        search_terms = search_terms.split(" ")
        global definition_number
        definition_number=0
        try:
            definition_number = int(search_terms[-1]) - 1
            search_terms.remove(search_terms[-1])
        except ValueError:
            definition_number = 0
        if definition_number not in range(0, 11):
            pos = 0
        search_terms = "+".join(search_terms)
        url = "http://api.urbandictionary.com/v0/define?term=" + search_terms
        async with aiohttp.get(url) as r:
            result = await r.json()
        if result["list"]:
            definition = result['list'][definition_number]['definition']
            example = result['list'][definition_number]['example']
            defs = len(result['list'])
            global terms
            search_terms = search_terms.split("+")
            terms=""
            for i in search_terms:
                terms += i
                terms += " "
            msg = ("{}\n\n**Example:\n**{}".format(definition, example))
            title = (terms + "  ({}/{})".format(definition_number+1, defs))
            emb = discord.Embed(color = discord.Color.blue(), title = title, description=msg)
            await self.bot.say(embed=emb)
        else:
            await self.bot.say("Your search terms gave no results.")

    @commands.command(pass_context=True)
    async def love(self, ctx, *, person : str):
        '''Loves a person'''
        spinner = ["|","/","-","\\","|","/","-","\\","|"]
        for count in range(9):
            await self.bot.edit_message(ctx.message, "`Calculating Love {}`".format(spinner[count]))
            await asyncio.sleep(0.2)
        await self.bot.say("", embed=discord.Embed(color=discord.Color.red(), title="Your love...", description="You love {} a whopping {}%!".format(person, random.randint(0, 100))))
        await self.bot.delete_message(ctx.message)

def setup(bot):
    bot.add_cog(Misc(bot))
