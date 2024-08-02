import os
import discord
from discord.ext import commands

from Mys import server_on

OWNER_ID = 449594221457047562  # เปลี่ยนเป็น ID ของคุณ

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='=', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def t(ctx, *, text):
    if ctx.author.id != OWNER_ID:
        return  # เฉพาะคุณเท่านั้นที่สามารถใช้คำสั่งนี้

    channel = ctx.channel
    await ctx.message.delete()  # ลบข้อความคำสั่งของคุณ

    # ส่งข้อความไปยังช่องที่บอทได้ฟัง
    await channel.send(text)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!🖐🏼. I'm Mr. Lollipop, Do you need any help?. 🍬")

    channel = ctx.channel
    await ctx.message.delete()  # ลบข้อความคำสั่งของคุณ

    # ส่งข้อความไปยังช่องที่บอทได้ฟัง
    await channel.send(text)

server_on()

bot.run(os.getenv('TOKEN'))
