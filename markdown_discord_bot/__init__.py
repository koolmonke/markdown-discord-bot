# noinspection PyPackageRequirements
import discord

from markdown_discord_bot import config

client = discord.Client()


def split_with_char_limit(string: str, max_size: int):
    return (string[i:i + max_size] for i in range(0, len(string), max_size))


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.attachments and message.content != "no-preview":
        ext = message.attachments[0].filename.split('.')[1]
        if ext in config.EXTS:
            print(f"Got {message.attachments[0].filename} from {message.author}")
            file_content = (await message.attachments[0].read()).decode()
            is_first = True
            for part in split_with_char_limit(file_content, 1992 - len(ext)):
                full_message = f"```{ext}\n{part}\n```"
                print(f"{len(full_message)=}")
                if is_first:
                    await message.reply(full_message)
                    is_first = False
                else:
                    await message.channel.send(full_message)


def main():
    client.run(config.DISCORD_TOKEN)
