import discord
import os
import smtplib, ssl

client = discord.Client()

token = '' #Discord Bot token


#Email server login info
ip = ''
port = 587  
email = ''
password = ''
context = ssl._create_unverified_context()
sendto = '' #Address you would like to send messages to




@client.event
async def on_message(message):
    if message.author == client.user:
            return
    print(str(message.content))
    msg = ("""From: ME
Subject:Discord Msg

"""+str(message.author)+":  "+str(message.content))

    
    with smtplib.SMTP(ip, port) as server:
        print("Sendmessage started")
        server.starttls(context=context)
        server.login(email, password, initial_response_ok=True)
        print("login success")
        server.sendmail(email, sendto, msg)
        print("Sent")



client.run(token)
