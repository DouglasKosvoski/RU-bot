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
    elif message.content.startswith("!") == False:
        return
    else:
        msg = message.content[1::]

    if msg in ['link', 'invite']:
        await message.channel.send(INVITE_LINK)

    elif msg in ['ru', 'site', 'web']:
        await message.channel.send("https://www.uffs.edu.br/campi/chapeco/restaurante_universitario")

    elif msg in ["autor", "author", "criador"]:
        await message.channel.send("`Douglas Kosvoski - 2022.1`")

    elif msg in ["code", "codigo", "repo", "repositorio"]:
        await message.channel.send("https://github.com/DouglasKosvoski/RU-bot")

    elif msg in ['menu', 'cardapio']:
        data = get_content(URL)
        for key, value in data.items():
            temp = ""
            count = 0
            for i in value:
                if count == 0:
                    temp += "--- Saladas ---\n"
                elif count == 3:
                    temp += "\n--- Pratos Principais ---\n"
                elif count == len(value)-1:
                    temp += "\n--- Sobremesa ---\n"

                temp += i + "\n"
                count += 1

            temp = key + "\n```\n" + temp + "```"
            await message.channel.send(":fork_knife_plate: " + temp)

    elif msg in ['cmd', 'cmds', "commands", "comandos", "help"]:
        cmds = [
            'link', 'invite', 'ru', 'site', 'web', "autor", "author", "criador", "code", "codigo", "repo", "repositorio", 'menu', 'cardapio'
        ]
        temp = ""
        for i in cmds:
            temp += i + "\n"
        temp = f"```{temp}```"
        await message.channel.send(temp)

def get_content(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    data = []

    for table in soup.find_all('tbody'):
        for tr in table.find_all('tr'):
            for td in tr.find_all('td'):
                data.append(td.find('p').text)

    week_data = {}
    for day in range(5):
        foods = []
        for i in range(day, len(data), 5):
            if i == day:
                week_data[data[i]] = {}
            else:
                if len(data[i]) >= 3:
                    foods.append(data[i])

        if len(foods) > 10:
            foods = foods[11::]
        week_data[list(week_data.keys())[day]] = foods

    return week_data

def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()