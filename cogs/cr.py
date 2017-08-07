import discord
from ext.commands import bot
from ext import commands
import datetime
import time
import random
import asyncio
import json
import string
import aiohttp
from bs4 import BeautifulSoup
from __main__ import send_cmd_help

class ClashRoyale:

    def __init__(self, bot):
        self.bot = bot

#     @commands.command(pass_context=True)
#     async def cards(self,ctx):
#         """Shows the card names for reference."""
#         with open('cogs/utils/cards.json') as f:
#             cards = ', '.join(sorted(list(json.loads(f.read()).keys())))
#         await self.bot.say('**Card names for reference:**\n```bf\n{}```'.format(cards))

    # @commands.group(pass_context=True, invoke_without_command=True)
    # async def deck(self, ctx, usr: discord.Member = None):
    #     """See someone's deck."""
    #     user = ctx.message.author
    #     if usr: user = usr
    #     try:
    #         with open('cogs/utils/decks.json') as f:
    #             deck = json.loads(f.read())[user.id] # See if the user's deck is saved in decks.json
    #     except:
    #         await self.bot.say('*You need to set a deck. Do `.cards` to see exact spelling. Please follow this as a guideline:*\n\n `.deck set archers-11, thelog-2, graveyard-2, knight-11, infernotower-8, ewiz-2, poison-5, icegolem-8`')
    #     with open('cogs/utils/cards.json') as f:
    #         card_info = json.loads(f.read())

    #     fmt = ''

    #     choices = ['Did you know that you can do `.deck description` to change this message?','Did you know that you can do `.deck league` to change the thumbnail?']
    #     dyk = random.choice(choices)
    #     desc = deck.get('desc', dyk)
    #     desc = '*'+desc+'*'
    #     thumb = deck.get('thumbnail', 'http://site-449644.mozfiles.com/files/449644/logo-1.png?1483382330')

    #     for card, level in deck['cards'].items():
    #         fmt += '{}{} '.format(card_info[card], str(level))

    #     em = discord.Embed(color=0x00FFFF, description=desc)
    #     em.set_author(name=user.name, icon_url=user.avatar_url if user.avatar_url else user.default_avatar_url)
    #     em.add_field(name='Battle Deck', value=fmt)
    #     em.set_footer(text='SpikeBot')
    #     em.set_thumbnail(url=thumb)
    #     await self.bot.say(embed=em)

    # @deck.command(pass_context=True, aliases=['desc', 'info'])
    # async def description(self, ctx, *, desc : str):
    #     """Set your description."""
    #     user = ctx.message.author
    #     with open('cogs/utils/decks.json') as f:
    #         decks = json.loads(f.read())
    #         decks[user.id]['desc'] = desc
    #         decks = json.dumps(decks, indent=4, sort_keys=True)
    #     with open('cogs/utils/decks.json','w') as f:
    #         f.write(decks)
    #     await self.bot.say('Changed your deck description to: *{}*'.format(desc))

    # @deck.command(pass_context=True)
    # async def league(self, ctx, *, thumb: str = None):
    #     """Set your league."""
    #     user = ctx.message.author
    #     thumbnails = {
    #     'challenger 1':"https://www.deckshop.pro/img/league/Challenger-1.png",
    #     'challenger 2':"https://www.deckshop.pro/img/league/Challenger-2.png",
    #     'challenger 3':"https://www.deckshop.pro/img/league/Challenger-3.png",
    #     'master 1':"https://www.deckshop.pro/img/league/Master-1.png",
    #     'master 2':"https://www.deckshop.pro/img/league/Master-2.png",
    #     'master 3':"https://www.deckshop.pro/img/league/Master-3.png",
    #     'champion':"https://www.deckshop.pro/img/league/Champion.png",
    #     'grand champion':"https://www.deckshop.pro/img/league/Grand-Champion.png",
    #     'ultimate champion':"https://www.deckshop.pro/img/league/Ultimate-Champion.png",
    #     'default':'http://site-449644.mozfiles.com/files/449644/logo-1.png?1483382330'
    #     }

    #     if not thumb:
    #         await self.bot.say('```bf\n'+', '.join(sorted(thumbnails.keys()))+'```')
    #     else:
    #         with open('cogs/utils/decks.json') as f:
    #             decks = json.loads(f.read())
    #         decks[user.id]['thumbnail'] = thumbnails[thumb.lower().strip()]
    #         decks = json.dumps(decks, indent=4, sort_keys=True)
    #         with open('cogs/utils/decks.json', 'w') as f:
    #             f.write(decks)
    #         await self.bot.say('Set league to: {}'.format(thumb.lower().strip()))

    # @deck.command(pass_context=True, aliases=['make', 'create'])
    # async def set(self, ctx, *, cards : str):
    #     with open('cogs/utils/decks.json') as f:
    #         decks = json.loads(f.read())
    #     with open('cogs/utils/cards.json') as f:
    #         card_ls = json.loads(f.read())
    #     user = ctx.message.author
    #     data = {}
    #     data['cards'] = {}
    #     cards = cards.split(',')
    #     try:
    #         for card_info in cards:
    #             card, level = card_info.split('-')
    #             data['cards'][card.strip().lower()] = level.strip().lower()
    #             if int(level) > 13:
    #                 await self.bot.say('Max level for cards is 13.')
    #                 return
    #     except:
    #         await self.bot.say('*Incorrect formatting. Please refer to the guideline.*')
    #         return

    #     if len(data['cards']) != 8:
    #         await self.bot.say('Incorrect amount of cards.')
    #     else:
    #         flag = [card for card in data['cards'].keys() if card not in card_ls.keys()]
    #         if not flag:
    #             decks[user.id] = data
    #             await self.bot.say('Successfuly set your deck!')
    #         else:
    #             await self.bot.say('Spelling error in cards: `{}`'.format(', '.join(flag)))

    #     decks = json.dumps(decks, indent=4, sort_keys=True)

    #     with open('cogs/utils/decks.json', 'w') as f:
    #         f.write(decks)

    # def em_format(self,data,user = None):
    #     with open('cogs/utils/decks.json') as f:
    #         try:
    #             deck = json.loads(f.read())[user]
    #         except KeyError:
    #             deck = None
    #     with open('cogs/utils/cards.json') as f:
    #         card_info = json.loads(f.read())
    #     em = discord.Embed(color=0xFFFF)
    #     em.set_author(name=data['name']+' (#'+data['tag']+')',icon_url=data['clan_data']['badge'] if 'clan_data' in data else 'http://site-449644.mozfiles.com/files/449644/logo-1.png?1483382330')
    #     em.add_field(name='Clan',value=data['clan'])
    #     em.add_field(name='Current Trophies',value=data['c_trophies'])
    #     em.add_field(name='Highest Trophies',value=data['h_trophies'])
    #     em.add_field(name='Donations',value=data['donations'])
    #     em.add_field(name='Wins',value=data['wins'])
    #     em.add_field(name='Losses',value=data['losses'])
    #     em.add_field(name='Level',value=data['level'])
    #     em.add_field(name='3 crown wins',value=data['3c_wins'])
    #     try:
    #         val = float(int(data['wins'])/int(data['losses']))
    #         val = "{0:.2f}".format(val)
    #     except:
    #         val = None
    #     em.add_field(name='W/L Ratio',value=val)
    #     if 'chests' in data:
    #         em.add_field(name='Upcoming Chests',value=data['chests'][0])
    #         em.add_field(name='Chests Until',value=data['chests'][1])
    #     if deck:
    #         fmt = ''
    #         for card, level in deck['cards'].items():
    #             fmt += '{}{} '.format(card_info[card], str(level))
    #         em.add_field(name='Battle Deck',value=fmt)
    #     em.set_footer(text='KnightBot Async Stats | Data from StatsRoyale.com')

    #     return em

    # def parse_data(self,tag,stats):
    #     data = {}
    #     data['name'] = stats['username']
    #     data['level'] = stats['level']
    #     data['clan'] = stats['clan']
    #     data['c_trophies'] = stats['profile']['last_known_trophies']
    #     data['h_trophies'] = stats['profile']['highest_trophies'] if stats['profile']['highest_trophies'] else 'None'
    #     data['donations'] = stats['profile']['total_donations']
    #     data['wins'] = stats['profile']['wins']
    #     data['losses'] = stats['profile']['losses']
    #     data['3c_wins'] = stats['profile']['3_crown_wins']
    #     data['tag'] = tag
    #     data['clan_tag'] = stats['clan_tag']

    #     return data


