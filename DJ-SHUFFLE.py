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
                sys.exit(0)

            li = u.readlines()

            u.close()
            htmlcode = str(li)

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
                await client.send_message(message.channel, 'ERROR```{fehler}```'.format(fehler=error))



    if message.content.startswith('&stop'):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except Exception as error:
            await client.send_message(message.channel, 'ERROR ```{fehler}```'.format(fehler=error))

    if message.content.startswith('&quit'):
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
            channel = message.author.voice.voice_channel
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
        userch = message.author.voice.voice_channel
        await client.send_message(message.channel, 'Test wird gestartet')
        botch = message.author.voice.voice_channel
        if userch == botch:
            await client.send_message(message.channel, 'Wir sind im gleichen channel')
        if userch != botch:
            await client.send_message(message.channel, 'Wir sind nicht im gleichen channel')


client.run('MzkwODg5MjcyMjk2ODY1Nzky.DRQsYg.9562Os10ub4DrWeQu0TjGmm2dqI')