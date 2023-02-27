import random
from pyrogram import Client, filters, enums
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
    "I'm not lazy, I'm on energy saving mode.....!!!",
    " Hey there Whatsapp is using me.",
    "Girls use photoshop to look beautiful.. Boys use photoshop to show their creativity.....",
    "செல்போனும் ஊறுகாய் போல் தொடாமல் பலரும் சாபிடுவதில்லை",
    "Dear Lord, there is a bug in your software... it's called Monday, please fix itളും.",
    "அன்பே உன் கையை பிடித்து நகை கடை வரை செல்ல ஆசை.....",
    "Save water - Drink beer!🍾",
    "ரன்னிங் ரேஸ்ல கால் எவ்வளவு வேகமா ஓடினாலும் பரிசு கைக்குத்தான் கிடைக்கும்....thats life",
    "Decided to burn lots of calories today so I set a fat kid on fire.",
    "I wake up when I cant hold my pee in any longer.",
    "C.L.A.S.S - Come late and start sleeping :)",
    "Relationship Status: Looking for a FREE WiFi connection.",
    "My father always told me, find a job you love and you'll never have to work a day in your life.",
    "Life is too short smile while you still have teeth...",
    "My study period = 15 minutes. My break time = 3 hours.",
    "I'm jealous of my parents... I'll never have a kid as cool as theirs!",
    "You can never buy Love... But still you have to pay for it...",
    "Don't kiss behind the garden, Love is blind but the neighbors are not.",
    "Sorry about those texts I sent you last night, my phone was drunk.",
    "This is the beginning of the sentence you just finished reading.",
    "Good Morning, let the stress begin...",
    "Eat - Sleep - Regret - Repeat.",
    "Move on...",
    "Dream as if you’ll live forever... Live as if tomorrow is last one.",
    "Always remember you are UNIQUE - Just like everybody else.",
    "The only difference between a good day and a bad day is your attitude.",
    "Life is too short. Don't waste it removing pen drive safely.",
    "Waiting for Wi-Fi Network...",
    "Sleep till you’re hungry... Eat till you’re sleepy.",
    "One day, I’m gonna make the onions cry.",
)


@Client.on_message(
    filters.command("runs", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