#     @commands.command(pass_context=True)
#     async def stats(self, ctx, tag = None):
#         '''See your in-game statistics'''
#         with open('cogs/utils/stats.json') as f:
#             s_data = json.loads(f.read())
#         user = ctx.message.author
#         channel = ctx.message.channel
        
#         if tag is None:
#             if user.id in s_data.keys():
#                 data = s_data[user.id]
#                 em = self.em_format(data,user=user.id)
#                 await self.bot.say(embed=em)
#                 print('Data from json recieved successfully. \nSent Embed.')
#                 status = await self.async_refresh('http://statsroyale.com/profile/'+s_data[user.id]['tag']+'/refresh')
#                 print('Refreshing Data.\n')
#                 stat = await self.getProfile(data['tag'])
#                 chests = await self.getChestCycle(data['tag'])
#                 data = self.parse_data(data['tag'],stat)
#                 clan_tag = data['clan_tag']
#                 data_c = await self.getClan(clan_tag)
#                 data['clan_data'] = data_c
#                 data['chests'] = chests
#                 s_data[user.id] = data
#                 with open('cogs/utils/stats.json','w') as f:
#                     f.write(json.dumps(s_data, indent=4, sort_keys=True))

#             else:
#                 await self.bot.say('You don\'t have a saved tag. Do `.save #tag`')

