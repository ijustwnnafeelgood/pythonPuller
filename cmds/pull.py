import discord
from discord.ext import commands
import os
import requests
from yt_dlp import YoutubeDL
import pathlib

base_dir = pathlib.Path(__file__).parent.parent

cover = "$undefined"

def checkInput(type, input):
    if type == "c":
        if not input:
            return "$undefined"
        else:
            return "s3://soundcloud-images/artworks-"+input+"-original.jpg"
    elif type == "t" or type == "w":
        if not input:
            raise Exception("Please Insert Input")


cookies = {
    'ja': '0',
    'sc_anonymous_id': '642479-752861-748105-571831',
    'ajs_anonymous_id': '%224231a560-73d1-4898-a4de-960756641670%22',
    'ajs_user_id': '%22soundcloud%3Ausers%3A1296732396%22',
    'oauth_token': '2-295236-1296732396-SjObwqZLU8qCw',
    'ajs_user_id': '%22soundcloud%3Ausers%3A1296732396%22',
    'ajs_anonymous_id': '%224231a560-73d1-4898-a4de-960756641670%22',
    'cookie_consent': '1',
    'connect_session': '1',
    'soundcloud_session_hint': '1',
    'datadome': 'bnc21I18SD81BvAEwh1yO6ADDT6N_oCU4zJOksxSTR120pGlkr6yx43FysyL_rMbdqIJ8FmSd7TwamNleP8fVBwZjI1kFMD6WQCjAnPf4jCdpwTZsvX3ncpAfI64dExH',
    'sc_session': '{%22id%22:%22B7827346-98CA-4F39-93CC-8D10C9830211%22%2C%22lastBecameInactive%22:%222024-04-14T20:14:31.149Z%22}',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Apr+14+2024+15%3A14%3A33+GMT-0500+(Central+Daylight+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d7466323-8f2c-4bda-9348-e3ba6bb81ee0&interactionCount=0&landingPath=https%3A%2F%2Fsoundcloud.com%2Fn%2Fupload&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1%2CC0005%3A1%2CC0007%3A1',
}

headers = {
    'accept': 'text/x-component',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'text/plain;charset=UTF-8',
    # 'cookie': 'ja=0; sc_anonymous_id=642479-752861-748105-571831; ajs_anonymous_id=%224231a560-73d1-4898-a4de-960756641670%22; ajs_user_id=%22soundcloud%3Ausers%3A1296732396%22; oauth_token=2-295236-1296732396-SjObwqZLU8qCw; ajs_user_id=%22soundcloud%3Ausers%3A1296732396%22; ajs_anonymous_id=%224231a560-73d1-4898-a4de-960756641670%22; cookie_consent=1; connect_session=1; soundcloud_session_hint=1; datadome=bnc21I18SD81BvAEwh1yO6ADDT6N_oCU4zJOksxSTR120pGlkr6yx43FysyL_rMbdqIJ8FmSd7TwamNleP8fVBwZjI1kFMD6WQCjAnPf4jCdpwTZsvX3ncpAfI64dExH; sc_session={%22id%22:%22B7827346-98CA-4F39-93CC-8D10C9830211%22%2C%22lastBecameInactive%22:%222024-04-14T20:14:31.149Z%22}; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Apr+14+2024+15%3A14%3A33+GMT-0500+(Central+Daylight+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d7466323-8f2c-4bda-9348-e3ba6bb81ee0&interactionCount=0&landingPath=https%3A%2F%2Fsoundcloud.com%2Fn%2Fupload&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1%2CC0005%3A1%2CC0007%3A1',
    'dnt': '1',
    'next-action': '612294c6684e08b0c4f5d1d8acc2fbd1e5e0fd8d',
    'next-router-state-tree': '%5B%22%22%2C%7B%22upload%22%3A%5B%22children%22%2C%7B%22children%22%3A%5B%22upload%22%2C%7B%22children%22%3A%5B%22review%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%5D%7D%5D%7D%5D%7D%5D%2C%22children%22%3A%5B%22%5B...catchAll%5D%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
    'next-url': '/children/upload/review',
    'origin': 'https://soundcloud.com',
    'referer': 'https://soundcloud.com/n/upload/review',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
getHeaders = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'OAuth 2-295236-1296732396-SjObwqZLU8qCw',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://soundcloud.com',
    'Referer': 'https://soundcloud.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
params = {
    'representation': 'owner',
    'client_id': 'X9BszUCk7gBtVEK0XKnrPr4MOk3eSRQY',
    'app_version': '1712837702',
    'app_locale': 'en',
}

def get_link(trackId):
    response = requests.get(f'https://api-v2.soundcloud.com/tracks/soundcloud:tracks:{trackId}', params=params, headers=getHeaders)
    if response.ok:
        resp = response.text
        resp = resp.split('"permalink_url":"')[1]
        resp = resp.split('","playback_count')[0]
        return resp
    else:
        return response

def download_track(url):
    ydl = YoutubeDL({'writeinfojson': False,
                'writethumbnail': True,
                'allowed_extractors': ['soundcloud.*', 'generic'],
                'paths': {'home': "./files"},
                'outtmpl': '%(id)s.%(ext)s'})
    with ydl:
        result = ydl.extract_info(
            url,
            download=True
        )
    return result

def main(title, waveform, cover):
    checkInput("t", title); checkInput("w", waveform); cover = checkInput("c",cover)
    if not os.path.isdir("./files"):
        os.makedirs("./files")
    data = '[{"uid":"{waveform}","trackInput":{"title":"{title}","permalink":"","genre":"","description":"","originalFilename":"incel squad.mp3","commentable":false,"revealComments":false,"downloadable":true,"revealStats":false,"sharing":"private","tagList":[],"s3ArtworkUrl":"{cover}"}}]'.replace("{waveform}",waveform).replace("{title}", title).replace("{cover}", cover)
    response = requests.post('https://soundcloud.com/n/upload/review', cookies=cookies, headers=headers, data=data)
    if response.ok:
        resp = response.text
        resp = resp.split('soundcloud:tracks:')[1]
        resp = resp.split('","permalinkUrl":"')[0]
        privLink = get_link(resp)
        try:
            getFile = download_track(privLink)
            covername = base_dir / "files" / f"{getFile["id"]}.jpg"
            songname = base_dir / "files" / f"{getFile["id"]}.{getFile["audio_ext"]}"
        except:
            covername = base_dir / "files" / "files/unableToDownload.txt"
            songname = base_dir / "files" / "files/unableToDownload.txt"
        


        toReturn = {
            "privateLink": privLink,
            "songFile": songname,
            "coverFile": covername
        }
        print(privLink)
        return toReturn
    else:
        response = {
            "errorCode": response,
            "privateLink": "",
        }
        return response


@commands.hybrid_command(name="pull",description="pull deleted soundcloud tracks")
async def pull(ctx, title, waveform, cover):
    await ctx.defer()
    response = main(title,waveform,cover)
    if response["privateLink"] != "":
        await ctx.send(f"{response["privateLink"]}")
    else:
        await ctx.send(f"failed with: {response["errorCode"]}", ephemeral=True)

async def setup(bot):
    bot.add_command(pull)