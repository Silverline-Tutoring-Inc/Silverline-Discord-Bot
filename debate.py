from replit import db
import discord
from discord.ext import commands, tasks

class Debate(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def changeDebateDay(self, ctx, time):
    try:
      if(ctx.channel.id == 998341658561224828):
        db["debateQuestionsDay"] = time
        embed = discord.Embed(title = "", description = "Debate questions will be sent on " + db["debateQuestionsDay"], colour = discord.Colour.green())
      await ctx.channel.send(embed = embed)
    except:
      embed = discord.Embed(title = "", description = "Try again later. Contact tarun#9792 if issue persists.", colour = discord.Colour.red())
      await ctx.channel.send(embed = embed, delete_after = 5)
  
  @commands.command()
  async def changeDebateTime(self, ctx, time):
    try:
      if(ctx.channel.id == 998341658561224828):
        embed1 = discord.Embed(title = "", description = "Time must be submited as HH:MM:SS in 24H format otherwise bot will fail.", colour = 0xdb9512)
        await ctx.channel.send(embed = embed1, delete_after = 5)
        db["debateQuestionsTime"] = time
        embed = discord.Embed(title = "", description = "Questions will be released on " + db["debateQuestionsDay"] + " @ " + db["debateQuestionsTime"], colour = discord.Colour.green())
      await ctx.channel.send(embed = embed)
    except:
      embed = discord.Embed(title = "", description = "Try again later. Contact tarun#9792 if issue persists.", colour = discord.Colour.red())
      await ctx.channel.send(embed = embed)
  
  @commands.command()
  async def testDebateQuestions(self, ctx, index):
    try:
      if(ctx.channel.id == 998341658561224828):
        print(len(db["debateQuestions"]))
        await ctx.send(db["debateQuestions"][int(index)])
        
    except:
      embed = discord.Embed(title = "", description = "Try again later. Contact tarun#9792 if issue persists.", colour = discord.Colour.red())
      await ctx.channel.send(embed = embed)
  
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def addDebateQuestion(self, ctx, *, question):
    try:
      if(ctx.channel.id == 998341658561224828):
        list = db["debateQuestions"]
        list.append(question)
        db["debateQuestions"] = list
      embed = discord.Embed(title = "", description = "Question Added.", colour = discord.Colour.green())
      await ctx.channel.send(embed = embed)
    except:
      embed = discord.Embed(title = "", description = "Must be admin to submit a question.", colour = discord.Colour.red())
      await ctx.channel.send(embed = embed)
  
  @commands.command()
  async def showDebateQuestions(self, ctx):
    try:
      if(ctx.channel.id == 998341658561224828):
        for i in range(len(db["debateQuestions"])):
          question = db["debateQuestions"][i]
          await ctx.send("**" + str(i+1) + ".** " + question)
    except:
      embed = discord.Embed(title = "", description = "Try again later.", colour = discord.Colour.red())
      await ctx.channel.send(embed = embed)
  
  @commands.command()
  async def removeDebateQuestion(self, ctx, num):
    
      if(ctx.channel.id == 998341658561224828):
        list = db["debateQuestions"]
        removed = list.pop(int(num)-1)
        db["debateQuestions"] = list
        embed = discord.Embed(title = "", description = "Question popped (removed). Popped question: " + removed, colour = discord.Colour.green())
        await ctx.channel.send(embed = embed)

def setup(client):
  client.add_cog(Debate(client))