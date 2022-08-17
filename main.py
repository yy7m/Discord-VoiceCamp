# Importing Modules.
from discord.ext import commands
import discord
from colorama import Fore

bot = commands.Bot("!", self_bot=True) # Defining bot.

@bot.event # Turning the bot online.
async def on_ready():
    print("This program has logged in to the account " + Fore.YELLOW + f"{bot.user}.\n")

@bot.command() # Join command.
async def join(ctx, voice_channel : discord.VoiceChannel):
    await voice_channel.connect()
    print(f"{Fore.GREEN}[-]{Fore.WHITE} Connected to {Fore.CYAN}{voice_channel} {Fore.WHITE}in {Fore.CYAN}{voice_channel.guild}{Fore.WHITE}.")
    await ctx.message.delete()

@bot.command() # Leave command.
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()
    print(f"{Fore.RED}[-]{Fore.WHITE} Disconnected from {Fore.CYAN}{voice_client.channel}{Fore.WHITE} in {Fore.CYAN}{ctx.message.guild}{Fore.WHITE}.")
    await ctx.message.delete()
    


bot.run("add_your_token_here", bot=False) # Run the bot by adding your token in between the quotes.