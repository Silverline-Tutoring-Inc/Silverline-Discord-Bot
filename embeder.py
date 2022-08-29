from replit import db
import discord
from discord.ext import commands, tasks

class Embeder(commands.Cog):
  def __init__(self, client):
    self.client = client

  # created emebeds that are custom
  @commands.command()
  async def embeder(self, ctx, titleA, *args):
    await ctx.message.delete()
    msg = ""
    for i in range(len(args)):
      msg += (args[i] + " ")
    final = msg.replace("enter", " \n ")
    embed = discord.Embed(title = titleA, description = final, colour = 0xdb9512)
    await ctx.channel.send(embed = embed)

def setup(client):
  client.add_cog(Embeder(client))