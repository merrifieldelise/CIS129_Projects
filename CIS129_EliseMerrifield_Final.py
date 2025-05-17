#Author: Elise Merrifield
#CIS 129
#Final
#Code for a discord bot with the purpose of automatically moderating a server


import discord
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from discord server
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Event handler when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Event handler for message creation
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the message contains a bad word
    bad_words = ['badword1', 'badword2']  # Add your own list
    for word in bad_words:
        if word in message.content.lower():
            await message.delete()  # Delete the message
            await message.channel.send(f'{message.author.mention}, please refrain from using inappropriate language.')
            return

    # Process other commands
    await bot.process_commands(message)  # Allow command processing

# Start the bot
bot.run('YOUR_BOT_TOKEN')