from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery

"""
    Класс фильтра для проверки данных callback-запроса.
    Фильтр позволяет сравнивать данные запроса с заданной строкой 
    или списком строк, чтобы определить, соответствует ли запрос условиям.
"""


class CallbackQueryData(BaseFilter):
    def __init__(self, callbacks: Union[str | list]):
        self.callbacks = callbacks

    async def __call__(self, call: CallbackQuery) -> bool:
        # Если ожидаемое значение — строка, проверяем точное совпадение с данными запроса
        if isinstance(self.callbacks, str):
            return call.data == self.callbacks

        # Если ожидаемое значение — список строк, проверяем наличие данных запроса в списке
        elif isinstance(self.callbacks, list):
            return call.data in self.callbacks

        # Если данные не соответствуют ни одному из условий, возвращаем False
        return False
