import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '-')
Client.discord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hello, welcome!')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='searching melk | -help'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '-ping':
        await client.send_message(message.channel,'Pong!')

    if message.content == '-melk':
        em = discord.Embed(description='')
        em.set_image(url='https://www.google.com/search?q=melk&client=firefox-b-ab&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjc7pPH5KXdAhUFjSwKHe61AXkQ_AUICygC&biw=1920&bih=966#imgrc=e76PnTMuHfTb-M:')
        await client.send_message(message.channel, embed=em)

    if message.content == '-help':
        await client.send_message(message.channel,'Hey there! Im Melk - a fun bot created by @ProLessSkill#7393 | -melk = show some melk | -ping = pong! | -support = Join Melk Support Server | -russia = No explonation needed. | More commands coming!')

    if message.content == '-support':
        await client.send_message(message.channel,'Support server is cuuently unavailable.')

    if message.content == '-dailymelkdose':
        await client.send_message(message.channel,'The recommended Melk dose is 5 Cups of Melk a day.')

    if message.content == '-russia':
        await client.send_message(message.channel,'Here: https://www.youtube.com/watch?v=y90yaLFoYoA')


    if message.content.startswith('-quote'):
        randomlist = ['I know that I am stupid but when I look around me I feel a lot better','On the internet you can be whatever you want. Its weird that so many people choose to be stupid','If it doesnt challenge you it wont change you.',]
        await client.send_message(message.channel,(random.choice(randomlist)))

    if message.content == '-croatia':
        await client.send_message(message.channel,'Here you are sir/ma: https://www.youtube.com/watch?v=QECanycriX0')

    if message.content == 'melk':
        await client.send_message(message.channel,'yo boi Melk here!!')
client.run('NDg2NDg1MzAxMzEzNjY3MDgy.DnJogA.blmb_LDBW5LGGoI6pOrM-1uEtzg')
