from aiogram import Router, Bot, Dispatcher
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

class Module:
    number_runtime = 0
    bot: Bot
    dp: Dispatcher

    def __init__(self):
        self.router = Router()

    async def del_or_edit_message(self, message: Message, state: FSMContext):
        state_data = await state.get_data()
        message_id = state_data.get('message_id')
        if message_id:
            try:
                is_del = await message.chat.delete_message(message_id=message_id)
            except TelegramBadRequest:
                is_del = False

            try:
                if not is_del:
                    await self.bot.edit_message_reply_markup(
                        message_id=message_id,
                        chat_id=message.chat.id,
                        reply_markup=None
                    )
            except TelegramBadRequest:
                pass

    def register_handlers(self):
        pass
