import sqlite3
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

db = sqlite3.connect("bazaTim.db")
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INT,
    userName TEXT,
    result INT,
    variable INT
)""")

bot = Bot(token='')
dp = Dispatcher(bot, storage=MemoryStorage())
scheduler = AsyncIOScheduler()

groups = types.ReplyKeyboardMarkup(resize_keyboard=True)

group_one = types.KeyboardButton("Начать тест")
groups.add(group_one)

test_again_btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
test_again = types.KeyboardButton("Пройти тест еще раз")
test_again_btn.add(test_again)

games1_btn1 = types.KeyboardButton("Князь")
games1_btn2 = types.KeyboardButton("Граф")
games1_btn3 = types.KeyboardButton("Барон")
game1_btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
game1_btns.add(games1_btn1, games1_btn2, games1_btn3)

games2_btn1 = types.KeyboardButton("В Петербурге")
games2_btn2 = types.KeyboardButton("В Ясной Поляне")
games2_btn3 = types.KeyboardButton("В Богородицком уезде")
game2_btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
game2_btns.add(games2_btn1, games2_btn2, games2_btn3)

games3_btn1 = types.KeyboardButton("Война и мир")
games3_btn2 = types.KeyboardButton("Анна Каренина")
games3_btn3 = types.KeyboardButton("Воскресенье")
game3_btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
game3_btns.add(games3_btn1, games3_btn2, games3_btn3)

games4_btn1 = types.KeyboardButton("Война и мир")
games4_btn2 = types.KeyboardButton("Воскресенье")
games4_btn3 = types.KeyboardButton("Декабристы")
game4_btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
game4_btns.add(games4_btn1, games4_btn2, games4_btn3)

games5_btn1 = types.KeyboardButton("Роман")
games5_btn2 = types.KeyboardButton("Роман-эпопея")
games5_btn3 = types.KeyboardButton("Роман-воспитание")
game5_btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
game5_btns.add(games5_btn1, games5_btn2, games5_btn3)

games6_btn1 = types.KeyboardButton("Алексей Вронский")
games6_btn2 = types.KeyboardButton("Николай Лёвин")
games6_btn3 = types.KeyboardButton("Стив Облонский")
game6_btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
game6_btns.add(games6_btn1, games6_btn2, games6_btn3)

games7_btn1 = types.KeyboardButton("Война и мир")
games7_btn2 = types.KeyboardButton("Воскресенье")
games7_btn3 = types.KeyboardButton("Анна Каренина")
game7_btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
game7_btns.add(games7_btn1, games7_btn2, games7_btn3)

games8_btn1 = types.KeyboardButton("Война и мир")
games8_btn2 = types.KeyboardButton("Воскресенье")
games8_btn3 = types.KeyboardButton("Анна Каренина")
game8_btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
game8_btns.add(games8_btn1, games8_btn2, games8_btn3)

games9_btn1 = types.KeyboardButton("Посидел неделю в камере Бутырской тюрьмы")
games9_btn2 = types.KeyboardButton("Работал с письмами заключенных")
games9_btn3 = types.KeyboardButton("Прошел с отправленными в Сибирь заключенными пут от Бутырской тюрьмы до Николаевского вокзала")
game9_btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
game9_btns.add(games9_btn1, games9_btn2, games9_btn3)

games10_btn1 = types.KeyboardButton("Непротивление злу насилием")
games10_btn2 = types.KeyboardButton("Анархизм")
games10_btn3 = types.KeyboardButton("Приверженность")
game10_btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
game10_btns.add(games10_btn1, games10_btn2, games10_btn3)


class GetGroup(StatesGroup):
    game1 = State()
    game2 = State()
    game3 = State()
    game4 = State()
    game5 = State()
    game6 = State()
    game7 = State()
    game8 = State()
    game9 = State()
    game10 = State()


@dp.message_handler(Command('start'), state=None)
async def welcome(message):
    if message.from_user.id == message.chat.id:
        sql.execute(f"SELECT * FROM users WHERE user_id = {message.from_user.id}")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)",
                        (message.from_user.id, message.from_user.username, 0, 0))
            db.commit()
        await message.answer('Добро пожаловать в бот @Blessed_union и @BlackMercury111\nВы сможете познакомиться с историй Л.Н. Толстого, а также пройти тест, который покажет ваши знания. Каждый правильный ответ будет двигать ваш путь по карте. В самом конце находится приз. Удачи в прохождении!',
                             reply_markup=groups)


@dp.message_handler(content_types=['text'])
async def lalala(message):
    global PAY
    if message.text == 'Начать тест' or message.text == 'Пройти тест еще раз':
        await message.answer('Какой титул носил Лев Толстой?', reply_markup=game1_btns)
        await GetGroup.game1.set()


@dp.message_handler(state=GetGroup.game1)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy():
        if message.text.lower() == 'граф':
            if sql.execute(f'SELECT variable FROM users WHERE user_id = {message.chat.id}').fetchone()[0] == 0:
                last = sql.execute(f'SELECT result FROM users WHERE user_id = {message.chat.id}').fetchone()[0]
                sql.execute(f'UPDATE users SET result = {last + 1} WHERE user_id = "{message.from_user.id}"')
                db.commit()
            await state.finish()
            await message.answer("Так держать! Двигаемся дальше")
            await message.answer('Где родился Лев Толстой?', reply_markup=game2_btns)
            sql.execute(f'UPDATE users SET variable = 0 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await GetGroup.game2.set()
        else:
            sql.execute(f'UPDATE users SET variable = 1 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await message.answer("Ответ не совпал! Попробуй ещё")


@dp.message_handler(state=GetGroup.game2)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy():
        if message.text.lower() == 'в ясной поляне':
            if sql.execute(f'SELECT variable FROM users WHERE user_id = {message.chat.id}').fetchone()[0] == 0:
                last = sql.execute(f'SELECT result FROM users WHERE user_id = {message.chat.id}').fetchone()[0]
                sql.execute(f'UPDATE users SET result = {last + 1} WHERE user_id = "{message.from_user.id}"')
                db.commit()
            await state.finish()
            await message.answer("Так держать! Двигаемся дальше")
            await message.answer('Какой роман Льва Толстова способствовал его отлучению от церкви?', reply_markup=game3_btns)
            sql.execute(f'UPDATE users SET variable = 0 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await GetGroup.game3.set()
        else:
            sql.execute(f'UPDATE users SET variable = 1 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await message.answer("Ответ не совпал! Попробуй ещё")


@dp.message_handler(state=GetGroup.game3)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy():
        if message.text.lower() == 'воскресенье':
            if sql.execute(f'SELECT variable FROM users WHERE user_id = {message.chat.id}').fetchone()[0] == 0:
                last = sql.execute(f'SELECT result FROM users WHERE user_id = {message.chat.id}').fetchone()[0]
                sql.execute(f'UPDATE users SET result = {last + 1} WHERE user_id = "{message.from_user.id}"')
                db.commit()
            await state.finish()
            await message.answer("Так держать! Двигаемся дальше")
            await message.answer('Какой из романов Льва Толстого можно сравнить с эпической фреской?', reply_markup=game4_btns)
            sql.execute(f'UPDATE users SET variable = 0 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await GetGroup.game4.set()
        else:
            sql.execute(f'UPDATE users SET variable = 1 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await message.answer("Ответ не совпал! Попробуй ещё")


@dp.message_handler(state=GetGroup.game4)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy():
        if message.text.lower() == 'война и мир':
            if sql.execute(f'SELECT variable FROM users WHERE user_id = {message.chat.id}').fetchone()[0] == 0:
                last = sql.execute(f'SELECT result FROM users WHERE user_id = {message.chat.id}').fetchone()[0]
                sql.execute(f'UPDATE users SET result = {last + 1} WHERE user_id = "{message.from_user.id}"')
                db.commit()
            await state.finish()
            await message.answer("Так держать! Двигаемся дальше")
            await message.answer('Каково точное определение жанра «Войны и мира»?', reply_markup=game5_btns)
            sql.execute(f'UPDATE users SET variable = 0 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await GetGroup.game5.set()
        else:
            sql.execute(f'UPDATE users SET variable = 1 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await message.answer("Ответ не совпал! Попробуй ещё")


@dp.message_handler(state=GetGroup.game5)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy():
        if message.text.lower() == 'роман-эпопея':
            if sql.execute(f'SELECT variable FROM users WHERE user_id = {message.chat.id}').fetchone()[0] == 0:
                last = sql.execute(f'SELECT result FROM users WHERE user_id = {message.chat.id}').fetchone()[0]
                sql.execute(f'UPDATE users SET result = {last + 1} WHERE user_id = "{message.from_user.id}"')
                db.commit()
            await state.finish()
            await message.answer("Так держать! Двигаемся дальше")
            await message.answer('Какой из перонажей романа «Анна Каренина» представляет собой alter ego писателя?', reply_markup=game6_btns)
            sql.execute(f'UPDATE users SET variable = 0 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await GetGroup.game6.set()
        else:
            sql.execute(f'UPDATE users SET variable = 1 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await message.answer("Ответ не совпал! Попробуй ещё")


@dp.message_handler(state=GetGroup.game6)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy():
        if message.text.lower() == 'николай лёвин':
            if sql.execute(f'SELECT variable FROM users WHERE user_id = {message.chat.id}').fetchone()[0] == 0:
                last = sql.execute(f'SELECT result FROM users WHERE user_id = {message.chat.id}').fetchone()[0]
                sql.execute(f'UPDATE users SET result = {last + 1} WHERE user_id = "{message.from_user.id}"')
                db.commit()
            await state.finish()
            await message.answer("Так держать! Двигаемся дальше")
            await message.answer('Какой роман Лев Толстой называл «романом о современной жизни»?', reply_markup=game7_btns)
            sql.execute(f'UPDATE users SET variable = 0 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await GetGroup.game7.set()
        else:
            sql.execute(f'UPDATE users SET variable = 1 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await message.answer("Ответ не совпал! Попробуй ещё")


@dp.message_handler(state=GetGroup.game7)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy():
        if message.text.lower() == 'анна каренина':
            if sql.execute(f'SELECT variable FROM users WHERE user_id = {message.chat.id}').fetchone()[0] == 0:
                last = sql.execute(f'SELECT result FROM users WHERE user_id = {message.chat.id}').fetchone()[0]
                sql.execute(f'UPDATE users SET result = {last + 1} WHERE user_id = "{message.from_user.id}"')
                db.commit()
            await state.finish()
            await message.answer("Так держать! Двигаемся дальше")
            await message.answer('Какой роман Льва Толстого был переведен на все основные европейские языки практически сразу после публикации?', reply_markup=game8_btns)
            sql.execute(f'UPDATE users SET variable = 0 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await GetGroup.game8.set()
        else:
            sql.execute(f'UPDATE users SET variable = 1 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await message.answer("Ответ не совпал! Попробуй ещё")


@dp.message_handler(state=GetGroup.game8)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy():
        if message.text.lower() == 'воскресенье':
            if sql.execute(f'SELECT variable FROM users WHERE user_id = {message.chat.id}').fetchone()[0] == 0:
                last = sql.execute(f'SELECT result FROM users WHERE user_id = {message.chat.id}').fetchone()[0]
                sql.execute(f'UPDATE users SET result = {last + 1} WHERE user_id = "{message.from_user.id}"')
                db.commit()
            await state.finish()
            await message.answer("Так держать! Двигаемся дальше")
            await message.answer('Что сделал Толстой, чтобы добиться наибольшей реалистичности в описании быта заключенных?' , reply_markup=game9_btns)
            sql.execute(f'UPDATE users SET variable = 0 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await GetGroup.game9.set()
        else:
            sql.execute(f'UPDATE users SET variable = 1 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await message.answer("Ответ не совпал! Попробуй ещё")


@dp.message_handler(state=GetGroup.game9)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy():
        if message.text.lower() == 'прошел с отправленными в сибирь заключенными пут от бутырской тюрьмы до николаевского вокзала':
            if sql.execute(f'SELECT variable FROM users WHERE user_id = {message.chat.id}').fetchone()[0] == 0:
                last = sql.execute(f'SELECT result FROM users WHERE user_id = {message.chat.id}').fetchone()[0]
                sql.execute(f'UPDATE users SET result = {last + 1} WHERE user_id = "{message.from_user.id}"')
                db.commit()
            await state.finish()
            await message.answer("Так держать! Двигаемся дальше")
            await message.answer('Основной тезис толстовства - это ...?', reply_markup=game10_btns)
            sql.execute(f'UPDATE users SET variable = 0 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await GetGroup.game10.set()
        else:
            sql.execute(f'UPDATE users SET variable = 1 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await message.answer("Ответ не совпал! Попробуй ещё")


@dp.message_handler(state=GetGroup.game10)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy():
        if message.text.lower() == 'непротивление злу насилием':
            if sql.execute(f'SELECT variable FROM users WHERE user_id = {message.chat.id}').fetchone()[0] == 0:
                last = sql.execute(f'SELECT result FROM users WHERE user_id = {message.chat.id}').fetchone()[0]
                sql.execute(f'UPDATE users SET result = {last + 1} WHERE user_id = "{message.from_user.id}"')
                db.commit()
            await state.finish()
            sql.execute(f'UPDATE users SET variable = 0 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await state.finish()
            text = sql.execute(f'SELECT result FROM users WHERE user_id = {message.chat.id}').fetchone()[0]
            await message.answer(f'Твой резуальтат: {text} из 10')
            await message.answer('Поздравляем! Вы прошли тест ✌️\nСпасибо, что учитесь с нами.', reply_markup=test_again_btn)
            sql.execute(f'UPDATE users SET variable = 0 WHERE user_id = "{message.from_user.id}"')
            sql.execute(f'UPDATE users SET result = 0 WHERE user_id = "{message.from_user.id}"')
            db.commit()
        else:
            sql.execute(f'UPDATE users SET variable = 1 WHERE user_id = "{message.from_user.id}"')
            db.commit()
            await message.answer("Попробуй еще раз")


async def on_startup(_):
    print('Бот запущен')


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
