#FINAL KANMANI BOT
import discord
from discord.ext import commands, tasks
from discord.utils import get
import asyncio
import random

#EMOJI TO USE
shh_emoji = '\U0001F910' #be quiet emoji
book_emoji= "\U0001F4DA" #stack of books emoji
partypop_emoji = "\U0001F389" #party popper
clap_emoji ='\U0001f44f' #clapping emoji
heart_emoji='\U0001f49c' #heart emoji
star_struck='\U0001f929' #star struck emoji
angry_emoji='\U0001f621' #angry emoji
heart_emoji='\U0001F497' #heart sparkle
handwave_emoji = '\U0001F44B' #waving hand



client = commands.Bot(command_prefix='!!')
#BOT LOGIN
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('!!ok kanmani'))
    print(' {0.user} is here!'.format(client))

#POMODORO TECHNIQUE
@client.command()
async def pomo(ctx):
  await ctx.send(ctx.author.mention)
  em_pomo_start = discord.Embed(
    title='Pomodoro starts now!',
    description = f'{ctx.author.mention}\n\n Time for you to buckle down and get productive!', 
    color = discord.Colour.red()
    )
  em_pomo_start.add_field(name = f"You can do this!", value = 'Are you ready?', inline = True )
  pomo_start = await ctx.send(embed = em_pomo_start)
  await pomo_start.add_reaction(partypop_emoji)
  await pomo_start.add_reaction(shh_emoji) 
  await pomo_start.add_reaction(book_emoji)
  await asyncio.sleep(2)
  await ctx.send(ctx.author.mention)
  em_pomo_break = discord.Embed(
    title='Congratulations!',
    description = f'{ctx.author.mention}\n\n Your 25 minutes of productivity has been completed!', 
    color = discord.Colour.green()
    )
  em_pomo_break.add_field(name = f"Now time for your 5 minute break!", value = 'Enjoy!', inline = True )
  pomo_break = await ctx.send(embed = em_pomo_break)
  await pomo_break.add_reaction(clap_emoji) 
  await pomo_break.add_reaction(partypop_emoji)
  await pomo_break.add_reaction(star_struck)
  await asyncio.sleep(2)
  await ctx.send(ctx.author.mention)
  em_pomo_bye = discord.Embed(
    title='Well Done!',
    description = f'{ctx.author.mention}\n\n Hope your break was refreshing!', 
    color = discord.Colour.blue()
    )
  em_pomo_bye.add_field(name = f"Type in the Pomodoro command so I know you're back.", value = 'See you soon!', inline = True )
  pomo_bye = await ctx.send(embed = em_pomo_bye)
  await pomo_bye.add_reaction(heart_emoji) 
  await pomo_bye.add_reaction(handwave_emoji)

#WATER REMINDERS
@tasks.loop(hours = 2)
async def water_rem():
  message_channel = client.get_channel(854294448439951411) #CHANNEL ID GOES HERE
  print(f"Got channel {message_channel}")
  await message_channel.send('@everyone' + "\n\n**Hey!**\nTake care of your body! Drink some water and stretch your body :)")

@water_rem.before_loop
async def before():
  await client.wait_until_ready()
  print("Finished wait.")


#ADMIN CLEAR MSG 
@client.command()
@commands.has_permissions(administrator=True)
async def clearit(ctx, amount=2):
  await ctx.channel.purge(limit = amount+1)
  await ctx.send('Messages have been deleted!')
  await asyncio.sleep(1.25)
  await ctx.channel.purge(limit = 1)

#VENTING FEATURE
@client.command(name='vent')
async def vent(ctx):
  if ctx.channel.type==discord.ChannelType.private:
    mbed=discord.Embed(
      title='Vent out your feelings!',
      description='** Note: Any slur will not be tolerated by us. ** ',
      color=random.randint(0,0xffffff)
    )
    mbed.set_thumbnail(url='https://cdn.discordapp.com/attachments/854294448439951411/855083404953518100/3a71df84c3736bbe8c548751ba057f59.png')
    demand=await ctx.send(embed=mbed)
    try:
      msg=await client.wait_for(
        'message',
        timeout=1000,
        check=lambda message: message.author == ctx.author and message.channel==ctx.channel
      )
      if msg:
        channel=get(client.get_all_channels(), guild__name='Bot_Testing',name='venting_kan')
        mbed=discord.Embed(
          title='New Vent',
          description=f'{msg.content}',
          colour=random.randint(0, 0xffffff)
        )
        mbed.add_field(name='Feel free to give your advice in the `advice` channel. Abuse will lead to your suspension from the server.',value=':smile:',inline=False)
        mbed.set_thumbnail(url='https://cdn.discordapp.com/attachments/854294448439951411/855083404953518100/3a71df84c3736bbe8c548751ba057f59.png')
        abc=await channel.send(embed=mbed)
        await abc.add_reaction(star_struck)
        await abc.add_reaction(heart_emoji)
        await abc.add_reaction(clap_emoji)
        await abc.add_reaction(angry_emoji)
        await demand.delete()

    except asyncio.TimeoutError:
      await ctx.send('You have not vented anything for way too long. Kanmani has to return now. Sorry!',delete_after=5)
      await demand.delete()

  else:
    mm=discord.Embed(
      title='Oops! Wrong chat',
      description='Please use the `!!vent` command in my DM, and it will be anonymously posted in the venting channel!',
      color=random.randint(0,0xffffff)
    )
    mm.set_thumbnail(url='https://cdn.discordapp.com/attachments/854294448439951411/855083404953518100/3a71df84c3736bbe8c548751ba057f59.png') 
    await ctx.send(embed=mm)       



#STUFF FOR RUNNING THE BOT WITH THE FUNCTIONS

water_rem.start()
#RUNNING THE BOT
client.run('ODU1MDAwNzg0MDk4MTY0Nzg2.YMsHiA.dwmKVu_i0BcNsEPmeFAjYOcGa2s') 