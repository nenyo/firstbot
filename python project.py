import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("고양이게임")
    await client.change_presence(status=discord.Status.online)





@client.event
async def on_message(message):
    if message.content.startswith("/노예"):
        await message.channel.send("저는 암냥님의 노예입니다")

    if message.content.startswith("/안녕"):
        await message.channel.send("ㅎㅇ")

    if message.content.startswith("/들레"):
        await message.channel.send("뿌까뿌까")

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

client.run("NTg0Mjg2ODQ3Mzc5NzAxNzkw.XPNQxQ.CurdXhxhkG50rq4f0L051-FC5GA")
