from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Message

"""
    Класс фильтра для проверки типа чата.
    Позволяет фильтровать сообщения или callback-запросы по их типу чата
    (например, 'private', 'group', 'supergroup', 'channel').
"""


class TypeChat(BaseFilter):
    def __init__(self, chat_type: Union[str | list]):
        self.chat_type = chat_type

    async def __call__(self, message: CallbackQuery | Message) -> bool:
        if isinstance(message, CallbackQuery):
            return await self.check_type_chat(message.message)

        elif isinstance(message, Message):
            return await self.check_type_chat(message)

    async def check_type_chat(self, message: Message):
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        elif isinstance(self.chat_type, list):
            return message.chat.type in self.chat_type