#         elif '<@' in tag:
#             tag = tag.strip(string.punctuation)
#             if tag in s_data.keys():
#                 data = s_data[tag]
#                 em = self.em_format(data,user=tag)
#                 await self.bot.say(embed=em)
#                 status = await self.async_refresh('http://statsroyale.com/profile/'+s_data[user.id]['tag']+'/refresh')
#                 stat = await self.getProfile(data['tag'])
#                 chests = await self.getChestCycle(data['tag'])
#                 data = self.parse_data(data['tag'],stat)
#                 clan_tag = data['clan_tag']
#                 data_c = await self.getClan(clan_tag)
#                 data['clan_data'] = data_c
#                 data['chests'] = chests
#                 s_data[tag] = data
#                 with open('cogs/utils/stats.json','w') as f:
#                     f.write(json.dumps(s_data, indent=4, sort_keys=True))

#             else:
#                 await self.bot.say('That player doesn\'t have a saved tag.')
#         else:
#             tag = tag.strip('#').upper()
#             check = ['P', 'Y', 'L', 'Q', 'G', 'R', 'J', 'C', 'U', 'V', '0', '2', '8', '9']
#             if any(i not in check for i in tag):
#                 await self.bot.say('Should only contain these characters: `0, 2, 8, 9, P, Y, L, Q, G, R, J, C, U, V`')
#                 return
#             print('Valid Tag Check: Passed | Tag : {}'.format(tag))
#             stat = await self.getProfile(tag)
#             if stat == 'Profile Not Found':
#                 status = await self.async_refresh('http://statsroyale.com/profile/'+tag+'/refresh')
#                 await self.bot.say('Player Not Found. Attempting to add to System. Success: '+str(status['success']))
#             else:
#                 data = self.parse_data(tag,stat)   
#                 data['chests'] = await self.getChestCycle(tag)
#                 em = self.em_format(data)
#                 print('Data requested successfully.')
#                 try:
#                     await self.bot.say(embed=em)
#                     print('Embed Sent.')
#                 except:
#                     await self.bot.say('Cant send Embeds. Check Perms.')

    @commands.command(pass_context=True)
    async def save(self, ctx, tag = None):
        '''Save an ingame tag to your discord profile.'''
        user = ctx.message.author
        channel = ctx.message.channel
        with open('cogs/utils/stats.json') as f:
            s_data = json.loads(f.read())
        if tag is not None:
            tag = tag.strip('#').upper()
            check = ['P', 'Y', 'L', 'Q', 'G', 'R', 'J', 'C', 'U', 'V', '0', 'O', '2', '8', '9']
            if any(i not in check for i in tag):
                await self.bot.say('Should only contain these characters: `0, 2, 8, 9, P, Y, L, Q, G, R, J, C, U, V`')
                return
            stat = await self.getProfile(tag)
            if stat == 'Player Not Found':
                status = await self.async_refresh('http://statsroyale.com/profile/'+tag+'/refresh')
                await self.bot.say('Player Not Found. Attempting to add to System. Success: '+str(status['success']))
                data = self.parse_data(tag,stat)
                clan_tag = data['clan_tag']
                data_c = await self.getClan(clan_tag)
                if data_c == 'Clan Not Found':
                    status = await self.async_refresh('http://statsroyale.com/clan/'+clan_tag+'/refresh')
                    await self.bot.say('Clan Not Found. Attempting to add to System. Success: '+str(status['success']))
                else:
                    data['clan_data'] = data_c
                    data['chests'] = await self.getChestCycle(tag)
                    s_data[user.id] = data

                em = self.em_format(data,user.id)

                await self.bot.say('Successfully saved your data.')
            else:
                data = self.parse_data(tag,stat)
                clan_tag = data['clan_tag']
                data_c = await self.getClan(clan_tag)
                if data_c == 'Clan Not Found':
                    status = await self.async_refresh('http://statsroyale.com/clan/'+clan_tag+'/refresh')
                    await self.bot.say('Clan Not Found. Attempting to add to System. Success: '+str(status['success']))
                else:
                    data['clan_data'] = data_c
                    data['chests'] = await self.getChestCycle(tag)
                    s_data[user.id] = data

                em = self.em_format(data,user.id)

                await self.bot.say('Successfully saved your data.')
        else:
            status = await self.async_refresh('http://statsroyale.com/profile/'+s_data[user.id]['tag']+'/refresh')
            stat = await self.getProfile(s_data[user.id]['tag'])
            data = self.parse_data(s_data[user.id]['tag'],stat)
            clan_tag = data['clan_tag']
            data_c = await self.getClan(clan_tag)
            data['clan_data'] = data_c
            data['chests'] = await self.getChestCycle(s_data[user.id]['tag'])
            s_data[user.id] = data
            await self.bot.say('Successfully saved data.')

        with open('cogs/utils/stats.json','w') as f:
            f.write(json.dumps(s_data, indent=4, sort_keys=True))

