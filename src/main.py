import discord
from discord.ext import commands
import json


with open("src/backend.json", "r") as config:
    
    data = json.load(config)
    
    token = data['token']
    

bot = commands.Bot(
        
    intents = discord.Intents.all(),
    status = discord.Status.idle,
    activity = discord.Game(name= 'Template by Devcheck#4611')
        
)
    
#Engranajes


engranajes = {
    
    'Comandos.hola'
    
}    

if __name__ in '__main__':
    
    for command in engranajes:
        
        print(f'Lista de Comandos: {command}')
        
        try:
            
            bot.load_extension(command)
            
        except Exception as E:
            
            print(f'Exploto el comando {E}') 
            

@bot.event
async def on_ready():
    
    #Sincroniza los comandos
    await bot.sync_commands()
    print('Se incio el bot {}'.format(bot.user))

bot.run(token)               
    