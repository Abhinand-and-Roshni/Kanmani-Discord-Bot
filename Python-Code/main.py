#FINAL KANMANI BOT
import discord
import asyncio
import random
import praw
from discord.ext import commands, tasks
from discord.utils import get
from kanmani_alive import kanmani_alive


commandinfo = "Here are a list of commands you can try!\n\n\n`!!pomo` : Pomodoro is a productivity technique which helps you focus. It involves following 25 minutes of work followed by a 5 minute refreshing break. Try the pomodoro technique using this command.\n\n`!!vent` : Want to vent but don't know to whom? Vent in my dm and I'll post it to the venting channel anonymously so you can get it off your chest!\n\n`!!reminder` : Remind yourself using this command! Write the duration after which you want to be reminder with the first letter of the timeperiod and follow it up with what you want to be reminded about.\nHere is an example : `!!reminder 15m Get Dinner!`\n  seconds: s  |  minutes: m  |  hours: h  |  days:day  \n\n`!!meme` : Want to laugh a bit? Try it out.\n\n`!!coding` : Want some cool coding tips to enhance your knowledge? Try this out!\n\n`!!motivate` : Are you in need for some inspiring words haha. This command gives you some of that plus some more.\n\n`!!study` : Your study motivation posted by strangers!\n\n"
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
water_emoji = "\U0001F6B0" #water
laptop_emoji = "\U0001F4BB" #mac emoji
clown_emoji = "\U0001F921" #clownnn
furious_emoji = "\U0001F624" #blowing air out of nose
cowboy_emoji = "\U0001F920" #cowboy smiling
tick_emoji = "\U00002705" #tick mark/good/done
X_emoji = "\U0000274C" #X mark/incomplete/bad
crying_emoji = "\U0001F62D" #tears flooding down face
exclamation_em = "\U0000203C" #double !!

#BOT LOGIN
client = commands.Bot(command_prefix='!!')
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('ok !!kanmani'))
    print(' {0.user} is here!'.format(client))

#KEYWORDS AND BOT LISTENING
@client.event
async def on_message(message):
  await client.process_commands(message)
  if message.author == client.user:
    return
  if message.content.startswith('!!hi'):
    await message.channel.send('Hello, ' + message.author.mention +' '+ heart_emoji + ' !')
  if message.content.startswith('!!thank'):
    await message.channel.send("You're welcome " + message.author.mention + '! ' + heart_emoji)


#Reminders 
@client.command(case_insensitive = True, aliases = ["remind", "remindme", "Reminder", "Remind", "remainder"])
@commands.bot_has_permissions(attach_files = True, embed_links = True)
async def reminder(ctx, time, *, reminder):
    print(time)
    print(reminder)
    user = ctx.message.author
    rem_em = discord.Embed(title = "Reminder!", description = reminder, colour=random.randint(0, 0xffffff))
    rem_em.set_footer(text="Kanmani | Be mindful | !!kanmani ", icon_url=f"{client.user.avatar_url}")
    seconds = 0
    if reminder is None:
        rem_em.add_field(name='!!Warning!!', value='Please specify what do you want me to remind you about.') # Error message
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        rem_em.add_field(name='!!Warning!!', value='Specify a proper duration. \n Example: `!!reminder 15m Get the groceries from the car!`')
    elif seconds < 10:
        rem_em.add_field(name='!!Warning!!',value='You need a reminder for that time period? The minimum time is 5 mins for a reminder. Try again  \n Example: `!!reminder 15m Get the groceries from the car!`')
    elif seconds > 172800:
        rem_em.add_field(name='!!Warning!!', value='That duration is too long!\nMaximum duration is 2 days.')
    else:
        await ctx.send(f"{ctx.author.mention}, I will remind you regarding  `{reminder}` in {counter}. Have a great day!")
        await asyncio.sleep(seconds)
        await ctx.send(f"Attention, {ctx.author.mention}!")
        em_reminder = await ctx.send(embed = rem_em)
        await em_reminder.add_reaction(exclamation_em)
        await em_reminder.add_reaction(tick_emoji)
        await em_reminder.add_reaction(X_emoji)
        await em_reminder.add_reaction(heart_emoji)
        return
    await ctx.send(embed=rem_em)

