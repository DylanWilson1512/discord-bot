import requests
import discord
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix= ".")

@client.event
async def on_ready():
    print("bot is ready! :DDD")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Angel's Descent!"))

@client.command()
async def commands(ctx):
    commands = discord.Embed(title= "Angel's Descent ⇢ Bot Commands", color=0x7289DA, description="Here is a list of all the available commands on this server!")
    commands.add_field(name=".uuid {username}", value="Fetches the Mojang UUID of the specified player!", inline=False)
    commands.add_field(name=".skywars {username}", value="Displays the SkyWars Statistics for the specified player!", inline=False)
    commands.add_field(name=".opals {username}", value="Displays the available amount of opals for the specified player!", inline=False)
    commands.add_field(name=".invite", value="Generates an invite link to invite your friends!", inline=False)
    commands.add_field(name=".members", value="Generates the number of members in this server!", inline=False)
    await ctx.send(embed=commands)

@client.command()
async def members(ctx):
    memberCountEmbed = discord.Embed(title= "Angel's Descent ⇢ Member Count", color=0x7289DA, description=f"There are currently: **{ctx.guild.member_count} members** in this Discord!")
    await ctx.send(embed=memberCountEmbed) 

@client.command()
async def invite(ctx):
    inviteEmbed = discord.Embed(title= "Angel's Descent ⇢ Invite Link", color=0x7289DA, description="<https://discord.gg/JaDZyYQHca>")
    await ctx.send(embed=inviteEmbed) 

@client.command(pass_context=True)
async def uuid(ctx,*,message):

    try:
        mojangAPI = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{message}").json()
        uuid = mojangAPI["id"]
        name = mojangAPI["name"]

        mojangAPI = discord.Embed(title= "Angel's Descent ⇢ Mojang ID", color=0x7289DA, description=f"**{name}**: {uuid}")
        await ctx.send(embed=mojangAPI) 
    except:
        exceptMojangAPI = discord.Embed(title= "Angel's Descent ⇢ Mojang ID", color=0x7289DA, description=f"Something went wrong! Read below.")
        exceptMojangAPI.add_field(name="Error 1", value=f"Check that '**{message}**' is a valid username!", inline=False)
        exceptMojangAPI.add_field(name="Error 2", value=f"Check the **Mojang API** is a running!", inline=False)
        exceptMojangAPI.add_field(name="Error 3", value=f"You're being rate limited!", inline=False)
        await ctx.send(embed=exceptMojangAPI)

@client.command(pass_context=True)
async def opals(ctx,*,message):
    api_key = "5d7e0f3f-ae5a-4a74-9577-9afaf18752de"

    mojangAPI3 = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{message}").json()
    mcid3 = mojangAPI3["id"]

    try:    
        hypixelAPI = requests.get(f"https://api.hypixel.net/player?key={api_key}&uuid={mcid3}").json()
        displayname = hypixelAPI["player"]["displayname"]
        skywarsOpals = hypixelAPI["player"]["stats"]["SkyWars"]["opals"] if "opals" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
        skywarsShards = hypixelAPI["player"]["stats"]["SkyWars"]["shard"] if "shard" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
        skywarsGrandSlam = hypixelAPI["player"]["stats"]["SkyWars"]["grand_slam"] if "grand_slam" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
        skywarsShardSeeker = hypixelAPI["player"]["stats"]["SkyWars"]["shard_seeker"] if "shard_seeker" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
        
        opals = discord.Embed(title= "Angel's Descent ⇢ SkyWars Opals", color=0x7289DA, description=f"**{displayname}** has **{skywarsOpals}** available opals!")
        opals.add_field(name="Grand Slam", value=f"{skywarsGrandSlam}/3", inline=True)
        opals.add_field(name="Shard Seeker", value=f"{skywarsShardSeeker}/5", inline=True)
        opals.add_field(name="Shards", value=f"{skywarsShards}/20000", inline=True)
        await ctx.send(embed=opals)
    except:
        skywarsExcept = discord.Embed(title= "Angel's Descent ⇢ SkyWars Opals", color=0x7289DA, description=f"Something went wrong! Read below.")
        skywarsExcept.add_field(name="Error 1", value=f"Check that you entered a valid username!", inline=False)
        skywarsExcept.add_field(name="Error 2", value=f"Check the **Hypixel API** is a running!", inline=False)
        skywarsExcept.add_field(name="Error 3", value=f"You're being rate limited!", inline=False)
        await ctx.send(embed=skywarsExcept) 

