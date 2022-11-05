
# .------.------.------.------.------.------.------.------.------.------.
# |D.--. |4.--. |N.--. |1.--. |3.--. |L.--. |3.--. |K.--. |0.--. |0.--. |
# | :/\: | :/\: | :(): | :/\: | :(): | :/\: | :(): | :/\: | :/\: | :/\: |
# | (__) | :\/: | ()() | (__) | ()() | (__) | ()() | :\/: | :\/: | :\/: |
# | '--'D| '--'4| '--'N| '--'1| '--'3| '--'L| '--'3| '--'K| '--'0| '--'0|
# `------`------`------`------`------`------`------`------`------`------'
#
#                     Copyright 2022 t.me/D4n13l3k00
#           Licensed under the Creative Commons CC BY-NC-ND 4.0
#
#                    Full license text can be found at:
#       https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode
#
#                           Human-friendly one:
#            https://creativecommons.org/licenses/by-nc-nd/4.0

# meta developer: @evilginx


import random
import re

from .. import loader, utils


@loader.tds
class RouletteMod(loader.Module):
    strings = {"name": "GLUsers"}

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    @loader.owner
    async def glucmd(self, m):
        "<int> - максимальное количество участников"
        args = utils.get_args(m)
        reply = await m.get_reply_message()
        if reply:
          messages = m.client.iter_messages(
             self.chat_id, 
             offset_id = reply.id, 
             reverse=True, 
             limit = 400
          )
          async for msg in messages:
            print (msg)
        
        await m.edit(f"debug: <code>{args}</code>")
