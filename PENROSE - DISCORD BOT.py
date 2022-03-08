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
    author = str(message.author)
    authorID = str(message.author.id)
    authorCheck = author.lower()[:-5]
    
##    print(str(message.created_at)[:19])
##    print(message.author)
##    print(message.content)
##    print("██████████████████████████████████████████████")

    if (message.channel.id == (851489737758998529)):
        try:
            if authorCheck in message.content.lower():
                if "soundcloud.com" in message.content.lower():
                    await message.delete(delay=1)
                    await message.channel.send("Rule 4, <@" + authorID + "> no self promo")

        except Exception as e:
            print(e)
            await message.channel.send("<@277911906243837952> There has been an error with this command")
    
#####################################################################
    if message.content == ("!!help"):
        try:
            embed = discord.Embed(title="All the commands this bot can do", color=0xD32F2F)
            embed.add_field(name="!!invite", value="Link to add this bot to another server", inline=False)
            embed.add_field(name="!!info", value="Displays your user information", inline=False)
            embed.add_field(name="!!vote", value="Starts a vote using reactions", inline=False)
            await message.channel.send(embed=embed)
        except Exception as e:
            print(e)
            await message.channel.send("<@277911906243837952> There has been an error with this command")
#####################################################################
    elif message.content == ("!!invite"):
        try:
            await message.channel.send("https://discordapp.com/oauth2/authorize?client_id=494243460493344769&scope=bot")
        except Exception as e:
            print(e)
            await message.channel.send("<@277911906243837952> There has been an error with this command")  
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
            await message.channel.send("<@277911906243837952> There has been an error with this command")
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
            await message.channel.send("<@277911906243837952> There has been an error with this command")
#####################################################################




