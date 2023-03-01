import discord
from discord.ext import commands

app = commands.Bot(command_prefix='!')

@app.command(
    name='dial',
    description='This is command to start making calls',
    guild_only=True,
)
async def call(ctx, cell_phone: str, otp_digits: str, client_name: str, company_name: str):
    await ctx.send('Calling Initiated!')
    open('Details/Digits.txt', 'w').write(f'{otp_digits}')
    open('Details/Client_Name.txt', 'w').write(f'{client_name}')
    open('Details/Company Name.txt', 'w').write(f'{company_name}')
    call = client.calls.create(
        url=f'{ngrok}/voice',
        to=f'{cell_phone}',
        from_=f'{your_twilio_phone_number}'
    )
    sid = call.sid
    print(sid)
    a = 0
    b = 0
    c = 0
    d = 0
    while True:
        if client.calls(sid).fetch().status == 'queued':
            if not a >= 1:
                embed = discord.Embed(title='', description='Call Is Placed', color=discord.Colour.green())
                await ctx.channel.send(embed=embed)
                a = a + 1
        elif client.calls(sid).fetch().status == 'ringing':
            if not b >= 1:
                embed = discord.Embed(title='', description='Cell Phone Is Ringing', color=discord.Colour.green())
                await ctx.channel.send(embed=embed)
                b = b + 1
        elif client.calls(sid).fetch().status == 'in-progress':
            if not c >= 1:
                embed = discord.Embed(title='', description='Call In Progress',
                                      color=discord.Colour.green())
                await ctx.channel.send(embed=embed)
                c = c + 1
        elif client.calls(sid).fetch().status == 'completed':
            embed = discord.Embed(title='', description='Call Succefully Completed', color=discord.Colour.green())
            await ctx.channel.send(embed=embed)
            break
        elif client.calls(sid).fetch().status == 'failed':
            embed = discord.Embed(title='', description='Call Failed',
                                  color=discord.Colour.red())
            await ctx.channel.send(embed=embed)
            break
        elif client.calls(sid).fetch().status == 'no-answer':
            embed = discord.Embed(title='', description='Call Was Not Answered',
                                  color=discord.Colour.red())
            await ctx.channel.send(embed=embed)
            break
        elif client.calls(sid).fetch().status == 'canceled':
            embed = discord.Embed(title='
