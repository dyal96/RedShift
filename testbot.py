import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
TOKEN = 'put your secret token here'
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

bot.run(TOKEN)
import discord
from discord.ext import commands

@bot.command(name='clear', help='Clears a specified number of messages from the chat.')
@commands.has_permissions(manage_messages=True)
async def clear_messages(ctx, num_messages: int):
    # Check if the number of messages to delete is within the limit
    if num_messages <= 0 or num_messages > 100:
        await ctx.send('Please provide a number between 1 and 100.')
        return
    
    # Delete the specified number of messages
    await ctx.channel.purge(limit=num_messages+1)
    await ctx.send(f'{num_messages} messages have been cleared.')
