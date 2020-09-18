import discord, pymongo, asyncio, colorama
from discord.ext import commands
from colorama import Fore, Style, init
from pymongo import MongoClient
"""Подключение к MongoDB"""

async def getprefix(bot, message):
	if not coll2.find_one({"guild_id": message.guild.id, "guild_name": str(message.guild.name)}): # проверка на присутствие префикса в бд
		coll2.insert_one({"guild_id": message.guild.id, "guild_name": str(message.guild.name), "prefix": "+"}) # если нет его там то он == +
	else:
		data = coll2.find_one({"guild_id": message.guild.id, "guild_name": str(message.guild.name)}) # если есть то берем его оттуда
		return data['prefix']

bot = commands.Bot(command_prefix=getprefix)

@bot.event
async def on_ready():
    print("logged in as {}".format(bot.user.name))
    
async def karochetambilbagietonadobilosdelatbvrode(ctx): #был какой-то там баг и это вроде помогло
    pass                                             #!
                                                     #!
@bot.command(aliases = ['префикс', 'pref', 'преф'])  #!
@commands.has_permissions( administrator = True )    #!
async def prefix(ctx, prefix = None):                #!
  await karochetambilbagietonadobilosdelatbvrode(ctx)#!
	if ctx.author.guild_permissions.administrator: #проверка на админку
		if prefix != None: # проверка введён ли префикс
			if len(prefix) < 2: # проверка длины префикса(нельзя больше 1 символа)
				coll2.update_one({"guild_id": ctx.guild.id, "guild_name": str(ctx.guild.name)}, {"$set":{"prefix": prefix}})#изменение префикса в бд
				embed_successful = discord.Embed(title=f"Вы успешно сменили префикс на: **``{prefix}``**", color=0xFF0000)
				await ctx.send(embed = embed_successful)
				print('--------------------------------')
				print(Fore.RED + '[log] ' + Style.RESET_ALL + f'prefix changed to {prefix} for guild {ctx.guild.name}')
				print(Fore.RED + '[log] ' + Style.RESET_ALL + f'префикс изменён на {prefix} в гильдии {ctx.guild.name}')
				print('--------------------------------')
			else:
				embederror = discord.Embed(title=f"Префикс не может быть **больше 1 символа**!", color=0xFF0000)
				await ctx.send(embed = embederror)
		else:
			embederror_none = discord.Embed(title=f"Вы не ввели префикс! **Используйте: {ctx.prefix}prefix <префикс>**", color=0xFF0000)
			await ctx.send(embed = embederror_none)
      
      
bot.run(token)
