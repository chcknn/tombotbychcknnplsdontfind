import discord

TOKEN = ('NTEzMzQwMDkxNjgzMzA3NTMx.DuBdGA.0UTbwPChl99bMTfvR7KdpDZevVQ')

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('/elo'):
        msg = 'Siemka! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('/mem'):
        msg = 'https://www.reddit.com/r/memes/comments/a14jbf/lol_but_no_offense_guys_i_own_an_android_too_its Oto twój mem, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('/pomoc'):
        msg = '/elo - Bot mówi ci "Siemka! (tu cie pinguje)                               /mem - Wysyła losowego mema z Reddita'.format(message)                                                       
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
