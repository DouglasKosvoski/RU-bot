from bs4 import BeautifulSoup
import requests, os, json
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
INVITE_LINK = os.getenv('INVITE_LINK')
URL = os.getenv('URL')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    activeservers = client.guilds
    for guild in activeservers:
        print(guild.name)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content in ['!link', '!invite']:
        await message.channel.send(INVITE_LINK)

    elif message.content in ['!salve', '!ola', '!oi']:
        await message.channel.send("Salve")

    elif message.content in ["!autor", "!author"]:
        await message.channel.send("`Douglas Kosvoski`")

    elif message.content in ["!codigo", "!repo", "!repositorio"]:
        await message.channel.send("`https://github.com/DouglasKosvoski/RU-bot`")

    elif message.content in ['!menu', '!cardapio', '!cardápio']:
        data = get_content(URL)
        for key, value in data.items():
            temp = ""
            for i in value:
                temp += i + "\n"
            temp = key + "\n```\n" + temp + "```"
            await message.channel.send(":fork_knife_plate: " + temp)

    elif message.content in ['!cmd', '!cmds', "!commands", "!comandos"]:
        cmds = ['!link', '!invite', '!salve', '!ola', '!oi', '!menu',
                '!cardapio', '!cardápio', "!autor", "!author", "!codigo",
                "!repo", "!repositorio"]
        temp = ""
        for i in cmds:
            temp += i + "\n"
        temp = f"```{temp}```"
        await message.channel.send(temp)

def get_content(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    vrau = []

    for table in soup.find_all('tbody'):
        for tr in table.find_all('tr'):
            for td in tr.find_all('td'):
                vrau.append(td.find('p').text)

    xesque = {}
    for day in range(5):
        asd = []
        for i in range(day, len(vrau), 5):
            if i == day:
                xesque[vrau[i]] = {}
            else:
                if len(vrau[i]) >= 3:
                    asd.append(vrau[i])

        xesque[list(xesque.keys())[day]] = asd

    return xesque

def main():
    client.run(TOKEN)


if __name__ == '__main__':
    main()