#POMODORO TECHNIQUE
@client.command()
async def pomo(ctx):
  await ctx.send(ctx.author.mention)
  em_pomo_start = discord.Embed(
    title='Pomodoro starts now!',
    description = f'{ctx.author.mention}\n\n Time for you to buckle down and get productive!', 
    color = discord.Colour.red()
    )
  em_pomo_start.set_thumbnail(url = "https://miro.medium.com/max/9216/1*d0eyYQyQUVFqsajOhWkhPw.jpeg")
  em_pomo_start.add_field(name = f"You can do this!", value = 'Are you ready?', inline = True )
  pomo_start = await ctx.send(embed = em_pomo_start)
  await pomo_start.add_reaction(partypop_emoji)
  await pomo_start.add_reaction(shh_emoji) 
  await pomo_start.add_reaction(book_emoji)
  await asyncio.sleep(1)
  await ctx.send(ctx.author.mention)
  em_pomo_break = discord.Embed(
    title='Congratulations!',
    description = f'{ctx.author.mention}\n\n Your 25 minutes of productivity has been completed!', 
    color = discord.Colour.green()
    )
  em_pomo_break.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScmF3m04HsD3pSEOC87mlgIiHBHerPXfDUQLFBsR0hTv-8lfzM1nEiLfh6msmxNZq0AlzSLS_E0s345g&usqp=CAU")
  em_pomo_break.add_field(name = f"Now time for your 5 minute break!", value = 'Enjoy!', inline = True )
  pomo_break = await ctx.send(embed = em_pomo_break)
  await pomo_break.add_reaction(clap_emoji) 
  await pomo_break.add_reaction(partypop_emoji)
  await pomo_break.add_reaction(star_struck)
  await asyncio.sleep(1)
  await ctx.send(ctx.author.mention)
  em_pomo_bye = discord.Embed(
    title='Well Done!',
    description = f'{ctx.author.mention}\n\n Hope your break was refreshing!', 
    color = discord.Colour.blue()
    )
  em_pomo_bye.set_thumbnail(url=ctx.author.avatar_url_as(format="png"))
  em_pomo_bye.add_field(name = f"Type in the Pomodoro command so I know you're back.", value = 'See you soon!', inline = True )
  pomo_bye = await ctx.send(embed = em_pomo_bye)
  await pomo_bye.add_reaction(heart_emoji) 
  await pomo_bye.add_reaction(handwave_emoji)

#WATER REMINDERS
@tasks.loop(hours = 2.1)
async def water_rem():
  message_channel = client.get_channel(854294448439951411) #CHANNEL ID GOES HERE
  print(f"Got channel {message_channel}")
  await message_channel.send('Hi @everyone! You know what time it is!! \n\n **hydration time!!**')
  remindermsg = discord.Embed(
    title='Water Reminder!',
    description = f'@everyone\n\n Hope you are doing well! \n -Drink water\n -Stretch your body\n -Rest your eyes for 5 seconds\n -Straighten your back\n -You are doing great! Keep it up!\n\n\n **Kanmani is here for you!**', 
    color = discord.Colour.blue()
    )
  remindermsg.set_thumbnail(url="https://image.shutterstock.com/image-vector/hand-drawn-doodle-style-cartoon-260nw-1170555406.jpg")
  remindermsg.add_field(name ="If you need me just call me.", value = '!!kanmani', inline = True )

  em_rem_msg = await message_channel.send(embed = remindermsg)
  for i in range(20):
    em_rem_edit = discord.Embed(
      title='Water Reminder!',
      description = f'@everyone\n\n Hope you are doing well! \n -Drink water\n -Stretch your body\n -Rest your eyes for 5 seconds\n -Straighten your back\n -You are doing great! Keep it up!\n\n\n **Kanmani is here for you!**', 
      colour=random.randint(0, 0xffffff)
    )
    em_rem_edit.set_thumbnail(url="https://image.shutterstock.com/image-vector/hand-drawn-doodle-style-cartoon-260nw-1170555406.jpg")
    em_rem_edit.add_field(name ="If you need me just call me.", value = '!!kanmani', inline = True )
    await asyncio.sleep(0.01)
    await em_rem_msg.edit(embed = em_rem_edit)
  await em_rem_msg.add_reaction(water_emoji)
  await em_rem_msg.add_reaction(tick_emoji)
  await em_rem_msg.add_reaction(X_emoji)
  await em_rem_msg.add_reaction(heart_emoji)

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

