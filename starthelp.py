# Bu repo edalet_22 tərəfindən yazılıb
# Öz adına çıxaran peysərdi
# Bu yazıları silmədən işlədin

# t.me/RoBotlarimTg | YouTube: RoBotlarimTg |
# t.me/aykhan_s |  t.me/edalet_22
# GitHub: EdaletRoBot


from telethon import events
from telethon import TelegramClient
from telethon import Button
#config
API_ID = 
API_HASH = "          "
bot_token = "6060154700:AAFCIAPfWuxXvxuNAUW6FPpr7bEaH9SU7uY"


edalet = TelegramClient('Qadir', API_ID, API_HASH).start(bot_token=bot_token)




@edalet.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in edalet.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"Salam, Mən @nesirovqadirofficiall terefinde Yazılmışam.Əmrlər düməsinə klik edərək əmrləri öyrənə bilərsiniz", buttons=(
        [Button.inline("📖 Əmrlər", data="help")],
        [Button.url("📣 Kanal", url="https://t.me/biolande")],
        [Button.url("👥 Qrup", url="https://t.me/imperatorofficiall"),
        Button.url("👤 Sahib", url="https://t.me/nesirovqadirofficiall")],
    ), 
    link_preview=False)


  if event.is_group:
    return await edalet.send_message(event.chat_id, f"Məni qrupunuza aldığınız üçün təşşəkür edirəm",)


@edalet.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in edalet.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"Salam, Mən @nesirovqadorofficiall terefinde Yazılmışam.Əmrlər düməsinə klik edərək əmrləri öyrənə bilərsiniz", buttons=(
        [Button.inline("📖 Əmrlər", data="help")],
        [Button.url("📣 Kanal", url="https://t.me/biolande")],
        [Button.url("👥 Qrup", url="https://t.me/imperatorofficiall"),
        Button.url("👤 Sahib", url="https://t.me/nesirovqadirofficiall")],
    ), 
    link_preview=False)

#edalet_22 terefinden yazilib bu sozleri silmeden istiafde edin
@edalet.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):	
    await event.edit(f"**  [Bot adı](http://t.me/Salamlamabot)-un Kömək '📖 Əmrlər' Bunlardır.⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**➪", buttons=(
	             [Button.url('Qrup💬', 'https://t.me/imperatorofficiall'),
                      Button.url('Sahib 👨‍💻', 'https://t.me/edalet_22')],
	             [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)


print(">> Bot işləyir narahat olmayın. @nesirovqadirofficiall Məlumat almaq üçün <<")
edalet.run_until_disconnected()
