import json
import discord
from ext import commands


def launch():
    config = open('cogs/utils/t_config.json').read()
    config = json.loads(config)
    print('-----------------------------------')
    print('Welcome to the KnightBot Launcher!')
    print('-----------------------------------')
    print('Please enter the following info: ')
    print('-----------------------------------')
    token = input('Bot Token \n> ')
    owner = input('Owner ID \n> ')
    print('-----------------------------------')
    print('-----------------------------------')
    config['bot']['token'] = token
    config['bot']['owner'] = owner
    config['bot']['opened'] = 1

    if input('Launch Bot?\n> ').lower() == 'yes':
        config = json.dumps(config, indent=4, sort_keys=True)
        with open('cogs/utils/t_config.json', 'w') as configfile:
            configfile.write(config)
        pass
    else:
        check()

def check():
    config = open('cogs/utils/t_config.json').read()
    config = json.loads(config)
    x = config['bot']['opened']
    if x == 0:
        x += 1
        config['bot']['opened'] = x
        launch()
    else:
        print('You have already set your configuration.')
        if input('Reset configuration?\n> ').lower() == 'yes':
            config['bot']['token'] = None
            config['bot']['owner'] = None
            config['bot']['opened'] = 0

            config = json.dumps(config, indent=4, sort_keys=True)

            with open('cogs/utils/t_config.json', 'w') as configfile:
                configfile.write(config)
            launch()
        else:
            pass


def bot():
    config = open("cogs/utils/t_config.json").read()
    config = json.loads(config)
    return config['bot']

def config():
    config = open("cogs/utils/t_config.json").read()
    config = json.loads(config)
    return config

def settings():
    config = open("cogs/utils/config.json").read()
    config = json.loads(config)
    return config





