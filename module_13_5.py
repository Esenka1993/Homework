from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button_count = KeyboardButton(text='Рассчитать')
    button_info = KeyboardButton(text='Информация')
    kb.add(button_count, button_info)
    await message.answer('Привет, я - бот, помогающий твоему здоровью!', reply_markup=kb)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(state=None, text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    w = float(data['weight'])
    g = float(data['growth'])
    a = int(data['age'])
    calories = (10 * w) + (6.25 * g) - (5 * a) + 5
    await message.answer(f"Норма калорий для Вас равна {calories}")
    await state.finish()


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
