# Bu repo edalet_22 tərəfindən yazılıb
# Öz adına çıxaran peysərdi
# Bu yazıları silmədən işlədin

# t.me/RoBotlarimTg | YouTube: RoBotlarimTg | t.me/EdaletSup
# t.me/aykhan_s | t.me/edalet_22
# GitHub: EdaletRoBot



from telethon import TelegramClient
from telethon import events


# Config məlumatları
API_ID = *******
API_HASH = "**********************************"
bot_token = "**********************************"

# Telegram Client (Telethon)
edalet = TelegramClient('Qadir', API_ID, API_HASH).start(bot_token=bot_token)


#@edalet_22 terefindən @RoBotlarimTg üçün yazilib silmədən istifadə edin
@edalet.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(random.choice(userjoin))


@edalet.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply("Əla Birdə gəlmə")

userjoin = (

    "Xoş gəldin mesajı 1",
    "Xoş gəldin mesajı 2",
    "Xoş gəldin mesajı 3",
    "Xoş gəldin mesajı 4",
    "Xoş gəldin mesajı 5",
    "",
)


print(">> Bot işləyir narahat olmayın. @nesirovqadirofficiall Məlumat almaq üçün <<")
edalet.run_until_disconnected()
