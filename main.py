import discord
import os, socket
import requests
from requests import get, post
from time import sleep
from keep_alive import keep_alive
from discord.ext import commands

os.system("clear")
sleep(7)
intents = discord.Intents().all()
bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=".",intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    activity = discord.Game(name="Samp Monitor!", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print (bot.user.name + " Is Online!")

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Help Command",color=ctx.author.color)
  embed.add_field(name="Command",value="""
samp,portscan,pingscan,checkweb,ipinfo""")
  await ctx.send(embed=embed)


@bot.command(name="samp")
async def samp(ctx, *,args=None):
        if args is None:
          await ctx.send("""
        ```
Usage !samp <ip>:<port>
example !samp 192.168.1.1:7777
        ```
        """)
        else:
          splits = args.split(":")
          ip = str(splits[0])
          port = int(splits[1])
          r = requests.get(f"https://tokyosamp.cyclic.app/API/samp?ip={ip}&port={port}")
          if "Something Went Wrong Please Check ip And port correcly or Please Try Again Later" in r.text:
            await ctx.send(f"Unable to connect to {ip}:{port}")
          else:
            res = r.json()
            samp = res['response']
            rule = samp['rule']
            embed = discord.Embed(title="",color=0x00000,timestamp=ctx.message.created_at)
            embed.set_author(name=samp['hostname'].upper())
            embed.add_field(name="Gamemode",value=f"{samp['gamemode']}")
            embed.add_field(name="Language",value=f"{samp['language']}")
            embed.add_field(name="Password",value=f"{samp['passworded']}")
            embed.add_field(name="PlayersOnline",value=f"{samp['isPlayerOnline']}/{samp['maxplayers']}")
            embed.add_field(name="Mapname",value=f"{rule['mapname']}")
            embed.add_field(name="Lagcomp",value=f"{rule['lagcomp']}")
            embed.add_field(name="Weather",value=f"{rule['weather']}")
            embed.add_field(name="Worldtime",value=f"{rule['worldtime']}")
            embed.add_field(name="Weburl",value=f"[{rule['weburl']}](http://{rule['weburl']})")
            embed.add_field(name="Version",value=f"{rule['version']}")
            embed.add_field(name="Only Show 10 Players Online!",value=f"""
            ```
[ID]   Name      Score Ping
---------------------------
{samp['isPlayersIngame']}\n
            ```
            """)
            embed.set_thumbnail(url="https://i.postimg.cc/P5d2CCv7/samp-logo-png-6.png")
            await ctx.send(embed=embed)

@bot.command()
async def portscan(ctx, *, args=None):
  if args is None:
    await ctx.send("""
    ```
Usage !portscan <ip> <port>
example !portscan 192.23.20 22
    ```
    """)
  else:
    splits = args.split(" ")
    ip = str(splits[0])
    port = int(splits[1])
    r = requests.get(f"https://xalbador.cyclic.app/API/scan?ip={ip}&port={port}")
    res = r.json()
    te = res["response"]
    scan = te["status"]
    await ctx.send(f"```Port {port} is {scan}```")


@bot.command(name="ipinfo")
async def ip(ctx, *, arg=None):
  if arg is None:
    await ctx.send("""
    ```
Usage $ipinfo <ip>
example $ipinfo 8.8.8.8/hostname
    ```
    """)
  else:
    r = requests.get(f"http://ip-api.com/json/{arg}?fields=33292287")
    res = r.json()
    embed = discord.Embed(title="",
                          color=ctx.author.color,
                          timestamp=ctx.message.created_at)
    embed.add_field(name=f"Information IP {res['query']}",
                    value=f"""
    ```
IP: {res['query']}
Continent: {res['continent']}
ContinentCode: {res['continentCode']}
Country: {res['country']}
Country: {res['countryCode']}
Region: {res['region']}
RegionName: {res['regionName']}
City: {res['city']}
District: {res['district']}
Zip: {res['zip']}
Lat: {res['lat']}
Lon: {res['lon']}
TimeZone: {res['timezone']}
Currency: {res['currency']}
Isp: {res['isp']}
Org: {res['org']}
As: {res['as']}
Asname: {res['asname']}
Reverse: {res['reverse']}
Mobile: {res['mobile']}
Proxy: {res['proxy']}
Hosting: {res['hosting']}
    ```
    [GoogleMaps](https://maps.google.com/?q={res['lat']},{res['lon']})""")
    await ctx.send(embed=embed)

@bot.command()
async def pingscan(ctx, *, args=None):
  if args is None:
    await ctx.send("""pingscan <ip>:<port>""")
  else:
    splits = args.split(":")
    ip = str(splits[0])
    port = int(splits[1])
    r = requests.get(f"https://xalbador.cyclic.app/API/ping?ip={ip}&port={port}")
    if "Something Went Wrong Please Check ip And port correcly or Please Try Again Later" in r.text:
      await ctx.send(f"Unable to connect to {ip}:{port}")
    else:
      res = r.json()
      te = res["response"]
      ping = te["ping"]
      await ctx.send(f"```Server ping is {ping}ms```")
keep_alive()
try:
  bot.run(os.environ['TOKEN'])
except Exception as e:
  print(f"Error when logging in: {e}")
  print("\n\n\nMOHON TUNGGU\n\n\n")
  os.system("kill 1")