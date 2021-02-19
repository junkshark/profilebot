import discord
import datetime
import os

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("---------------------")
    game = discord.Game("정보")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!프로필"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="디스코드 닉네임",value=message.author.name)
        embed.add_field(name="서버닉네임", value=message.author.display_name)
        embed.add_field(name="디스코드 가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일")
        embed.add_field(name="아이디", value=message.author.id)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(message.channel, embed=embed)
        
        
access_token = os.environ["BOT_TOKEN"]        
클라이언트 . 실행 (access_token) 
