# noinspection PyPackageRequirements
import discord

from markdown_discord_bot import config

client = discord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.attachments:
        ext = message.attachments[0].filename.split('.')[1]
        if ext in config.EXTS:
            if (message.attachments[0].size + len(ext) + 8) <= 2000:  # 8 is len(```) x2+\n x2 in bytes
                print(f'Got {message.attachments[0].filename}')
                file_content = (await message.attachments[0].read()).decode()
                await message.channel.send(f"```{ext}\n{file_content}\n```")
            else:
                await message.channel.send(
                    "Слишком большой файл. Невозможно отправить в качестве одного сообщения")


def main():
    client.run(config.DISCORD_TOKEN)
