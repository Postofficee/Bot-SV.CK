import os
import discord
from discord.ext import commands
from discord import Intents
from discord_interactions import DiscordInteractions

from Mys import server_on

OWNER_ID = 449594221457047562  # เปลี่ยนเป็น ID ของคุณ

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
slash = DiscordInteractions(bot)

member_data = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def send(ctx, *, text):
    if ctx.author.id != OWNER_ID:
        return  # เฉพาะคุณเท่านั้นที่สามารถใช้คำสั่งนี้

    channel = ctx.channel
    await ctx.message.delete()  # ลบข้อความคำสั่งของคุณ

    # ส่งข้อความไปยังช่องที่บอทได้ฟัง
    await channel.send(text)

@slash.command(
    name="create_card",
    description="สร้างบัตรข้อมูลสมาชิก"
)
async def create_card(ctx):
    questions = [
        "ชื่อของคุณคืออะไร?",
        "อายุของคุณ?",
        "งานอดิเรกของคุณคืออะไร?"
    ]
    answers = []

    for question in questions:
        await ctx.send(question)
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        msg = await bot.wait_for('message', check=check)
        answers.append(msg.content)

    card_content = (
        f"**บัตรข้อมูลสมาชิก**\n"
        f"ชื่อ: {answers[0]}\n"
        f"อายุ: {answers[1]}\n"
        f"งานอดิเรก: {answers[2]}"
    )

    await ctx.send(card_content)

server_on()

bot.run(os.getenv('TOKEN'))