#Kanmani commands
@client.command(pass_context = True, aliases = [ "Inf", "infor", "information", "Info", "commandss", "comands"])
async def info(ctx):
  em_com = discord.Embed(
    title = "Kanmani's Ability",
    description = commandinfo,
    colour=random.randint(0, 0xffffff)
  )
  em_com.set_footer(text = "Kanmani | Be mindful | !!kanmani", icon_url=f"{client.user.avatar_url}")
  react_com= await ctx.send(embed = em_com)
  await react_com.add_reaction(clap_emoji)
  await react_com.add_reaction(star_struck)



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

#REDDIT: MOTIVATION, CODING AND PRODUCTIVITY
#coding tips subreddit#
@client.command()
async def coding(ctx):
  reddit = praw.Reddit(client_id = 'M9RzCP9qFbpWDQ', client_secret = 'm7kK9grNlNa0DRsNjGOqEEEXdEm_9g', user_agent = 'try-all')
  code_sub = reddit.subreddit('LearnProgramming').top()
  post_to_pick = random.randint(1, 100)
  for x in range(0, post_to_pick):
    submission = next(n for n in code_sub if not n.stickied)
  resp_msg = await ctx.send(ctx.author.mention + " here is what you asked for!")
  await resp_msg.add_reaction(heart_emoji)
  em_codingtip = discord.Embed(
    title = 'Random Coding Tip',
    description = f'{submission.url}',
    color=random.randint(0,0xffffff)
  )
  em_codingtip.set_thumbnail(url=ctx.author.avatar_url_as(format="png"))
  em_codingtip.set_footer(text = "brought to you by r/LearnProgramming")
  codingtip_msg = await ctx.send(embed = em_codingtip)
  await codingtip_msg.add_reaction(laptop_emoji)
  await codingtip_msg.add_reaction(heart_emoji)
  await codingtip_msg.add_reaction(star_struck)

#motivation subreddit#
@client.command()
async def motivate(ctx):
  reddit = praw.Reddit(client_id = 'M9RzCP9qFbpWDQ', client_secret = 'm7kK9grNlNa0DRsNjGOqEEEXdEm_9g', user_agent = 'try-all')
  motiv_sub = reddit.subreddit('MotivationalPics').top()
  post_to_pick = random.randint(1, 100)
  for x in range(0, post_to_pick):
    submission = next(n for n in motiv_sub if not n.stickied)
  resp_msg = await ctx.send(ctx.author.mention + " here is what you asked for!")
  await resp_msg.add_reaction(heart_emoji)
  em_motiv = discord.Embed(
    title = 'Motivation 101',
    description = 'Here is some motivation for you!',
    color=random.randint(0,0xffffff)
  )
  em_motiv.set_image(url = submission.url )
  em_motiv.set_footer(text = "brought to you by r/MotivationalPics")
  motiv_msg = await ctx.send(embed = em_motiv)
  await motiv_msg.add_reaction(heart_emoji)
  await motiv_msg.add_reaction(star_struck)
  await motiv_msg.add_reaction(partypop_emoji)
  await motiv_msg.add_reaction(tick_emoji)

#meme reddit#
@client.command()
async def meme(ctx):
  reddit = praw.Reddit(client_id = 'M9RzCP9qFbpWDQ', client_secret = 'm7kK9grNlNa0DRsNjGOqEEEXdEm_9g', user_agent = 'try-all')
  memes_sub = reddit.subreddit('CollegeHomeworkTips').top()
  post_to_pick = random.randint(1, 100)
  for x in range(0, post_to_pick):
    submission = next(n for n in memes_sub if not n.stickied)
  resp_msg = await ctx.send(ctx.author.mention + " here is what you asked for!")
  await resp_msg.add_reaction(heart_emoji)
  em_memes = discord.Embed(
    title = 'Here take a meme, kanna.',
    description = 'Is this relatable lol',
    color=random.randint(0,0xffffff)
  )
  em_memes.set_image(url = submission.url )
  em_memes.set_footer(text = "brought to you by r/CollegeHomeworkTips")
  memes_msg = await ctx.send(embed = em_memes)
  await memes_msg.add_reaction(clown_emoji)
  await memes_msg.add_reaction(crying_emoji)
  await memes_msg.add_reaction(cowboy_emoji)

