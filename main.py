from replit import db
import discord
import pytz
from discord.ext import commands, tasks
from discord.utils import get
from datetime import datetime
from datetime import timedelta
import threading
import asyncio
import random
import os
from discord.ext.commands import CommandNotFound
import csv
from online import online
import random
import pickle
import sys
from discord import Embed, Color
from discord.ext.commands import has_permissions, MissingPermissions
import json
from discord.ext import commands
from discord.ext import buttons










# AUTHOR: Tarun Eswar
# UPDATE DATE: 7/26/2022
# CONTENTS:
# 1. DATABASE
# 2. SETUP OF BOT
#  a. PREFIX GETTER
#  b. INTENTIONS/SETUP
#  c. GLOBAL VARS
#  d. UNKNOWN PREFIX
#  e. SET DEFAULT PREFIX
#  f. BROADCASTS TO ALL SERVERS
#  g. RETRIEVE PREFIX
#  h. CHANGE PREFIX
#  i. RENAME BOT
#  j. TICKETS
#  k. WELCOME MEMBERS
#  l. SET TIME
#  m. RESOURCES
#  n. COMMAND ERROR
#  o. COGS
#    - CHESS
#    - DEBATE
#    - DM
#    - EMBEDER
#    - HELP
#    - ONLINE
#    - PAIR
#    - ROLE

# ---------------------------------------- #
# ---------------- DATABASE -------------- #
# ---------------------------------------- #
# db["name"] =
#db["debateQuestions"] = ['The United States federal government should legalize all illicit drugs.', 'Countries should guarantee universal child care.', 'Countries should provide a universal basic income of $10,0000 per person', 'The U.S. Federal Government should sustainably increase its investment on high-speed rails', 'In The U.S., does the benefits of  increasing organic agriculture outweigh the harms?', 'Should the United States implement a single-payer universal healthcare system?', 'The member nations of the World Trade Organizations to reduce intellectual property protections for medicines', 'A public health emergency justifies limiting civil liberties', 'The United States ought to provide a federal job guarantee, The United States ought to eliminate subsidies for fossil fuels', 'In the United States, reporters ought to have the right to protect the identity of confidential sources', 'Wealthy nations have an obligations to provide development assistance to other nations', 'The United States ought to guarantee the right to housing', 'Public colleges and universities in the United States ought not restrict any constitutionally protected speech', 'Just governments ought to ensure food security for their citizens', 'Placing political conditions on humanitarian aid to foriegn countries are unjust', 'Rehabilitation ought to be valued above retribution in The United States Criminal Justice System', 'Justice requires the recognition of animal rights', 'Public Health concerns justify compulsory immunization', 'It is morally permissible to kill one innocent person to save the lives of more innocent people', 'The Secondary education in America should value fine arts over athletics', 'A just government should provide healthcare to its citizens', 'The pursuit of scientific knowledge ought to be constrained for societal good', 'Establishing a safe educational environment in grades K-12 justifies infringement on students civil liberties', 'The benefits of the International Monetary fund outweigh the harms', 'Are charter schools considered beneficial in terms of the quality of education in the united states', 'The US federal government should enforce antitrust regulations on technology giants', 'The United States Federal government should']

# db["chessQuestions"] = ['What is your favorite/least favorite opening? Why?', 'Countries should guarantee universal child care.', 'Who are you rooting for in the next world championship? Nepo or Ding?', 'Share a fun tactic from a recent game you played!', 'What is the best chess-related story that happened to you or you heard?', 'Which stage of the game are you the best at? Opening, Middlegame, Endgame?', 'Share a puzzle you found and challenge everyone else to find the answer!', 'What is the most fun part of chess? Don’t just say winning :)', 'Create the best chess dad-joke', 'Does chess count as a sport?', 'Who is your favorite chess player of all time? Why?', 'Share a game that you played really badly in :)', 'What are some things your opponents do that annoys you in over-the-board chess?', '1. e4!! or 1. d4!! ?', 'Share a weird endgame pattern that you have memorized but never/rarely use']
# colors = [ 0xdbbe8a, 0xcae394, 0x82adc4, 0xc0a8f0, 0x8c2727, 0xe08743, 0xffc800, 0x6e7a58, 0x8affcc, 0x5a6e65 ]

# ---------------------------------------- #
# -------------- SETUP OF BOT ------------ #
# ---------------------------------------- #


# ------------ PREFIX GETTER ------------ #
def get_prefix(client, message):
    return db[str(message.guild.id)]


