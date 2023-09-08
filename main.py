from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove
import datetime
from initial import Token
from text import start_text, help_text, get_text, supoort_text, error_text
from keys import (
    person_keyboard,
    course_keyboard,
    valid_person,
    valid_course,
    bye_me_coffee,
)
from user_manegment import save_user_data, user_exists

# Initialize the bot and dispatcher
bot = Bot(Token)
dp = Dispatcher(bot)

async def send_document_to_user(message, person, tmp_course):
    try:
        wait_message = await message.reply(text="لطفا کمی صبر کنید", reply_markup=ReplyKeyboardRemove())
        file_path = f"jozve/{valid_person[person]}/{tmp_course}.pdf"
        with open(file_path, "rb") as file:
            await message.reply_document(document=file, caption=f"جزوه {tmp_course} توسط {person}", reply_markup=bye_me_coffee)
            await message.answer(text="شما میتوانید برای حمایت از کسی که جزوه را تهیه کرده است, قهوه بخرید D:", reply_markup=ReplyKeyboardRemove())
            await bot.delete_message(message.chat.id, wait_message.message_id)
    except:
        await message.answer(text="/support جزوه مورد نظر یافت نشد. با سازنده در ارتباط باشید", reply_markup=ReplyKeyboardRemove())

async def send_welcome_message(message):
    if not user_exists(message.from_user.id):
        save_user_data(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    await message.answer(text=start_text, reply_markup=ReplyKeyboardRemove())

async def send_help_message(message):
    await message.answer(text=help_text, reply_markup=ReplyKeyboardRemove())

async def send_get_message(message):
    await message.answer(text=get_text, reply_markup=course_keyboard)

async def send_support_message(message):
    await message.answer(text=supoort_text, reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await send_welcome_message(message)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await send_help_message(message)

@dp.message_handler(commands=['get'])
async def get_command(message: types.Message):
    await send_get_message(message)

@dp.message_handler(commands=['support'])
async def support_command(message: types.Message):
    await send_support_message(message)

@dp.message_handler(lambda message: message.text in valid_course)
async def course_handler(message: types.Message):
    global selection_course 
    global course_input
    selection_course = message.text
    course_input = True
    await message.answer(text="فرد مورد نظر خود را انتخاب کنید", reply_markup=person_keyboard)

@dp.message_handler(lambda message: message.text in valid_person.keys())
async def person_handler(message: types.Message):
    global course_input, selection_course 
    if course_input and message.text != "برکشت":
        tmp_course = selection_course
        course_input = False
        person = message.text
        await send_document_to_user(message, person, tmp_course)
    elif message.text == "برکشت":
        await message.answer(text="درس مورد نظر خود را انتخاب کنید", reply_markup=course_keyboard)
    else:
        await message.answer(text="ابتدا درس مورد نظر خود را انتخاب کنید", reply_markup=course_keyboard)

@dp.message_handler()
async def handle_other_messages(message: types.Message):
    await message.answer(text=error_text, reply_markup=ReplyKeyboardRemove())
async def start(_):
    print(datetime.datetime.now(), "Bot Started")
async def shutdown(_):
    print(datetime.datetime.now(), "Bot Stopped")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True ,on_startup=start , on_shutdown=shutdown )
