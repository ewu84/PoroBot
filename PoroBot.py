import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import requests
from discord.utils import get
Client = discord.Client()
client = commands.Bot(command_prefix = "dank")


@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    
    if message.content.startswith("psearch!"):
        args = message.content.split(" ")
        name = args[1:]
        print(name)
        space = ' '
        name = space.join(name)
        print(name)
        string = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + name + '?api_key=RGAPI-30070262-1d35-4800-bff3-a7d5a5c3ee82'
        r = requests.get(string)
        print(string)
        data = r.json()
        participantID = str(data["id"])
        participantLevel = str(data["summonerLevel"])
        participantName = data["name"]
        string4 = 'https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/' + participantID + '?api_key=RGAPI-30070262-1d35-4800-bff3-a7d5a5c3ee82'
        print(string4)
        finar = requests.get(string4)
        data4 = finar.json()
        if data4 != []:
            datarata = data4[0]
            rank = datarata['rank']
            tier = datarata['tier']
            if tier == "BRONZE":
                emoji = '<:BRONZE:457608214893297665>'
            if tier == "SILVER":
                emoji = '<:SILVER:457608274582175746>'
            if tier == "GOLD":
                emoji = '<:GOLD:457608323814916112>'
            if tier == "PLATINUM":
                emoji = '<:PLATINUM:457608409672450080>'
            if tier == "CHALLENGER":
                emoji = '<:CHALLENGER:457608471706206209>'
            if tier == "DIAMOND":
                emoji = '<:DIAMOND:457609634081931275>'
            if tier == "MASTER":
                emoji = '<:MASTER:457608443583397888>'
            embed = discord.Embed(title=participantName)
            embed.add_field(name='League', value = emoji + ' ' + rank)
            embed.add_field(name = 'Level', value = 'Level: ' + participantLevel)
            await client.send_message(message.channel, embed=embed)
        else:
            embed = discord.Embed(title=participantName)
            embed.add_field(name='League', value = 'Unranked')
            embed.add_field(name = 'Level', value = 'Level: ' + participantLevel)
            await client.send_message(message.channel, embed=embed)
    if message.content.startswith('plive!'):
        args = message.content.split(" ")
        name = args[1:]
        print(name)
        space = ' '
        name = space.join(name)
        print(name)
        string = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + name + '?api_key=RGAPI-30070262-1d35-4800-bff3-a7d5a5c3ee82'
        r = requests.get(string)
        data = r.json()
        print(data)
        summ = data["id"]
        string2 = 'https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/' + str(summ) + '?api_key=RGAPI-30070262-1d35-4800-bff3-a7d5a5c3ee82'
        print(string2)
        rtwo = requests.get(string2)
        dataa = rtwo.json()
        print(dataa)
        participants = dataa["participants"]
        participantNames = []
        counter = 0
        embed = discord.Embed(title="Live Game Stats")
        tiers = [] 
        ranks = []
        levels = []
        for participant in participants:
            participantName = participant['summonerName']
            participantNames.append(participantName)
            
            string3 = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + participantNames[counter] + '?api_key=RGAPI-30070262-1d35-4800-bff3-a7d5a5c3ee82'
            r3 = requests.get(string3)
            data3 = r3.json()
            participantID = str(data3["id"])
            participantLevel = str(data3["summonerLevel"])
            string4 = 'https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/' + participantID + '?api_key=RGAPI-30070262-1d35-4800-bff3-a7d5a5c3ee82'
            
            print(string4)
            finar = requests.get(string4)
            data4 = finar.json()
            print(data4)
            if data4 == []:
                tiers.append('<:UNRANKED:457609694953865226>')
                ranks.append(' ')
                levels.append(participantLevel)
                counter += 1
            else:
                datarata = data4[0]
                tier = datarata["tier"]
                rank = datarata["rank"]
                emoji = ''
                if tier == "BRONZE":
                    emoji = '<:BRONZE:457608214893297665>'
                if tier == "SILVER":
                    emoji = '<:SILVER:457608274582175746>'
                if tier == "GOLD":
                    emoji = '<:GOLD:457608323814916112>'
                if tier == "PLATINUM":
                    emoji = '<:PLATINUM:457608409672450080>'
                if tier == "CHALLENGER":
                    emoji = '<:CHALLENGER:457608471706206209>'
                if tier == "DIAMOND":
                    emoji = '<:DIAMOND:457609634081931275>'
                if tier == "MASTER":
                    emoji = '<:MASTER:457608443583397888>'
                counter += 1 
                tiers.append(emoji)
                ranks.append(rank)
                levels.append(participantLevel)
        vdalue = participantNames[5] + '\n' + participantNames[6] + '\n' + participantNames[7] + '\n' + participantNames[8] + '\n' + participantNames[9]
        vbalue = participantNames[0] + '\n' + participantNames[1] + '\n' + participantNames[2] + '\n' + participantNames[3] + '\n' + participantNames[4]
        
        embed.add_field(name = ':large_blue_diamond: Blue Team', value = vbalue)
        
        rvalue = '\n' + tiers[0] + ranks[0] + '\n' + tiers[1] + ranks[1] + '\n' + tiers[2] + ranks[2] + '\n' + tiers[3] + ranks[3] + '\n' + tiers[4] + ranks[4]
        rvalued = '\n' + tiers[5] + ranks[5] + '\n' + tiers[6] + ranks[6] + '\n' + tiers[7] + ranks[7] + '\n' + tiers[8] + ranks[8] + '\n' + tiers[9] + ranks[9]
        embed.add_field(name = '\nRanks', value = rvalue)
        levelvalues = levels[0] + '\n' + levels[1] + '\n' + levels[2] + '\n' + levels[3] + '\n' + levels[4]
        levelvalued = levels[5] + '\n' + levels[6] + '\n' + levels[7] + '\n' + levels[8] + '\n' + levels[9]
        embed.add_field(name = '\nLevels', value = levelvalues)
        embed.add_field(name = ':diamonds: Red Team', value = vdalue)
        embed.add_field(name = 'Ranks', value = rvalued)
        embed.add_field(name = 'Levels', value = levelvalued)

        await client.send_message(message.channel, embed=embed)
        
    if message.content.startswith("p!help"):
        await client.send_message(message.channel, "Poro baita righty nowie. Commandos ahri plg! Namey for live gamey static tacs and pl! Name for level of summoner!!!!")
    if message.content.startswith("p!ping"):
          
        embed = discord.Embed(title = "How to test your ping")
        embed.add_field(name = "Windows", value = "To test your ping, open Command Prompt by pressing the windows key + r. Type cmd and press enter. Copy and paste this code: ping 104.160.131.3 -t")
        
        embed.add_field(name = "Mac", value = "To test your ping, open Terminal by open your Applications folder then open the Utilities folder. Click on the Terminal application. Copy and paste this code: ping 104.160.131.3 -t")
        await client.send_message(message.channel, embed=embed)
    if message.content.startswith("pchamp!"):
        
        args = message.content.split(" ")
        if len(args) == 2:
            champName = args[1]
        print(champName)
        r = requests.get('https://na1.api.riotgames.com/lol/static-data/v3/champions?api_key=RGAPI-30070262-1d35-4800-bff3-a7d5a5c3ee82')
        data = r.json()
        if champName not in data["data"]:
            await client.send_message(message.channel, "That champion doesn't exist! Please use proper caps and spelling")
        else:
            
            champID = data["data"][champName]["id"]
            r = requests.get("https://na1.api.riotgames.com/lol/static-data/v3/champions/" + str(champID) + "?locale=en_US&champData=stats&api_key=RGAPI-30070262-1d35-4800-bff3-a7d5a5c3ee82")
            
            datar = r.json()
            data = datar["stats"]
            armor = str(data["armor"])
            armorperlevel = str(data["armorperlevel"])
            attackdamage = str(data["attackdamage"])
            attackdamageperlevel = str(data["attackdamageperlevel"])
            attackrange = str(data["attackrange"])
            attackspeedoffset = str(data["attackspeedoffset"])
            attackspeedperlevel = str(data["attackspeedperlevel"])
            crit = str(data["crit"])
            critperlevel = str(data["critperlevel"])
            hp = str(data["hp"])
            hpperlevel = str(data["hpperlevel"])
            hpregen = str(data["hpregen"])
            hpregenperlevel = str(data["hpregenperlevel"])
            movementspeed = str(data["movespeed"])
            mana = str(data["mp"])
            manaperlevel = str(data["mpperlevel"])
            manaregenperlevel = str(data["mpregenperlevel"])
            manaregen = str(data["mpregen"])
            magicresist = str(data["spellblock"])
            magicresistperlevel = str(data["spellblockperlevel"])
            await client.send_message(message.channel, champName + ":")
            embed = discord.Embed(name = champName)
            embed.add_field(name = "Armor", value = armor + ', ' + armorperlevel)
            embed.add_field(name = "Attack Damage", value = attackdamage + ', ' + attackdamageperlevel + ' per level')
            embed.add_field(name = "Attack Range", value = attackrange)
            embed.add_field(name = "Crit Chance", value = crit + ', ' + critperlevel + ' per level')
            embed.add_field(name = "Health", value = hp + ' ' + hpperlevel + ' per level')
            embed.add_field(name = "Health Regen", value = hpregen + ', ' + hpregenperlevel + ' per level')
            embed.add_field(name = "Movement Speed", value = movementspeed)
            embed.add_field(name = "Mana", value = mana + ' ' + manaperlevel + ' per level')
            embed.add_field(name = "Mana Regen", value = manaregen + ', ' + manaregenperlevel + ' per level')
            embed.add_field(name = "Magic Resist", value = magicresist + ', ' + magicresistperlevel + ' per level')
            await client.send_message(message.channel, embed=embed)
            embed = discord.Embed(name = "Tips")
            r = requests.get("https://na1.api.riotgames.com/lol/static-data/v3/champions/" + str(champID) + "?locale=en_US&tags=allytips&tags=enemytips&api_key=RGAPI-30070262-1d35-4800-bff3-a7d5a5c3ee82")
            data = r.json()
            enemy = data["enemytips"]
            print(enemy)
            enemytips = enemy[0]
            print(enemytips)
            counter = 1
            for i in enemy:
                enemytips = enemytips + '\n' + enemy[counter]
                counter += 1
            ally = data["allytips"]
            allytips = ally[0]
            counter = 1
            for i in ally:
                allytips = allytips + '\n' + ally[counter]
                counter += 1
            embed.add_field(name = "Against " + champName, value = enemytips)
            embed.add_field(name = "While playing " + champName, value = allytips)
            await client.send_message(message.channel, embed=embed)
client.run("NDIyNzgzMzgxMTg1NzU3MTk0.Df3_aA.25jGy2o5MF1dyJf5KvucRE3rpxo")