@client.command(pass_context=True)
async def skywars(ctx,*,message):
    api_key = "5d7e0f3f-ae5a-4a74-9577-9afaf18752de"
    
    mojangAPI2 = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{message}").json()
    mcid = mojangAPI2["id"]

    hypixelAPI = requests.get(f"https://api.hypixel.net/player?key={api_key}&uuid={mcid}").json()
    displayname = hypixelAPI["player"]["displayname"]
    skywarsOpals = hypixelAPI["player"]["stats"]["SkyWars"]["opals"] if "opals" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    skywarsShards = hypixelAPI["player"]["stats"]["SkyWars"]["shard"] if "shard" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    skywarsGrandSlam = hypixelAPI["player"]["stats"]["SkyWars"]["grand_slam"] if "grand_slam" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    skywarsShardSeeker = hypixelAPI["player"]["stats"]["SkyWars"]["shard_seeker"] if "shard_seeker" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    
    #Overall Skywars Stats
    skywarsWins = hypixelAPI["player"]["stats"]["SkyWars"]["wins"] if "wins" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    skywarsTokens = hypixelAPI["player"]["stats"]["SkyWars"]["cosmetic_tokens"] if "cosmetic_tokens" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    skywarsKills = hypixelAPI["player"]["stats"]["SkyWars"]["kills"] if "kills" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    skywarsCoins = hypixelAPI["player"]["stats"]["SkyWars"]["coins"] if "coins" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    aodLevel = hypixelAPI["player"]["stats"]["SkyWars"]["angel_of_death_level"] if "angel_of_death_level" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    skywarsHeads = hypixelAPI["player"]["stats"]["SkyWars"]["heads"] if "heads" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    skywarsSouls = hypixelAPI["player"]["stats"]["SkyWars"]["souls"] if "souls" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    skywarsOpals = hypixelAPI["player"]["stats"]["SkyWars"]["opals"] if "opals" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    skywarsDeaths = hypixelAPI["player"]["stats"]["SkyWars"]["deaths"] if "deaths" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    skywarsLosses = hypixelAPI["player"]["stats"]["SkyWars"]["deaths"] if "deaths" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    
    #Solo Skywars Stats
    soloKills = hypixelAPI["player"]["stats"]["SkyWars"]["kills_solo"] if "kills_solo" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    soloDeaths = hypixelAPI["player"]["stats"]["SkyWars"]["deaths_solo"] if "deaths_solo" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    soloWins = hypixelAPI["player"]["stats"]["SkyWars"]["wins_solo"] if "wins_solo" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    soloLosses = hypixelAPI["player"]["stats"]["SkyWars"]["losses_solo"] if "losses_solo" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    
    #Doubles Skywars Stats
    teamKills = hypixelAPI["player"]["stats"]["SkyWars"]["kills_team"] if "kills_team" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    teamDeaths = hypixelAPI["player"]["stats"]["SkyWars"]["deaths_team"] if "deaths_team" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    teamWins = hypixelAPI["player"]["stats"]["SkyWars"]["wins_team"] if "wins_team" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    teamLosses = hypixelAPI["player"]["stats"]["SkyWars"]["losses_team"] if "losses_team" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    
    #Ranked Skywars Stats  
    rankedWins = hypixelAPI["player"]["stats"]["SkyWars"]["wins_ranked"] if "wins_ranked" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    rankedDeaths = hypixelAPI["player"]["stats"]["SkyWars"]["deaths_ranked"] if "deaths_ranked" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    rankedKills = hypixelAPI["player"]["stats"]["SkyWars"]["kills_ranked"] if "kills_ranked" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    rankedLosses = hypixelAPI["player"]["stats"]["SkyWars"]["losses_ranked"] if "losses_ranked" in hypixelAPI["player"]["stats"]["SkyWars"] else 0
    #API End

    
    #KD and WL {solo}
    if soloKills and skywarsWins > 0:
        killDeath = skywarsKills / skywarsDeaths
        killDeath = round(killDeath,2)
        winLoss = skywarsWins / skywarsLosses
        winLoss = round(winLoss,2)
    else:
        killDeath = 0
        winLoss = 0

    #KD and WL {team}
    if teamKills and teamWins > 0:
        teamKillDeath = teamKills / teamDeaths
        teamKillDeath = round(teamKillDeath,2)
        teamWinLoss = teamWins / teamLosses
        teamWinLoss = round(teamWinLoss,2)
    else:
        teamKillDeath = 0
        teamWinLoss = 0

    #KD and WL {ranked}
    if rankedKills and rankedWins > 0:
        rankedKillDeath = rankedKills / rankedDeaths
        rankedKillDeath = round(rankedKillDeath,2)
        rankedWinLoss = rankedWins / rankedLosses
        rankedWinLoss = round(rankedWinLoss,2)
    else:
        rankedKillDeath = 0
        rankedWinLoss = 0
    
    skywars = discord.Embed(title= "Angel's Descent ⇢ SkyWars Statistics", color=0x7289DA, description=f"SkyWars Statistics for **{displayname}**")
    skywars.add_field(name="Souls", value=f"{skywarsSouls}", inline=True)
    skywars.add_field(name="Coins", value=f"{skywarsCoins}", inline=True)
    skywars.add_field(name="Tokens", value=f"{skywarsTokens}", inline=True)

    skywars.add_field(name="⠀", value=f"⠀", inline=False)

    skywars.add_field(name="Kills", value=f"{skywarsKills}", inline=True)
    skywars.add_field(name="Wins", value=f"{skywarsWins}", inline=True)
    skywars.add_field(name="K/D | W/L", value=f"{killDeath} | {winLoss}", inline=True)

    skywars.add_field(name="Doubles Kills", value=f"{teamKills}", inline=True)
    skywars.add_field(name="Doubles Wins", value=f"{teamWins}", inline=True)
    skywars.add_field(name="K/D | W/L", value=f"{teamKillDeath} | {teamWinLoss}", inline=True)

    skywars.add_field(name="Ranked Kills", value=f"{rankedKills}", inline=True)
    skywars.add_field(name="Ranked Wins", value=f"{rankedWins}", inline=True)
    skywars.add_field(name="K/D | W/L", value=f"{rankedKillDeath} | {rankedWinLoss}", inline=True)

    skywars.add_field(name="⠀", value=f"⠀", inline=False)

    skywars.add_field(name="Grand Slam", value=f"{skywarsGrandSlam}/3", inline=True)
    skywars.add_field(name="Shard Seeker", value=f"{skywarsShardSeeker}/5", inline=True)
    skywars.add_field(name="Shards", value=f"{skywarsShards}/20000", inline=True)

    await ctx.send(embed=skywars)


client.run("ODIyMTEyOTg5Mjc2NTM2ODcy.YFNiYg.QThV4g-HjK-2OUGBiG7UJ75r7UA")