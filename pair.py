from replit import db
import discord
from discord.ext import commands, tasks

class Pair(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def pair(self, ctx, subject, user: discord.User, user2: discord.User, *args):
    msg = ""
    for server in self.client.guilds:
      math = discord.utils.get(server.channels, name = "math-tutoring")
      science = discord.utils.get(server.channels, name = "science-tutoring")
      history = discord.utils.get(server.channels, name = "history-tutoring")
      language = discord.utils.get(server.channels, name = "language-tutoring")
      coding = discord.utils.get(server.channels, name = "coding-tutoring")
      sat_act = discord.utils.get(server.channels, name = "sat-act-tutoring")
      chess = discord.utils.get(server.channels, name = "chess-tutoring")
      economics = discord.utils.get(server.channels, name = "economics-tutoring")
      bot_channel = discord.utils.get(server.channels, name = "bot-testing")

    if subject.lower() == "math":
      channel = self.client.get_channel(math.id)
    elif subject.lower() == "science":
      channel = self.client.get_channel(science.id)
    elif subject.lower() == "history":
      channel = self.client.get_channel(history.id)
    elif subject.lower() == "language":
      channel = self.client.get_channel(language.id)
    elif subject.lower() == "coding":
      channel = self.client.get_channel(coding.id)
    elif subject.lower() == "sat_act":
      channel = self.client.get_channel(sat_act.id)
    elif subject.lower() == "chess":
      channel = self.client.get_channel(chess.id)
    elif subject.lower() == "economics":
      channel = self.client.get_channel(economics.id)
    elif subject.lower() == "bot-testing":
      channel = self.client.get_channel(bot_channel.id)

    msg = f"{user.mention} is paired with {user2.mention} in {subject}. Please reach out to {user.mention} to get started!"
    await channel.send(msg)
    
def setup(client):
  client.add_cog(Pair(client))