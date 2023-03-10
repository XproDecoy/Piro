import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://api.sumanjay.cf/covid/?country="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("π²π»πΎππ΄", callback_data='close_data')]])

@Client.on_message(filters.command("covid"))
async def reply_info(client, message):
    query = message.text.split(None, 1)[1]
    await message.reply_photo(
        photo="https://telegra.ph/file/5c7f6ec6a2727708a74f6.jpg",
        caption=covid_info(query),
        quote=True
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**π²πΎππΈπ³ π·πΏ πΈπ½π΅πΎππΌπ°ππΈπΎπ½**--
αβΊ Country : `{country}`
αβΊ Actived : `{active}`
αβΊ Confirmed : `{confirmed}`
αβΊ Deaths : `{deaths}`
αβΊ ID : `{info_id}`
αβΊ Last Update : `{last_update}`
αβΊ Latitude : `{latitude}`
αβΊ Longitude : `{longitude}`
αβΊ Recovered : `{recovered}`"""
        return covid_info
    except Exception as error:
        return error
