from replit import db
import discord
from discord.ext import commands, tasks

class Help(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def help(self, message):
    result = "\n"
    cmd = db[str(message.guild.id)]
    list_msg ="**Silverline Assistant Help Menu** \n"
    embed = discord.Embed(title =  list_msg, description = ''.join(result), colour = 0xFFFFFF)        
    embed.add_field(name="\n**Learn More:**", value="[Visit our website](https://silverlinetutoring.org/)", inline = False)    
    embed.add_field(name="\n**Summoning The Bot:**", value=f"> Use the command " + db[str(message.guild.id)] + " to summon the bot\n> default prefix is > \n> use " + db[str(message.guild.id)] + "changePrefix to change the prefx", inline = False)    
    if(message.channel.id == 998341658561224828):
      embed.add_field(name="**Commands (Part 1):**", value="Commands for admins: \n\n> " + cmd + "get_prefix [message] - returns the message's id \n> "+ cmd + "on_message [message] - used to send a message when the prfx error is resolved \n> " + cmd + "on_ready - changes presence of bot \n> " + cmd + "on_guild_join [guild] - occurs during the presence of guild \n> " + cmd + "broadcast [message] - broadcast message to the server \n> " + cmd + "changeDebateDay [day] - changes the day for the daily release of debate question \n> " + cmd + "changeDebateTime [time] - changes the time that the debate question is released on the set day, insert as HH:MM:SS in 24H format \n> " + cmd + "testDebateQuestion [index] - ignore if not Tarun \n> " + cmd + "addDebateQuestion [question] - adds a debate question to list \n> " + cmd + "showDebateQuestions - shows all debate questions but might take some time to send because each needs to be sent individually (too long for discord to be sent in one msg) \n> " + cmd + "removeDebateQuestion [question number] - use showDebateQuestions and after seeing the number next to each question, remove a question by inputing that value rules", inline = False)
      embed.add_field(name = "**Commands (Part 2):**", value = "Commands for admins: \n\n> " + cmd + "prefix - returns the current prefix \n> " + cmd + "changePrefix [command] - changes the current prefix \n> " + cmd + "rename [name] - renames the bot \n> " + cmd + "on_member_join - welcomes members into the server \n> " + cmd + "send - sends the debate question in the server and pings the debate role \n> " + cmd + "checkTime - checks the current time \n> " + cmd + "id [message, user] - returns the id of the message \n> " + cmd + "applyRole - adds the Student role to an member that currently doesn't have it \n> " + cmd + "dm [message, user] - allows user to dm the user through the bot \n> " + cmd + "dm_role [message, role] - allows the user to dm all of the members that contain the specific role through the bot \n> " + cmd + "embeder [message] - embeds the message given", inline = False)
    embed.set_footer(text = "EIN: 88-3149458")
    await message.channel.send(embed = embed)
    
def setup(client):
  client.add_cog(Help(client))