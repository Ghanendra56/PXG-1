import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='=')

#Hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def greet(ctx, member: discord.Member):
    await ctx.send(f'Hello {member.mention}')

@bot.command()
async def info(ctx):
    await ctx.send('This is a bot made by SyntaxError')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)

@bot.command()
async def unban(ctx, *, member):
    await ctx.guild.unban(discord.Object(id=member))

@bot.command()
async def mute(ctx, member: discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role, reason=reason)

@bot.command()
async def unmute(ctx, member: discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.remove_roles(role, reason=reason)

@bot.command()
async def google(ctx, *, query):
    await ctx.send(f'https://www.google.com/search?q={query}') 

@bot.command()
async def github(ctx, *, query):
    await ctx.send(f'https://github.com/search?q={query}') 

@bot.command()
async def youtube(ctx, *, query):
    await ctx.send(f'https://www.youtube.com/results?search_query={query}')

@bot.command()
async def reddit(ctx, *, query):
    await ctx.send(f'https://www.reddit.com/r/{query}')

@bot.command()
async def wikipedia(ctx, *, query):
    await ctx.send(f'https://en.wikipedia.org/wiki/{query}')

@bot.command()
async def google_images(ctx, *, query):
    await ctx.send(f'https://www.google.com/search?tbm=isch&q={query}')

@bot.command()
async def twitter(ctx, *, query):
    await ctx.send(f'https://twitter.com/{query}')

@bot.command()
async def insta(ctx, *, query):
    await ctx.send(f'https://www.instagram.com/{query}')

@bot.command()
async def syntax(ctx):
    await ctx.send('https://bit.ly/Web_Syntax')
    

bot.run('OTE5MjEwMTA0NDc2MjkxMDcy.YbSfHw.A0GGHAyEv-CKceQNhyOiVnNaov0')