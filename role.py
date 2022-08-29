from replit import db
import discord
from discord.ext import commands, tasks

class Role(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def id(self, message, user : discord.User):
    id = user.id
    await message.channel.send(id)

  @commands.command()
  async def applyRole(ctx):
    members = ctx.guild.members
    role = discord.utils.find(lambda r: r.name == 'Student', ctx.message.guild.roles)
    for member in members:
      if role not in member.roles:
        await member.add_roles(role) # Adds the role to the member
        print("added " + str(member))

def setup(client):
  client.add_cog(Role(client))