from aiogram.types import ReplyKeyboardMarkup , InlineKeyboardButton , InlineKeyboardMarkup

person_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
valid_person = {"آیدا احمدزاده":"aida_ahmadzadeh" ,
                 "حنانه یحیایی":"hanane_yahyai",
                "جزوات ترم پیش":"last_semester",
                "برکشت":"back"}
for person_name in valid_person.keys() :person_keyboard.insert(person_name)


course_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
valid_course = ["احتمال" ,
                "مباني جبر" ,
                "مباني آناليز عددي"  ,
                "مباني نظريه محاسبه" ,
                "مباني منطق ونظريه مجموعه ها" ]
for course in valid_course :course_keyboard.insert(course)

bye_me_coffee = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text="برای من قهوه بخر",
                          url="https://coffeebede.com/amirel1te")
)