# ------------ INTENTIONS/SETUP ------------ #
intents = discord.Intents.all()
intents.members = True
intents.reactions = True
client = commands.Bot(command_prefix=get_prefix, intents=intents)
client.remove_command('help')

# ------------ GLOBAL VARS ------------ #
current_date = None
current_time = None
currentDay = None
est = pytz.timezone('US/Eastern')

# ------------ LOADING?U------------ #
@client.command()
async def load(extension_name: str):
    try:
        client.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await client.say("{} loaded.".format(extension_name))


@client.command()
async def unload(extension_name: str):
    client.unload_extension(extension_name)
    await client.say("{} unloaded.".format(extension_name))


# ------------ UNKNOWN PREFIX --------- #
@client.event
async def on_message(message):
    mute_words = ["are you interested", "contact", "our mission"]
    number = 0
    if message.author != client.user:
        for word in mute_words:
            if word.lower() in message.content:
                number += 1
        if number >= 2:
            await message.channel.purge(
                after=datetime.now() - timedelta(minutes=10),
                check=lambda x: x.author.id == message.author.id,
                oldest_first=False)
            muted_role = discord.utils.get(message.guild.roles, name='Muted')
            await message.author.add_roles(muted_role)
            for server in client.guilds:
                channel2 = discord.utils.get(server.channels,
                                             name="server-updates")
            await channel2.send(
                f'muted spammer {message.author} and deleted messages')

    if message.content == "~CMDnullOverride" and message.author.id == 743999268167352651:
        db[str(message.guild.id)] = "~"
        embed = discord.Embed(title="",
                              description="Prfx error resolved.",
                              colour=discord.Colour.green())
        await message.channel.send(embed=embed)
    elif str(message.author.id) in db["bans"]:
        return
    else:
        await client.process_commands(message)


# ---------- SET DEFAULT PREFIX --------- #
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('~help'))
    print("ready.")


@client.event
async def on_guild_join(guild):
    db[str(guild.id)] = "."


@client.command(pass_context=True)
# ---------- BROADCASTS TO ALL SERVERS --------- #
async def broadcast(ctx, *msg):
    if ctx.author.id == 743999268167352651:
        for server in client.guilds:
            for channel in server.channels:
                try:
                    args = ""
                    for i in range(len(msg)):
                        args += msg[i] + " "
                    await channel.send(args)
                except Exception:
                    continue
                else:
                    break


# ------------ RETRIEVE PREFIX --------- #
@client.command()
async def prefix(ctx):
    cmd = db[str(ctx.message.guild.id)]
    embed = discord.Embed(title="",
                          description="Current prefix: " + str(cmd),
                          colour=discord.Colour.green())
    await ctx.channel.send(embed=embed)


# ------------ CHANGE PREFIX --------- #
@client.command()
@commands.has_permissions(administrator=True)
async def changePrefix(ctx, cmd):
    try:
        if (len(cmd) == 1):
            db[str(ctx.message.guild.id)] = str(cmd)
            embed = discord.Embed(title="",
                                  description="New prefix has been set.",
                                  colour=discord.Colour.green())
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="",
                description="Prefixes cannot be longer than 1 character.",
                colour=discord.Colour.red())
            await ctx.channel.send(embed=embed, delete_after=5)
    except:
        embed = discord.Embed(
            title="",
            description="Failed to change command. Try later.",
            colour=discord.Colour.red())
        await ctx.channel.send(embed=embed, delete_after=5)


# ------------ RENAME BOT --------- #
@client.command()
async def rename(ctx, name):
    try:
        if (ctx.author.id == 743999268167352651):
            await client.user.edit(username=name)
            embed = discord.Embed(title="",
                                  description="Name Successfully Changed.",
                                  colour=discord.Colour.green())
        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(
            title="",
            description=
            "Issues with changing name. Too many requests or the name is overused.",
            colour=discord.Colour.red())
        await ctx.channel.send(embed=embed, delete_after=5)