#     @commands.command(pass_context=True)
#     async def clan(self,ctx,tag = None):
#         '''See clan information'''
#         with open('cogs/utils/stats.json') as f:
#             s_data = json.loads(f.read())
#         user = ctx.message.author

#         if tag is None:
#             if user.id in s_data:
#                 if 'clan_data' in s_data[user.id]:
#                     data = s_data[user.id]['clan_data']
#                     clan_tag = s_data[user.id]['clan_tag']
#                     data['clan_tag'] = clan_tag
#                     if clan_tag is None:
#                         await self.bot.say('You dont have a clan')
#                         return
#                     em = self.em_clan(data)
#                     await self.bot.say(embed=em)
#                     status = await self.async_refresh('http://statsroyale.com/clan/'+clan_tag+'/refresh')
#                     data = await self.getClan(clan_tag)
#                     s_data[user.id]['clan_data'] = data 
#                 else:    
#                     clan_tag = s_data[user.id]['clan_tag']
#                     if clan_tag is None:
#                         await self.bot.say('You dont have a clan')
#                     data = await self.getClan(clan_tag)
#                     data['clan_tag'] = clan_tag
#                     em = self.em_clan(data)
#                     await self.bot.say(embed=em)
#                     status = await self.async_refresh('http://statsroyale.com/clan/'+clan_tag+'/refresh')
#                     data = await self.getClan(clan_tag)
#                     s_data[user.id]['clan_data'] = data

