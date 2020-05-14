import discord
from datetime import *
import psycopg2
import random

conn = psycopg2.connect("dbname=mydb user=postgres password=pass") # to samo hasło które wybieraliśmy przy instalacji
cur = conn.cursor()

def initDB():
    cur.execute("CREATE TABLE notatki ( id SERIAL PRIMARY KEY, content text);")
    conn.commit()
# initDB()

def saveToDb(text):
    cur.execute('INSERT INTO notatki (content) VALUES (%s);', [text])
    conn.commit()

def readAll():
    pass

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author == client.user:
            return
        if message.content.startswith('save '):
            saveToDb(message.content)
            await message.channel.send('zapisano')
        if message.content.startswith('remind me what have i said'):
            await message.channel.send(readAll())
               


client = MyClient()

# zmienić ../bot-token na ./bot-token jeżeli plik jest obok skryptu
with open('../bot-token', 'r') as tokenfile:
    token = tokenfile.read(70)
    client.run(token)

print("ojej")