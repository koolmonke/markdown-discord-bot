# noinspection PyPackageRequirements
import discord

from markdown_discord_bot import config

DISCORD_MESSAGE_MAX_SIZE = 2000

client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.attachments:
        ext = message.attachments[0].filename.split('.')[-1]
        if ext in config.EXTS:
            file_content = (await message.attachments[0].read()).decode()
            maximum_message_size = DISCORD_MESSAGE_MAX_SIZE - 8 - len(ext)  # 8 - len(ext) is markdown overhead
            full_message = f"```{ext}\n{file_content[:maximum_message_size]}\n```"
            print(f"Got {message.attachments[0].filename} from {message.author} with {len(full_message)=}")
            await message.reply(full_message)


def main():
    client.run(config.DISCORD_TOKEN)
