import discord
from discord.ext import commands
from discord.ext.commands import slash_command


class hola(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        self.bot = bot
        
    
    @slash_command(name = 'hola', description = '😃 Te saludo!')
    async def hola (self, interaction : discord.Interaction):
        
        return await interaction.response.send_message(content= f'Hola papi {interaction.user.mention}')
    
    
def setup (bot : commands.Bot):
    bot.add_cog(hola(bot))    
        