from filldata import data



main_text = """import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN_API
from menu import base_model


bot = Bot(TOKEN_API)
dp = Dispatcher()

async def main():

    dp.include_routers(base_model.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())"""

config_text = f"""TOKEN_API = {data["API_KEY"]}"""

initial_text = 'from . import states'

state_text = """from aiogram.fsm.state import StatesGroup, State


class BasicState(StatesGroup):
    Mystate = State()"""

base_model_text = """from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import CommandStart
from menu.mainkb import new_kb


router = Router()

# /start Command handler
@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Hi user!')"""

main_kb_text = """from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def new_kb(): 
    
    builder = ReplyKeyboardBuilder(resize_keyboard=True)
    btn1 = KeyboardButton('Hello!')
    builder.add(btn1)
    
    return builder.as_markup()"""

license_text = f"""MIT License

Copyright (c) 2024 {data['author_license']}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

readme_text = """# Name of Your Project

Short description or video ->>> link

## Description

Your main description

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/yourprojectname.git
    cd yourprojectname
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Replace `<YOUR_API_KEY>` in `config.py` with your API.

4. Run the bot:

    ```bash
    python main.py
    ```

## Ideas to update

Your future ideas.

## License

This project is licensed under the MIT License. See the LICENSE file for details."""