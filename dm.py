from replit import db
import discord
from discord.ext import commands, tasks

class DM(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def dm(self, ctx, user: discord.User, *args):
    msg = ""
    if(ctx.channel.id == 999740442117668975):
      try:
        channel = await user.create_dm()
        for i in range(len(args)):
          msg += (args[i] + " ")
        final = msg.replace("enter", " \n ")
        msg = discord.Embed(title = "**Message from Silverline**", description = final, colour = 0x5271FF)
        await channel.send(embed = msg)
        embed = discord.Embed(title = "Status", description = "`" + str(user.name) + "`" + " has recieved the message.", colour = discord.Colour.green())
        await ctx.channel.send(embed = embed)
      except:
        embed = discord.Embed(title = "Status", description = "`" + str(user.name) + "`" + " has not recieved the message. Member has dms closed or needs to be contacted manually.", colour = discord.Colour.red())
        await ctx.channel.send(embed = embed)
    else:
      embed = discord.Embed(title = "Status", description = "`" + str(user.name) + "`" + " has not recieved the message because dms are not authorized to be sent without #dm-members channel.", colour = discord.Colour.red())
      await ctx.channel.send(embed = embed)
  

  @commands.command()
  async def dm_role(self, ctx, d_role, *args):
    msg = ""
    for i in range(len(args)):
      msg += (args[i] + " ")
    if(ctx.channel.id == 999740442117668975):
      members = ctx.guild.members
      role = discord.utils.find(lambda r: r.name == f'{d_role}', ctx.message.guild.roles)
      print(d_role)
      for member in members:
        if role in member.roles:
          channel = await member.create_dm()
          final = msg.replace("enter", " \n ")
          try:
            print("in the method")
            msgs = discord.Embed(title = "**Message from Silverline**", description = final, colour = 0x5271FF)
              
            embed = discord.Embed(title = "Status", description = "`" + str(member.name) + "`" + " has recieved the message.", colour = discord.Colour.green())
            await channel.send(embed = msgs)
            await ctx.channel.send(embed = embed)
          except:
            embed = discord.Embed(title = "Status", description = "`" + str(member.name) + "`" + " has not recieved the message. Member has dms closed or needs to be contacted manually.", colour = discord.Colour.red())
            await ctx.channel.send(embed = embed)
    elif(ctx.channel.id != 999740442117668975):
      embed = discord.Embed(title = "Status", description = "`" + str(d_role) + "`" + " have not recieved the message because dms are not authorized to be sent without #dm-members channel.", colour = discord.Colour.red())
      await ctx.channel.send(embed = embed)

def setup(client):
  client.add_cog(DM(client))