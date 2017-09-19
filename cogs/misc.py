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
from ext.utility import parse_equation
from ext.colours import ColorNames
from sympy import solve
from PIL import Image
import asyncio
import random
import emoji
import copy
import io
import aiohttp

class Misc:
    def __init__(self, bot):
        self.bot = bot
        self.emoji_converter = commands.EmojiConverter()


    def prepare_code(self, code):
        def map_left_bracket(b, p):
            return (b, find_bracket(code, p + 1, b))

        def map_right_bracket(b, p):
            offset = find_bracket(list(reversed(code[:p])), 0, ']')
            return (b, p - offset)

        def map_bracket(b, p):
            if b == '[':
                return map_left_bracket(b, p)
            else:
                return map_right_bracket(b, p)

        return [map_bracket(c, i) if c in ('[', ']') else c
                for c, i in zip(code, range(len(code)))]


    def read(self, string):
        valid = ['>', '<', '+', '-', '.', ',', '[', ']']
        return prepare_code([c for c in string if c in valid])


    def eval_step(self, code, data, code_pos, data_pos):
        c = code[code_pos]
        d = data[data_pos]
        step = 1
        output = None

        if c == '>':
            data_pos = data_pos + 1
            if data_pos > len(data):
                data_pos = 0
        elif c == '<':
            if data_pos != 0:
                data_pos -= 1
        elif c == '+':
            if d == 255:
                data[data_pos] = 0
            else:
                data[data_pos] += 1
        elif c == '-':
            if d == 0:
                data[data_pos] = 255
            else:
                data[data_pos] -= 1
        elif c == '.':
            output = (chr(d))
        elif c == ',':
            data[data_pos] = ord(stdin.read(1))
        else:
            bracket, jmp = c
            if bracket == '[' and d == 0:
                step = 0
                code_pos = jmp
            elif bracket == ']' and d != 0:
                step = 0
                code_pos = jmp

        return (data, code_pos, data_pos, step, output)

    def bfeval(code, data=[0 for i in range(9999)], c_pos=0, d_pos=0):
        outputty = None
        while c_pos < len(code):
            out = None
            (data, c_pos, d_pos, step, output) = eval_step(code, data, c_pos, d_pos)
            if outputty == None and output == None:
                c_pos += step
            elif outputty == None and out == None and output != None:
                outputty = ''
                out = ''
                out = out + output
                outputty = outputty + out
                c_pos += step
            elif out == None and output != None:
                out = ''
                out = out + output
                outputty = outputty + out
                c_pos += step
            else:
                c_pos += step
        return outputty

    @commands.command()
    async def bf(self, ctx, slurp:str):
       thruput = ctx.message.content
       preinput = thruput[5:]
       preinput2 = "\"\"\"\n" + preinput
       input = preinput2 + "\n\"\"\""
       code = read(input)
       output = bfeval(code)
       await ctx.send("Input:\n`{}`\nOutput:\n`{}`".format(preinput, output))

    @commands.command()
    async def animate(self, ctx, *, file):
        '''Animate a text file on discord!'''
        try:
            with open(f'data/anims/{file}') as a:
                anim = a.read().splitlines()
        except:
            return await ctx.send('File not found.')
        interval = anim[0]
        base = await ctx.send(anim[1])
        for line in anim[2:]:
            await base.edit(content=line)
            await asyncio.sleep(float(interval))

    @commands.command()
    async def virus(self, ctx, virus=None, *, user : discord.Member=None):
        '''
        Destroy someone's device with this virus command!
        '''
        virus = virus or 'discord'
        user = user or ctx.author
        with open('data/virus.txt') as f:
            animation = f.read().splitlines()
        base = await ctx.send(animation[0])
        for line in animation[1:]:
            await base.edit(content=line.format(virus=virus, user=user))
            await asyncio.sleep(random.randint(1, 4))

    @commands.command()
    async def react(self, ctx, index : int, *, reactions):
        '''React to a specified message with reactions'''
        history = await ctx.channel.history(limit=10).flatten()
        message = history[index]
        async for emoji in self.validate_emojis(ctx, reactions):
            await message.add_reaction(emoji)

    async def validate_emojis(self, ctx, reactions):
        '''
        Checks if an emoji is valid otherwise, 
        tries to convert it into a custom emoji
        '''
        for emote in reactions.split():
            if emote in emoji.UNICODE_EMOJI:
                yield emote
            else:
                try:
                    yield await self.emoji_converter.convert(ctx, emote)
                except commands.BadArgument:
                    pass

    @commands.command(aliases=['color', 'colour', 'sc'])
    async def show_color(self, ctx, *, color : discord.Colour):
        '''Enter a color and you will see it!'''
        file = io.BytesIO()
        Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
        file.seek(0)
        em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
        em.set_image(url='attachment://color.png')
        await ctx.send(file=discord.File(file, 'color.png'), embed=em)

    @commands.command(aliases=['dc','dominant_color'])
    async def dcolor(self, ctx, *, url):
        '''Fun command that shows the dominant color of an image'''
        await ctx.message.delete()
        color = await ctx.get_dominant_color(url)
        string_col = ColorNames.color_name(str(color))
        info = f'`{str(color)}`\n`{color.to_rgb()}`\n`{str(string_col)}`'
        em = discord.Embed(color=color, title='Dominant Color', description=info)
        em.set_thumbnail(url=url)
        file = io.BytesIO()
        Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
        file.seek(0)
        em.set_image(url="attachment://color.png")
        await ctx.send(file=discord.File(file, 'color.png'), embed=em)

    @commands.command()
    async def add(self, ctx, *numbers : int):
        '''Add multiple numbers together'''
        await ctx.send(f'Result: `{sum(numbers)}`')

    @commands.command()
    async def algebra(self, ctx, *, equation):
        '''Solve algabraic equations'''
        eq = parse_equation(equation)
        result = solve(eq)
        em = discord.Embed(
            color=discord.Color.green(),
            title='Equation', 
            description=f'```py\n{equation} = 0```',
            )
        em.add_field(name='Result', value=f'```py\n{result}```')
        await ctx.send(embed=em)

    @commands.group(invoke_without_command=True, name='emoji', aliases=['emote', 'e'])
    async def _emoji(self, ctx, *, emoji : str):
        '''Use emojis without nitro!'''
        emoji = emoji.split(":")
        if emoji[0] == "<" or emoji[0] == "":
            emo = discord.utils.find(lambda e: emoji[1] in e.name, ctx.bot.emojis)
        else:
            emo = discord.utils.find(lambda e: emoji[0] in e.name, ctx.bot.emojis)
        if emo == None:
            em = discord.Embed(title="Send Emoji", description="Could not find emoji.")
            em.color = await ctx.get_dominant_color(ctx.author.avatar_url)
            await ctx.send(embed=em)
            return
        async with ctx.session.get(emo.url) as resp:
            image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.message.delete()
            await ctx.send(file=discord.File(file, 'emoji.png'))

    @_emoji.command()
    async def copy(self, ctx, *, emoji : str):
        '''Copy an emoji from another server to your own'''
        emo = discord.utils.find(lambda e: emoji.replace(":","") in e.name, ctx.bot.emojis)
        em = discord.Embed()
        em.color = await ctx.get_dominant_color(ctx.author.avatar_url)
        if emo == None:
            em.title = 'Add Emoji'
            em.description = 'Could not find emoji.'
            await ctx.send(embed=em)
            return
        em.title = f'Added Emoji: {emo.name}'
        em.set_image(url='attachment://emoji.png')
        async with ctx.session.get(emo.url) as resp:
            image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(embed=em, file=discord.File(copy.deepcopy(file), 'emoji.png'))
            await ctx.guild.create_custom_emoji(name=emo.name, image=file.read())
    
    @commands.command()
    async def urban(self, ctx, *, search_terms : str):
        '''Searches Up a Term in Urban Dictionary'''
        search_terms = search_terms.split()
        definition_number = terms = None
        try:
            definition_number = int(search_terms[-1]) - 1
            search_terms.remove(search_terms[-1])
        except ValueError:
            definition_number = 0
        if definition_number not in range(0, 11):
            pos = 0
        search_terms = "+".join(search_terms)
        url = "http://api.urbandictionary.com/v0/define?term=" + search_terms
        async with ctx.session.get(url) as r:
            result = await r.json()
        emb = discord.Embed()
        emb.color = await ctx.get_dominant_color(url=ctx.message.author.avatar_url)
        if result.get('list'):
            definition = result['list'][definition_number]['definition']
            example = result['list'][definition_number]['example']
            defs = len(result['list'])
            search_terms = search_terms.split("+")
            emb.title = "{}  ({}/{})".format(" ".join(search_terms), definition_number+1, defs)
            emb.description = definition
            emb.add_field(name='Example', value=example)
        else:
            emb.title = "Search term not found."
        await ctx.send(embed=emb)
       
    @commands.group(invoke_without_command=True)
    async def lenny(self, ctx):
        """Lenny and tableflip group commands"""
	msg = f'Available: `{ctx.prefix}lenny face`, `{ctx.prefix}lenny shrug`, `{ctx.prefix}lenny tableflip`, `{ctx.prefix}lenny unflip`'
        await ctx.send(msg)
        
    @lenny.command()
    async def shrug(self, ctx):
        """Shrugs!"""
        await ctx.message.edit(content='¯\\\_(ツ)\_/¯')

    @lenny.command()
    async def tableflip(self, ctx):
        """Tableflip!"""
        await ctx.message.edit(content='(╯°□°）╯︵ ┻━┻')

    @lenny.command()
    async def unflip(self, ctx):
        """Unfips!"""
        await ctx.message.edit(content='┬─┬﻿ ノ( ゜-゜ノ)')

    @lenny.command()
    async def face(self, ctx):
        """Lenny Face!"""
        await ctx.message.edit(content='( ͡° ͜ʖ ͡°)')

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question = None):
        """Ask questions to the 8ball"""
        if question == None:
            ask_first = f'You need to ask me a yes/no question.\nUsage: `{ctx.prefix}eightball [yes/no question]`'
            emb = discord.Embed(colour=discord.Colour(0x2e1c1a), title='\N{BILLIARDS} Write question:')
            emb.description = ask_first
            await ctx.channel.send(embed=emb)
            return

        answerList = [  "It is certain, just relax and it will come/happen", 
                        "I have determined that, yes!", 
                        "Without a shred of doubt", 
                        "Yes definitely, no need to ask anymore for today", 
                        "You may rely on it", 
                        "As I see it... yes, don't worry about it anymore", 
                        "Most likely, but you have to take the first step", 
                        "Outlook is good, do your best!", 
                        "Yes", 
                        "Signs point to yes, but with some difficulty", 
                        "Hazy reply, try again after a cold shower", 
                        "Ask again later, for now try to relax and think about something else", 
                        "Better not tell you now, you'll me understand later", 
                        "Cannot predict now, ask anything else", 
                        "Concentrate, breathe, close your eyes and, ask again", 
                        "Don't count on it, better do something else", 
                        "My reply is no, have a nice day", 
                        "My imaginary friends say no, brb", 
                        "There might be problems, be ready", 
                        "Very doubtful, better don't get attached", 
                        "Never, just give up and be happy as you are", 
                        "Forget about it, turn on airplane mode and relax offline for a while", 
                        "乁( ⁰͡ Ĺ̯ ⁰͡ ) ㄏ who knows, who cares" ] 
        alaberga = random.randint(0, len(answerList)-1)
        ball_answer = f'{answerList[alaberga]}'
        emb = discord.Embed(title='\N{BILLIARDS} Your answer:')
        emb.colour = discord.Colour(0x2e1c1a)
        emb.description = ball_answer
        await ctx.channel.send(embed=emb)
 

def setup(bot):
	bot.add_cog(Misc(bot))
