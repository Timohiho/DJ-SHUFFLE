import discord
import sys
import urllib.request

client = discord.Client()

player = {}

loop = 1

translation_table = {
    " ": "+",
}

@client.event
async def on_ready():
    print('==========')
    print(client.user.name + '#' + client.user.discriminator)
    print(client.user.id)
    print('https://discordapp.com/oauth2/authorize?client_id=390889272296865792&permissions=36768768&scope=bot')
    print('==========')

@client.event #musik
async def on_message(message):
    if message.content.startswith('&play '):
        song = message.content[6:]

        if song.startswith('https://www.youtube.com/watch?v='):
            link = song
            try:
                channel = message.author.voice.voice_channel
                voice = await client.join_voice_channel(channel)
                player = await voice.create_ytdl_player(link)
                player.start()
                print(message.content)
            except Exception as error:
                await client.send_message(message.channel, ' ```ERROR{fehler}```'.format(fehler=error))

        else:
            song = message.content[6:]
            titel = song
            name = titel.translate(str.maketrans(translation_table))
            try:
                u = urllib.request.urlopen("https://www.youtube.com/results?q=" + name)
            except:
                print('Fehler')
                sys.exit(0) # schliessen der funktion

            li = u.readlines() # Kopieren des Html code in li

            u.close() # Html code schliessen
            htmlcode = str(li) # Html code als string in die variable htmlcode

            str1 = str(li); # Html code als string in die variable str1
            str2 = "/watch?v="; # /watch?v= in variable str2

            startsongid = htmlcode[str1.find(str2):] # beginn der variable str2 in htmlcode finden und bis an diese position kürzen und diese in die variable startsingid kopieren
            videoid = startsongid[:20] # ende der variable startsongid definieren und diese in die variable videoid kopieren
            songlink = videoid.translate(str.maketrans(translation_table))

            print(songlink)
            youtubesong = 'https://www.youtube.com' + songlink # Vervollständigen der video url

            userch = message.author.voice.voice_channel # herausfinden in welchem voice channel der absender ist
            botch = message.author.voice.voice_channel # herausfinden in welchem voice channel der bot ist
            if userch == botch:
                try:
                    voice_client = client.voice_client_in(message.server)
                    await voice_client.disconnect()
                except Exception as error:
                    print(error)

            try:
                channel = message.author.voice.voice_channel # herausfinden in welchem voice channel der absender ist
                voice = await client.join_voice_channel(channel)
                player = await voice.create_ytdl_player(youtubesong)
                player.start()
                print(message.content)
            except Exception as error:
                await client.send_message(message.channel, 'ERROR```{fehler}```'.format(fehler=error))



    if message.content.startswith('&stop'): # Wiedergabe stopen
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect() # Voice channel verlassen
            channel = message.author.voice.voice_channel # herausfinden in welchem voice channel der absender ist
            await client.join_voice_channel(channel) # voice channel beitreten
        except Exception as error:
            await client.send_message(message.channel, 'ERROR ```{fehler}```'.format(fehler=error)) # Fehler ausgabe

    if message.content.startswith('&quit'): # voice_channel verlassen
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except Exception as error:
            await client.send_message(message.channel, 'ERROR ```{fehler}```'.format(fehler=error))

    if message.content.startswith('&join'):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except Exception as error:
            print(error)
        try:
            channel = message.author.voice.voice_channel # herausfinden in welchem voice channel der absender ist
            await client.join_voice_channel(channel)
        except Exception as error:
            await client.send_message(message.channel, 'ERROR ```{fehler}```'.format(fehler=error))

    if message.content.startswith('&commands'):
        music_help = '&play [Song]'
        quit_help = '&quit'
        join_help = '&join'
        stop_help = '&stop'
        await client.send_message(message.channel, '``{music_help}`` play music'.format(music_help=music_help))
        await client.send_message(message.channel, '``{quit_help}`` disconnect'.format(quit_help=quit_help))
        await client.send_message(message.channel, '``{join_help}`` connect'.format(join_help=join_help))
        await client.send_message(message.channel, '``{stop_help}`` stop music'.format(stop_help=stop_help))

    if message.content.startswith('&test'):
        userch = message.author.voice.voice_channel # herausfinden in welchem voice channel der absender ist
        await client.send_message(message.channel, 'Test started') # ausgabe Test started
        botch = message.author.voice.voice_channel # herausfinden in welchem voice channel der bot ist
        if userch == botch: # ist channel absender gleich channel bot
            await client.send_message(message.channel, 'Wir sind im gleichen channel') # ausgabe wir sind im gleichen channel
        if userch != botch: # ist channel absender nichtgleich channel bot
            await client.send_message(message.channel, 'Wir sind nicht im gleichen channel') # ausgabe wir sind nicht im gleichen channel

client.run('MzkwODg5MjcyMjk2ODY1Nzky.DRQsYg.9562Os10ub4DrWeQu0TjGmm2dqI')