#quotes subreddit#
@client.command()
async def study(ctx):
  reddit = praw.Reddit(client_id = 'M9RzCP9qFbpWDQ', client_secret = 'm7kK9grNlNa0DRsNjGOqEEEXdEm_9g', user_agent = 'try-all')
  quotes_sub = reddit.subreddit('QuotesPorn').top()
  post_to_pick = random.randint(1, 100)
  for x in range(0, post_to_pick):
    submission = next(n for n in quotes_sub if not n.stickied)
  resp_msg = await ctx.send(ctx.author.mention + " here is what you asked for!")
  await resp_msg.add_reaction(heart_emoji)
  em_quotes = discord.Embed(
    title = 'Get Productive',
    description = 'Straighten your back and take a sip of water, its time to get productive!',
    color=random.randint(0,0xffffff)
  )
  em_quotes.set_image(url = submission.url)
  em_quotes.set_thumbnail(url=ctx.author.avatar_url_as(format="png"))
  em_quotes.set_footer(text = "brought to you by r/QuotesPorn")
  quotes_msg = await ctx.send(embed = em_quotes)
  await quotes_msg.add_reaction(book_emoji)
  await quotes_msg.add_reaction(tick_emoji)
  await quotes_msg.add_reaction(laptop_emoji)

#ok kanmani
@client.command(pass_context = True, aliases = ["Kanmani", "kanmanii kamani", "Kanmanii"])
async def kanmani(ctx):
  em_ok = discord.Embed(title = "Kanmani", description = f"**Your Wellness and Productivity Bot**\n\nHi {ctx.author.mention}! I'm a bot designed by students for students! From productivity to chilling - Kanmani's got your back.\n\nDo you want to know what I can do? Try the `!!info` command!\nHave a good day!", color = random.randint(0,0xffffff))
  em_ok.set_thumbnail(url = ctx.author.avatar_url_as(format = "png"))
  em_ok.set_footer(text = "Kanmani | Be mindful | !!kanmani", icon_url=f"{client.user.avatar_url}")
  msg_em_ok = await ctx.send(embed = em_ok)
  await msg_em_ok.add_reaction(clap_emoji)
  await msg_em_ok.add_reaction(heart_emoji)













#REST YOUR EYES
@tasks.loop(hours = 3)
async def eyes_relax():
  message_channel = client.get_channel(854294448439951411) #CHANNEL ID GOES HERE
  print(f"Got channel {message_channel}")
  await asyncio.sleep(504)
  await message_channel.send('Hi @everyone! Time to rest your vision providers')
  eyesmsg = discord.Embed(
    title='Rest your eyes!',
    description = f'@everyone\n\n**LOOK AWAY FROM THE SCREEN AND LOOK AROUND**\n Looking at the screen for long periods of team are extremely harmful. Do your eyes a favour and look at the furthest wall lol', 
    color = discord.Colour.red()
    )
  eyesmsg.set_thumbnail(url="https://image.shutterstock.com/image-vector/sick-cartoon-eyes-vector-illustration-260nw-177695450.jpg")
  eyesmsg.add_field(name ="If you need me just call me.", value = '!!ok kanmani', inline = True )

  em_eyes_msg = await message_channel.send(embed = eyesmsg)
  
  await asyncio.sleep(15)
  eyesmsg = discord.Embed(
    title='Your eyes thank you',
    description = f'@everyone\n\n Have a wonderful day!', 
    color = discord.Colour.green()
    ) 
  eyesmsg.set_thumbnail(url="https://image.shutterstock.com/image-vector/cartoon-illustration-giant-eye-meditating-260nw-655693876.jpg")
  eyesmsg.add_field(name ="If you need me just call me.", value = '!!ok kanmani', inline = True )

  em_eyes_msg = await message_channel.send(embed = eyesmsg)
  await em_eyes_msg.add_reaction(tick_emoji)
  await em_eyes_msg.add_reaction(X_emoji)
@eyes_relax.before_loop
async def before_eyes():
  await client.wait_until_ready()
  print("Finished wait.")


#######STUFF FOR RUNNING THE BOT WITH THE FUNCTIONS##############

eyes_relax.start()
water_rem.start()
kanmani_alive()
#RUNNING THE BOT
client.run('#') #Token goes here