# ------------ TICKETS ------------ #
@client.command(pass_context=True)
async def ticket(ctx):
    guild = ctx.guild
    await ctx.message.delete()
    embed = discord.Embed(
        title = 'Silverline Tickets',
        description = 'Welcome to the Ticket System, react below 📩 to make a help ticket. Personalized help will be given in the created channel. Afterwards, please close your ticket.',
        color = 0xFFFFFF
    )

    embed.set_footer(text=f"Silverline Tutoring Tickets | EIN: 88-3149458")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("📩")

    @client.event
    async def on_reaction_add(reaction, user):
      if user == "Silverline Assistant#2144":
        pass
      else:
        if reaction.emoji == "📩" and user != "Silverline Assistant#2144":
          name = '➤ Tickets'
          category1 = discord.utils.get(ctx.guild.categories, name=name)
          if user == "Silverline Assistant#2144":
            pass
          else:
            await guild.create_text_channel(name=f'ticket - {user}', category=category1)
            string = str(user).lower()
            index = string.index("#")
            final_string = string[:index] + string[index+1:]
            for server in client.guilds:
              ticket_channel = discord.utils.get(server.channels, name=f'ticket-{final_string}')
            embed = discord.Embed(
              title = 'Steps For Silverline Tutoring Help',
              description = f'Welcome to the Ticket System {user.mention}! Use this channel to ask questions to recieve personalized assistance from one of our helpers. Please be specific in the questions that you ask and provide as much as detail as possible. We will get back to as soon as possible! To close the ticket use the ~close method once your problem is solved! Rate your experience at https://g.co/kgs/S9BC6v',
              color = 0xFFFFFF
            )
            #ctx.guild.get_role(ctx.guild.id),
            print(user)
            if user == "Silverline Assistant#2144":
              pass
            else:
              await ticket_channel.set_permissions(target=user, send_messages=True, read_messages=True)
              embed.set_footer(text=f"Silverline Tutoring Tickets | EIN: 88-3149458")

              await ticket_channel.send(embed=embed)

@client.command()
async def close(ctx):
  guild = ctx.guild
  string2 = str(ctx.author).lower()
  index2 = string2.index("#")
  final_string2 = string2[:index2] + string2[index2+1:]
  for server in client.guilds:
      ticket_channel = discord.utils.get(server.channels, name=f'ticket-{final_string2}')
  channel = client.get_channel(ticket_channel.id)
  await channel.delete()
  

# ------------ WELCOME MEMBERS --------- #
@client.event
async def on_member_join(ctx):
    welcome_messages = [
        "We're delighted to have you here at Silverline, ",
        "Welcome to Silverline, ", "Great to see you, "
    ]
    used_messages = []
    number = random.randint(0, 2)
    msg = welcome_messages[number]
    while msg in used_messages:
        msg = welcome_messages[random.randint(0, 2)]
    message = f"{msg} {ctx.mention}!"
    welcome_messages.remove(msg)
    used_messages.append(msg)
    fh = open("w_messages.pkl", 'wb')
    pickle.dump(welcome_messages, fh)
    fh.close()
    fh2 = open("u_messages.pkl", 'wb')
    pickle.dump(used_messages, fh2)
    fh2.close()
    print(used_messages)
    print(welcome_messages)

    for server in client.guilds:
        welcome_channel = discord.utils.get(server.channels, name="welcome")
        rules_channel = discord.utils.get(server.channels, name="rules")
        quick_help_channel = discord.utils.get(server.channels,
                                               name="quick-help")
        forms_channel = discord.utils.get(server.channels, name="forms")
        general_channel = discord.utils.get(server.channels, name="general")
        bot_channel = discord.utils.get(server.channels, name="bot-testing")

        embed = discord.Embed(
            title="Welcome!",
            description=
            f"Welcome to Silverline Tutoring. After the 10 minute verification period has finished, feel free to look around! Check out {rules_channel.mention} for our server rules. Additionally we have a plethora of resources for students. Check out {quick_help_channel.mention} for immediate help, and {forms_channel.mention} to sign up for long term tutoring. We pride ourselves in working fast and efficiently so expect a response to either long or short term tutoring within a few hours. Be sure to also check out our entertainment channels, and feel free to share our server with others to help us in our mission. Feel free to also rate your experiences [here] (https://g.co/kgs/S9BC6v)",
            colour=0x5271FF)
        channel = ctx.guild.get_channel(795627064093966351)
    try:
       # await channel.send(message)
        await ctx.send(embed=embed)
    except:
         #await channel.send(message)
        pass

