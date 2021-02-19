import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트봇")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("뭐 새꺄")
    if message.content.startswith("바보"):
        await message.channel.send("응 반사")
    if message.content.startswith("멍청이"):
        await message.channel.send("자기소개 잘하네")
    if message.content.startswith("병신"):
        await message.channel.send("어떻게 그렇게 심한말을... 야이 호랑말코 옘병 시베리아 수박 시발라먹을 새끼야")
    if message.content.startswith("꺼져"):
        await message.channel.send("너도 븅아")
    if message.content.startswith("야"):
        await message.channel.send("ㅗㅗㅗㅗㅗ")


client.run("ODEyMTkyOTAyMTIwNzM0Nzgw.YC9LlQ.8LqRwBR45lW8JETh5mFLEf9na4s")
