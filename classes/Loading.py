import importlib
import pathlib

from aiogram import Dispatcher, Bot

from classes import Module


class LoadingClasses:
    def __init__(self, folder: str):
        self.folder = folder
        self.list = list()
        self.current_directory = pathlib.Path(folder)
        self.ignor_file = list()

    def load_classes(self)-> None:
        for current_file in self.current_directory.glob('*.py'):
            self.ignor_file.append('__init__.py')
            if current_file.name not in self.ignor_file:
                file = current_file.name.replace('.py', '')
                module = importlib.import_module(f"{self.folder}.{file}")
                my_class = getattr(module, file)
                self.list.append(my_class)
        # Проверяем, можно ли выполнить сортировку
        can_sort = all(hasattr(cls, 'number_runtime') for cls in self.list)

        if can_sort:
            # Сортируем список по значению number_runtime
            self.list.sort(key=lambda x: x.number_runtime)


class LoadingModule(LoadingClasses):
    def __init__(self, folder: str = None):
        if not folder:
            folder = 'modules'
        super(LoadingModule, self).__init__(folder)

    def load_modules(self, bot: Bot, dp: Dispatcher) -> None:
        self.load_classes()

        for class_ in self.list:
            classes: Module = class_()
            classes.bot = bot
            classes.dp = dp
            classes.register_handlers()

            if 'router' in dir(classes):
                dp.include_router(classes.router)


class LoadingMiddlewares(LoadingClasses):
    def __init__(self, folder: str = None):
        if not folder:
            folder = 'middlewares'
        super(LoadingMiddlewares, self).__init__(folder)

    def load_middlewares(self, dp: Dispatcher) -> None:
        self.load_classes()
        for class_ in self.list:
            dp.update.outer_middleware(class_())
