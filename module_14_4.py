from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import initiate_db, get_all_products
initiate_db()

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_count = KeyboardButton(text='Рассчитать')
button_info = KeyboardButton(text='Информация')
button_buy = KeyboardButton(text='Купить')
kb.add(button_count, button_info, button_buy)
ik = InlineKeyboardMarkup(resize_keyboard=True)
ik_button_count = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
ik_button_formulas = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
ik.add(ik_button_count, ik_button_formulas)
ik2 = InlineKeyboardMarkup()
ik_button_pr1 = InlineKeyboardButton(text='Product1', callback_data="product_buying")
ik_button_pr2 = InlineKeyboardButton(text='Product2', callback_data="product_buying")
ik_button_pr3 = InlineKeyboardButton(text='Product3', callback_data="product_buying")
ik_button_pr4 = InlineKeyboardButton(text='Product4', callback_data="product_buying")
ik2.add(ik_button_pr1, ik_button_pr2, ik_button_pr3, ik_button_pr4)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет, я - бот, помогающий твоему здоровью!', reply_markup=kb)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    for name in products:
        title, description, price = name[0], name[1], name[2]
        await message.answer(f'Название: {title} | Описание: {description} | Цена: {price}')
        with open(f'{name[0]}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=ik2)



@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=ik)



@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('(10 * вес) + (6.25 * рост) - (5 * возраст) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await call.answer()
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
