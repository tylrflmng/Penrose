import random
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("██████████████████████████████████████████████")
    print("Username:", client.user.name)
    print("User ID :", client.user.id)
    print()
    servers = list(client.guilds)
    print("Connected on " + str(len(client.guilds)) + " servers:")
    for x in range(len(servers)):
        print('    ' + servers[x-1].name)
    print("██████████████████████████████████████████████")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for !!help"))

@client.event
async def on_message(message):
    print(str(message.created_at)[:19])
    print(message.author)
    print(message.content)
    print("██████████████████████████████████████████████")
    
#####################################################################
    if message.content == ("!!help"):
        try:
            embed = discord.Embed(title="All the commands this bot can do", color=0xD32F2F)
            embed.add_field(name="!!invite", value="Link to add this bot to another server", inline=False)
            embed.add_field(name="!!info", value="Displays your user information", inline=False)
            embed.add_field(name="!!vote", value="Starts a vote using reactions", inline=False)
            embed.add_field(name="!!tank", value="Picks a random tank for Overwatch", inline=False)
            embed.add_field(name="!!dps", value="Picks a random dps for Overwatch", inline=False)
            embed.add_field(name="!!healer", value="Picks a random healer for Overwatch", inline=False)
            embed.add_field(name="!!wz", value="Picks a random location for Warzone", inline=False)
            embed.add_field(name="!!dice", value="Rolls a dice", inline=False)
            await message.channel.send(embed=embed)
        except Exception as e:
            print(e)
            await message.channel.send("<@277911906243837952> There has been an Error with this command")
#####################################################################
    elif message.content == ("!!invite"):
        try:
            await message.channel.send("https://discordapp.com/oauth2/authorize?client_id=494243460493344769&scope=bot")
        except Exception as e:
            print(e)
            await message.channel.send("<@277911906243837952> There has been an Error with this command")  
#####################################################################
    elif message.content == ("!!tank"):
        try:
            tank = ["D.VA", "Orisa", "Reinhardt", "Roadhog", "Sigma", "Winston", "Wrecking Ball", "Zarya"]
            hero = random.choice(tank)
            embed = discord.Embed(title="", color=0xD32F2F)
            embed.add_field(name="Random Tank", value = hero, inline=False)
            await message.channel.send(embed=embed)
        except Exception as e:
            print(e)
            await message.channel.send("<@277911906243837952> There has been an Error with this command")
################################
    elif message.content == ("!!dps"):
        try:
            dps = ["Ashe", "Bastion", "Doomfist", "Echo", "Genji", "Hanzo", "Junkrat", "McCree", "Mei",
                   "Pharah", "Reaper", "Soldier 76", "Sombra", "Symmetra","Torbjorn", "Tracer", "Widowmaker"]
            hero = random.choice(dps)
            embed = discord.Embed(title="", color=0xD32F2F)
            embed.add_field(name="Random DPS", value = hero, inline=False)
            await message.channel.send(embed=embed)
        except Exception as e:
            print(e)
            await message.channel.send("<@277911906243837952> There has been an Error with this command")
################################
    elif message.content == ("!!healer"):
        try:
            healer = ["Ana", "Baptiste", "Brigitte", "Lucio", "Mercy", "Moira", "Zenyatta"]
            hero = random.choice(healer)
            embed = discord.Embed(title="", color=0xD32F2F)
            embed.add_field(name="Random Healer", value = hero, inline=False)
            await message.channel.send(embed=embed)
        except Exception as e:
            print(e)
            await message.channel.send("<@277911906243837952> There has been an Error with this command")
#####################################################################
    elif message.content == ("!!dice"):
        try:
            dice = ["<:1_:734110378094624850>", "<:2_:734110569757540433>", "<:3_:734110585418940526>",
                    "<:4_:734110596970315907>", "<:5_:734110609918132344>", "<:6_:734110623431917629>"]
            result = random.choice(dice)
            await message.channel.send(result)
        except Exception as e:
            print(e)
            await message.channel.send("<@277911906243837952> There has been an Error with this command")
#####################################################################
    elif message.content == ("!!info"):
        try:
            embed = discord.Embed(title=message.author.name + "#" + message.author.discriminator, color=0xD32F2F)
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.add_field(name = "User ID", value = "`" + str(message.author.id) + "`", inline=False)
            embed.add_field(name= "Server Join Date", value = "__" + str(message.author.joined_at)[:19] + "__", inline=False)
            embed.add_field(name= "Account Creation Date", value =  "__" + str(message.author.created_at)[:19] + "__", inline=False)
            await message.channel.send(embed=embed)
        except Exception as e:
            print(e)
            await message.channel.send("<@277911906243837952> There has been an Error with this command")
#####################################################################
    elif message.content.startswith("!!vote"):
        try:
            vote = message.content[7::]
            if vote == (""):
                embed = discord.Embed(title="There's nothing to vote on", color=0xD32F2F)
                message = await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(title = str(message.author) + " has asked: " + vote, color=0xD32F2F)
                try:
                    await message.delete(delay=1)
                    message = await message.channel.send(embed=embed)
                    await message.add_reaction("🅰️")
                    await message.add_reaction("🅱️")
                except:
                    embed.set_footer(text="Grant 'manage messages' to delete commands")
                    message = await message.channel.send(embed=embed)
                    await message.add_reaction("🅰️")
                    await message.add_reaction("🅱️")
        except Exception as e:
            print(e)
            await message.channel.send("<@277911906243837952> There has been an Error with this command")
#####################################################################
    elif message.content == ("!!wz"):
        try:
            locations = ["Dam","Military Base","Quarry","Airport","TV Station","Storage Town","Superstore","Stadium",
                        "Lumber","Boneyard","Train Station","Hosptial","Downtown","Farmland","Promenade East","Promenade West",
                        "Hills","Park","Port","Prison"]
            drop = random.choice(locations)
            embed = discord.Embed(title="", color=0xD32F2F)
            embed.add_field(name="You should drop:", value = drop, inline=False)
            await message.channel.send(embed=embed)
        except Exception as e:
            print(e)
            await message.channel.send("<@277911906243837952> There has been an Error with this command")
    

        

    

            

        
client.run("NDk0MjQzNDYwNDkzMzQ0NzY5.XxA9cA.wju0ak0IRneDyC7_Jt0poaFuexU")




