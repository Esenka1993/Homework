from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = '7405481807:AAGuWdeXHTjHe7Q581rYmdzwPCzLRkuBJZ8'
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

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    ik = InlineKeyboardMarkup(resize_keyboard=True)
    ik_button_count = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
    ik_button_formulas = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
    ik.add(ik_button_count, ik_button_formulas)
    await message.answer('Выберите опцию', reply_markup=ik)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('(10 * вес) + (6.25 * рост) - (5 * возраст) + 5')


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
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


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение')

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)