# Bu kod edalet_22 tərəfindən yazılıb
# Öz adına çıxaran peysərdi
# Bu yazıları silmədən işlədin

# t.me/RoBotlarimTg | YouTube: RoBotlarimTg |
# t.me/aykhan_s | t.me/edalet_22
# GitHub: EdaletRoBot

from telethon import events
import asyncio
import random
from telethon.tl.types import ChannelParticipantsBots
from telethon.tl.types import ChannelParticipantsAdmins
from os import remove
from telethon.tl.functions.users import GetFullUserRequest


edalet = TelegramClient('Qadir', API_ID, API_HASH).start(bot_token=bot_token)

#config
API_ID = 26712413
API_HASH = "3298034eb7cec614ef852fda02536153"
bot_token = "6060154700:AAFCIAPfWuxXvxuNAUW6FPpr7bEaH9SU7uY"


#Bu kodda olan • By @EdaletRoBot yazisini silen gelib mene Ata deyer
@edalet.on(events.NewMessage(pattern="^/banda ?(.*)"))
async def banda(event):
    if not event.is_group:
        return await event.reply("Bu əmr qruplar üçün etibarlıdır!")
    info = await event.client.get_entity(event.chat_id)
    title = info.title if info.title else "This chat"
    mentions = f'**{title}** qrupunda olan silinmiş hesaplar:\n'
    deleted = 0
    async for user in event.client.iter_participants(event.chat_id):
        if user.deleted:
            mentions += f"\nSilinmiş hesap `{user.id}`"
            deleted += 1
            await event.client.kick_participant(event.chat_id, user.id)
    mentions += f"\nSilinmiş hesaplar` = {deleted}`\n\n__• By @EdaletRoBot__"
    await event.reply(mentions)
    
    
    
print(">> Bot işləyir narahat olmayın. @nesirovqadirofficiall Məlumat almaq üçün <<")
edalet.run_until_disconnected()