#                 with open('cogs/utils/stats.json','w') as f:
#                     f.write(json.dumps(s_data,indent=4,sort_keys=True))

#             else:
#                 await self.bot.say('You don\'t have a saved tag. Do `.save #tag`')

#         elif '<@' in tag:
#             tag = tag.strip(string.punctuation)
#             if tag in s_data:
#                 if 'clan_data' in s_data[tag]:
#                     data = s_data[tag]['clan_data']
#                     data['clan_tag'] = s_data[tag]['clan_tag']
#                     if data['clan_tag'] is None:
#                         await self.bot.say('That player doesn\'t have a clan')
#                         return
#                     em = self.em_clan(data)
#                     await self.bot.say(embed=em)
#                     clan_tag = s_data[tag]['clan_tag']
#                     status = await self.async_refresh('http://statsroyale.com/clan/'+clan_tag+'/refresh')
#                     data = await self.getClan(clan_tag)
#                     s_data[tag]['clan_data'] = data
#                 else:
#                     clan_tag = s_data[tag]['clan_tag']
#                     if clan_tag is None:
#                         await self.bot.say('That player doesn\'t have a clan')
#                         return
#                     data = await self.getClan(clan_tag)
#                     data['clan_tag'] = clan_tag
#                     em = self.em_clan(data)
#                     await self.bot.say(embed=em)
#                     status = await self.async_refresh('http://statsroyale.com/clan/'+clan_tag+'/refresh')
#                     data = await self.getClan(clan_tag)
#                     s_data[tag]['clan_data'] = data
#             else:
#                 await self.bot.say('That player doesn\'t have a saved tag.')

#         else:
#             tag = tag.strip('#').upper()
#             check = ['P', 'Y', 'L', 'Q', 'G', 'R', 'J', 'C', 'U', 'V', '0', '2', '8', '9']
#             if any(i not in check for i in tag):
#                 await self.bot.say('Should only contain these characters: `0, 2, 8, 9, P, Y, L, Q, G, R, J, C, U, V`')
#                 return
#             data = await self.getClan(tag)
#             if data == 'Clan Not Found':
#                 status = await self.async_refresh('http://statsroyale.com/clan/'+tag+'/refresh')
#                 await self.bot.say('Clan Not Found. Attempting to add to System. Success: '+str(status['success']))
#                 data = await self.getClan(tag)
#                 data['clan_tag'] = tag
#                 em = self.em_clan(data)
#                 await self.bot.say(embed=em)
#             else:
#                 data['clan_tag'] = tag
#                 em = self.em_clan(data)
#                 await self.bot.say(embed=em)

#     @commands.command(pass_context=True)
#     async def chests(self, ctx, tag = None):
#         '''See basic chest cycle'''
#         with open('cogs/utils/stats.json') as f:
#             s_data = json.loads(f.read())
#         user = ctx.message.author

#         if tag is None:
#             if user.id in s_data:
#                 data = s_data[user.id]
#                 tag = data['tag']
#                 if 'chests' in data:
#                     em = self.em_chests(data, tag)
#                     await self.bot.say(embed=em)
#                     status = await self.async_refresh('http://statsroyale.com/profile/'+s_data[user.id]['tag']+'/refresh')
#                     stat = await self.getProfile(data['tag'])
#                     chests = await self.getChestCycle(data['tag'])
#                     data = self.parse_data(data['tag'],stat)
#                     clan_tag = data['clan_tag']
#                     data_c = await self.getClan(clan_tag)
#                     data['clan_data'] = data_c
#                     data['chests'] = chests
#                     s_data[user.id] = data
#                     with open('cogs/utils/stats.json','w') as f:
#                         f.write(json.dumps(s_data, indent=4, sort_keys=True))

