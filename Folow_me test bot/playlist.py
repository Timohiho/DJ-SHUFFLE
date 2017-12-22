import discord # Importiert Discord
import sys # Importiert sys
import urllib.request # Importiert urllib.request


client = discord.Client() # Definiert den Client

player = {} # Plaver

translation_table = {
    " ": "+",
} # Ersetzten durch

@client.event #zeigt die daten des Bots
async def on_ready():
    print('==========')
		print(client.user.name + '#' + client.user.discriminator) # Bot name und
    print(client.user.id) # Bot ID
    print('https://discordapp.com/oauth2/authorize?client_id=387166472004173826&permissions=36768768&scope=bot') # Einladungslink
    print('==========')

@client.event #musik
async def on_message(message):

    if message.content.startswith('çtest'):
        userch = message.author.voice.voice_channel
        await client.send_message(message.channel, 'Video mit dem Namen ' + 'song' + ' wird gesucht.')
        botch = message.author.voice.voice_channel
        if userch == botch:
            await client.send_message(message.channel, 'Wir sind im gleichen channel')
        if userch != botch:
            await client.send_message(message.channel, 'Wir sind nicht im gleichen channel')

    if message.content.startswith('çplay '):
        song = message.content[6:] # Aus der Nachricht den titel extrahieren

        if song.startswith('https://www.youtube.com/watch?v='):
            link = song
            try:
                channel = message.author.voice.voice_channel
                voice = await client.join_voice_channel(channel)
                player = await voice.create_ytdl_player(link)
                player.start()
                print(message.content)
            except Exception as error:
                await client.send_message(message.channel, ' ```{fehler}```'.format(fehler=error))

        else:
            song = message.content[6:]
            titel = song
            name = titel.translate(str.maketrans(translation_table)) # Leerzeichen aus der suche entfernen
            try:
                u = urllib.request.urlopen("https://www.youtube.com/results?q=" + name) # Beginn der URL anfrage
            except:
                print('Fehler')
                sys.exit(0)

            li = u.readlines() # lesen des HTML code

            u.close() # Schliessen der URL anfrage
            htmlcode = str(li) # HTML code als string in die variable htmlcode kopieren

            str1 = str(li);
            str2 = "/watch?v=";

            startsongid = htmlcode[str1.find(str2):]
            videoid = startsongid[:20]
            songlink = videoid.translate(str.maketrans(translation_table))

            print(songlink)
            youtubesong = 'https://www.youtube.com' + songlink

            userch = message.author.voice.voice_channel
            botch = message.author.voice.voice_channel
            if userch == botch:
                try:
                    voice_client = client.voice_client_in(message.server)
                    await voice_client.disconnect()
                except Exception as error:
                    print(error)

            try:
                channel = message.author.voice.voice_channel
                voice = await client.join_voice_channel(channel)
                player = await voice.create_ytdl_player(youtubesong)
                player.start()
                print(message.content)
            except Exception as error:
                await client.send_message(message.channel, 'Es gab folgenden Fehler ```{fehler}```'.format(fehler=error))

    if message.content.startswith('çstop'):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except Exception as error:
            await client.send_message(message.channel, 'Es gab folgenden Fehler ```{fehler}```'.format(fehler=error))

    if message.content.startswith('çquit'): # voice_channel verlassen
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except Exception as error:
            await client.send_message(message.channel, 'Es gab folgenden Fehler ```{fehler}```'.format(fehler=error))

    if message.content.startswith('çjoin'): # voice_channel beitreten
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except Exception as error:
            await client.send_message(message.channel, 'Es gab folgenden Fehler ```{fehler}```'.format(fehler=error))

    if message.content.startswith('çcommands'):
        music_help = 'çplay [Song]'
        quit_help = 'çquit'
        join_help = 'çjoin'
        stop_help = 'çstop'
        await client.send_message(message.channel, '``{music_help}`` um musik zu hören'.format(music_help=music_help))
        await client.send_message(message.channel, '``{quit_help}`` trennt den bot vom Kanal'.format(quit_help=quit_help))
        await client.send_message(message.channel, '``{join_help}`` verbinden den bot mit dem kanal mit dem auch sie verbunden sind'.format(join_help=join_help))
        await client.send_message(message.channel, '``{stop_help}`` stopt die aktuelle wiedergabe'.format(stop_help=stop_help))


client.run('Mzg3OTA2MzIwODUxOTI3MDQw.DQlR6w.hVcJXvdQpWRATwSUPYzZuZ2otOg')