# ------------- SET TIME ------------- #
def send(ctx, debate, chess):
    now1 = datetime.now()
    current_date = now1.astimezone(est).strftime("%m-%d")
    index = int(db["index"])
    index = int(db["index1"])
    embed = ""
    ping = ""
    if debate == True:
        embed = discord.Embed(
            title="Weekily Debate Question " + str(current_date),
            description="**Resolved** " + db["debateQuestions"][int(index)],
            colour=0x5271FF)
        embed.set_footer(text="Question valid for next 7 days.")
        ping = get(ctx.guild.roles, name='Debate Ping')
    if chess == True:
        embed = discord.Embed(title="Weekily Chess Question " +
                              str(current_date),
                              description=db["chessQuestions"][int(index)],
                              colour=0x5271FF)
        embed.set_footer(text="Refreshed every " +
                         str(db['chessQuestionsDay']) + " @ " +
                         str(db['chessQuestionsTime']))
        ping = get(ctx.guild.roles, name='Chess Game Ping')
    client.loop.create_task(ctx.send(ping.mention))
    client.loop.create_task(ctx.send(embed=embed))


# periodic
def checkTime():
    global current_date
    global current_time
    threading.Timer(1, checkTime).start()
    now1 = datetime.now()
    current_date = now1.astimezone(est).strftime("%m-%d")
    current_time = now1.astimezone(est).strftime("%H:%M:%S")
    index = int(db["index"])
    index1 = int(db["index1"])
    # debate question
    if (datetime.today().strftime('%A') == db['debateQuestionsDay']
            and current_time == db['debateQuestionsTime']):
        channel = client.get_channel(907690281263050794)
        db["index"] = index + 1
        send(channel, True, False)
    if (datetime.today().strftime('%A') == db['chessQuestionsDay']
            and current_time == db['chessQuestionsTime']):
        channel = client.get_channel(816466835901120514)
        send(channel, False, True)
        db["index1"] = index1 + 1


checkTime()

# -------- RESOURCES -------- #


def buttons(message, l, r):
    def check(reaction, user):
        if reaction.message.id != message.id or user == client.user:
            return False
        if l and reaction.emoji == "⏪":
            return True
        if r and reaction.emoji == "⏩":
            return True
        return False

    return check


@client.command()
async def resources(ctx):
    pages = []
    embedVar = discord.Embed(title=f"Silverline Tutoring Resources",
                             colour=discord.Colour.blue())
    embedVar.add_field(
        name="Math Resource",
        value=
        "Resource #1\nResource #2\nResource #3\nResource #4\nResource #5\nResource #6\nResource #7\nResource #8\nResource #9\nResource #10"
    )
    embedVar2 = discord.Embed(title=f"Silverline Tutoring Resources",
                              colour=discord.Colour.blue())
    embedVar2.add_field(
        name="Science Resources",
        value=
        "Resource #1\nResource #2\nResource #3\nResource #4\nResource #5\nResource #6\nResource #7\nResource #8\nResource #9\nResource #10"
    )
    embedVar3 = discord.Embed(title=f"Silverline Tutoring Resources",
                              colour=discord.Colour.blue())
    embedVar3.add_field(
        name="History Resources",
        value=
        "Resource #1\nResource #2\nResource #3\nResource #4\nResource #5\nResource #6\nResource #7\nResource #8\nResource #9\nResource #10"
    )
    pages.append(embedVar)
    pages.append(embedVar2)
    pages.append(embedVar3)
    page = 0
    left = "⏪"
    right = "⏩"
    while True:
        msg = await ctx.send(embed=pages[(page)])
        l_reaction = page != 0
        r_reaction = page <= len(pages) - 1
        if l_reaction:
            await msg.add_reaction(left)
        if r_reaction:
            if page == (len(pages) - 1):
                react = await client.wait_for('reaction_add',
                                              check=buttons(
                                                  msg, l_reaction, r_reaction))
            else:
                await msg.add_reaction(right)
                react = await client.wait_for('reaction_add',
                                              check=buttons(
                                                  msg, l_reaction, r_reaction))

        if str(react[0]) == left:
            page -= 1
        elif str(react[0]) == right:
            page += 1

        await msg.delete()


# ------------ COMMAND ERROR --------- #
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        embed = discord.Embed(title="",
                              description="Command not found! Use " +
                              str(db[str(ctx.guild.id)]) +
                              "help for possible commands.",
                              colour=discord.Colour.red())
        await ctx.channel.send(embed=embed, delete_after=5)
        return
    raise error


# ------------- COGS ------------- #
startup_extensions = [
    "chess", "debate", "help", "dm", "role", "embeder", "pair"
]
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

online()
client.run(os.environ.get("TOKEN"))