#                 else:
#                     await self.bot.say('Do `.save` to update your config.')
#             else:
#                 await self.bot.say('You do not have a saved tag. Do `.save #tag`')
            
#         elif '<@' in tag:
#             tag = tag.strip(string.punctuation)
#             if tag in s_data:
#                 data = s_data[tag]
#                 tag = data['tag']
#                 if 'chests' in data:
#                     em = self.em_chests(data, tag)
#                     await self.bot.say(embed=em)
#                 else:
#                     await self.bot.say('Doesnt have any chests data.')
#             else:
#                 await self.bot.say('Player doesnt have a saved tag')

#         else:
#             tag = tag.strip('#').upper()
#             check = ['P', 'Y', 'L', 'Q', 'G', 'R', 'J', 'C', 'U', 'V', '0', '2', '8', '9']
#             if any(i not in check for i in tag):
#                 await self.bot.say('Should only contain these characters: `0, 2, 8, 9, P, Y, L, Q, G, R, J, C, U, V`')
#                 return
#             stat = await self.getProfile(tag)
#             if stat == 'Profile Not Found':
#                 status = await self.async_refresh('http://statsroyale.com/profile/'+tag+'/refresh')
#                 await self.bot.say('Player Not Found. Attempting to add to System. Success: '+str(status['success']))
#             else:
#                 data = self.parse_data(tag,stat)   
#                 data['chests'] = await self.getChestCycle(tag)
#                 em = self.em_chests(data, tag)
#                 try:
#                     await self.bot.say(embed=em)
#                 except:
#                     await self.bot.say('Invalid Stats.')


#     def em_chests(self, data, tag):
#         em = discord.Embed(color=0x00FFFF, description='Here you can see your chests and upcoming chests with 100% accuracy. Just make sure to refresh your profile.')
#         em.set_author(name=data['name']+' (#'+tag+')', icon_url=data['clan_data']['badge'] if 'clan_data' in data else 'http://site-449644.mozfiles.com/files/449644/logo-1.png?1483382330')
#         em.add_field(name='Upcoming Chests',value=data['chests'][0],inline=True)
#         em.add_field(name='Chests Until',value=data['chests'][1],inline=True)
#         # em.set_thumbnail(url='http://site-449644.mozfiles.com/files/449644/logo-1.png?1483382330').
#         em.set_footer(text='SpikeBot Async | Data from statsroyale.com')
#         return em



            

#     def em_clan(self, data):
#         em = discord.Embed(color=0x00FFFF,description=data['description'])
#         em.set_author(name=data['name']+' (#'+data['clan_tag']+')',icon_url=data['badge'])
#         em.add_field(name='Score',value=data['clan_trophies'])
#         em.add_field(name='Required Trophies',value=data['required_trophies'])
#         em.add_field(name='Donations/Week',value=data['donations_week'])
#         em.add_field(name='Members',value=data['members'])
#         em.set_thumbnail(url=data['badge'])
#         em.set_footer(text='KnightBot Async | Data from statsroyale.com')
#         return em

#     async def getChestCycle(self, tag):
#         with open('cogs/utils/cards.json') as f:
#             data = json.loads(f.read())
#         fmt = ''
#         fmt_2 = ''

#         soup = await self.async_get('http://statsroyale.com/profile/'+tag)
#         chests_queue = soup.find('div', {'class':'chests__queue'})
#         chests = chests_queue.find_all('div')
#         for chest in chests:
#             if 'chests__disabled' in chest['class'][-1]:
#                 continue # Disabled chests are those chest that player has already got.
#             elif 'chests__next' in chest['class'][-1]:
#                 fmt += '| ' + data[chest['class'][0][8:]] + ' | ' # class=chests__silver chests__next
#                 continue
#             elif 'chests__' in chest['class'][0]:
#                 chest_name = chest['class'][0][8:]
#                 counter=chest.find('span', {'class':'chests__counter'}).get_text()
#                 chest_ls = ['giant','magic','legendary','super','epic']
#                 if chest_name in chest_ls:
#                     if int(counter[1:]) < 7:
#                         fmt += '{}'.format(data[chest_name])
#                     else:
#                         fmt_2 += '{}{} '.format(data[chest_name],counter[1:])
#                 else:
#                     if int(counter[1:]) < 7:
#                         fmt += '{}'.format(data[chest_name])

#         return [fmt, fmt_2]



    async def async_get(self,url):
        async with aiohttp.get(url) as r:
            response = await r.text()
            soup = BeautifulSoup(response, 'html.parser')
            return soup

    async def async_refresh(self,url):
        async with aiohttp.get(url) as r:
            response = await r.json()
            return response


    async def getProfile(self,tag):
        try:
            stats = await self.getProfileBasic(tag)
        except:
            return 'Profile Not Found'
        soup = await self.async_get('http://statsroyale.com/profile/'+tag)

        stats[u'profile'] = {}
        profile = soup.find('div', {'class':'statistics__metrics'})
        for a in soup.find_all('a', {'class':'ui__link ui__mediumText statistics__userClan'},href=True):
            clan = a['href'].replace('/clan/','')
        try:
            stats['clan_tag'] = clan
        except:
            stats['clan_tag'] = None

        for div in profile.find_all('div', {'class':'statistics__metric'}):
            result = (div.find_all('div')[0].get_text().replace('\n', '')).lstrip().rstrip()
            try:
                result = int(result)
            except ValueError:
                pass
            item = div.find_all('div')[1].get_text().replace(' ', '_').lower()
            stats[u'profile'][item] = result

        return stats


    async def getProfileBasic(self,tag):
        soup = await self.async_get('http://statsroyale.com/profile/'+tag)
        basic = soup.find('div', {'class':'statistics__userInfo'})
        stats = {}
        level = basic.find('span', {'class':'statistics__userLevel'}).get_text()
        stats[u'level'] = int(level)
        username = basic.find('div', {'class':'ui__headerMedium statistics__userName'}).get_text()
        username = username.replace('\n', '')[:-3].lstrip().rstrip()
        stats[u'username'] = username
        clan = basic.get_text().replace(level, '').replace(username, '').lstrip().rstrip()
        if clan == 'No Clan':
            stats[u'clan'] = None
        else:
            stats[u'clan'] = clan

        return stats

    # async def getClan(self,tag):
    #     soup = await self.async_get('http://statsroyale.com/clan/'+tag)
    #     clan = {}
    #     try:
    #         title = soup.find('div', {'class':'ui__headerMedium clan__clanName'}).get_text()
    #     except:
    #         return 'Clan Not Found'
    #     clan[u'name'] = title.lstrip().rstrip()

    #     description = soup.find('div', {'class':'ui__mediumText'}).get_text()
    #     clan[u'description'] = description.lstrip().rstrip()

    #     img = soup.find('img',{'class':'clan__clanBadge'})
    #     badge = 'http://statsroyale.com'+img['src']
    #     clan['badge'] = badge

    #     members = soup.find_all('div',{'class':'clan__rowContainer'})
    #     count = str(len(members))+'/50'
    #     clan['members'] = count

    #     clan_stats = soup.find_all('div', {'class':'clan__metricContent'})

    #     for div in clan_stats:
    #         item = div.find('div', {'class':'ui__mediumText'}).get_text()
    #         item = item.replace('/', '_').replace(' ', '_').lower()
    #         result = div.find('div', {'class':'ui__headerMedium'}).get_text()
    #         result = int(result)
    #         clan[item] = result

    #     return clan





           

def setup(bot):
    bot.add_cog(ClashRoyale(bot))


