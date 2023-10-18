import aiogram
import asyncio,aiosqlite
from aiogram import Bot, Dispatcher, executor, types
from config import *
from buttons import *
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

########## States - start  ##########
class rate(StatesGroup):
    name = State()
    number = State()
    text = State()
    type = State()

########## States - END ##########


bot=Bot(token=token,parse_mode=types.ParseMode.HTML,disable_web_page_preview=True)
dp = Dispatcher(bot,storage=MemoryStorage())



########## - HANDLERS of state ##########
@dp.message_handler(content_types=['text'], state = rate.name)
async def get_channel_id(message,state: FSMContext):
    
    if message.text == 'Отмена ❌':
        await bot.send_message(message.chat.id,'Отменен ❎',reply_markup=menu)
        await state.finish()
        return

    else:
        await bot.send_message(message.chat.id,'<i>Ваше имя: ...</i>')
        global otziv_text
        otziv_text = str(message.text)
        await rate.number.set()

        

########## - HANDLERS of state ##########

@dp.message_handler(content_types=['text'], state = rate.number)
async def get_channel_id(message,state: FSMContext):
    if message.text == 'Отмена ❌':
        await bot.send_message(message.chat.id,'Отменен ❎',reply_markup=menu)
        await state.finish()
        return
    else:
        await bot.send_message(message.chat.id,'<i>Ваш номер телефона: ...</i>')
        global type_of_rev
        type_of_rev =str(message.text)
        await rate.type.set()
########## - HANDLERS of state ##########

@dp.message_handler(content_types=['text'], state = rate.type)
async def get_channel_id(message,state: FSMContext):
    if message.text == 'Отмена ❌':
        await bot.send_message(message.chat.id,'Отменен ❎',reply_markup=menu)
        await state.finish()
        return
    else:
        await bot.send_message(message.chat.id,'<i>Пожалуйста укажите кем вы являетесь</i>',reply_markup=type_of_reviewer)
        global users_name
        users_name =str(message.text)
        await rate.text.set()
########## - HANDLERS of state ##########

@dp.message_handler(content_types=['text'], state = rate.text)
async def get_channel_id(message,state: FSMContext):
    if message.text == 'Отмена ❌':
        await bot.send_message(message.chat.id,'Отменен ❎',reply_markup=types.ReplyKeyboardRemove())
        await start_command(message)
        await state.finish()
        return
    else:
        global number
        number = str(message.text)
        await state.finish()
        await bot.send_message(Admins_id,f"""#отзыв {number}\n\nНомер телефона: <b>{users_name}</b>\nимя: <b>{type_of_rev}</b>\nотзыв: <b>{otziv_text}</b>\n""",reply_markup=types.ReplyKeyboardRemove())
        await bot.send_message(message.chat.id,"ваш отзыв отправлен администратору...",reply_markup=types.ReplyKeyboardRemove())

########## - HANDLERS of START COMMAND - START ##########

@dp.message_handler(commands=['start'])
async def start_command(message):
    await bot.send_photo(message.chat.id,"https://t.me/saveruz/12",caption="""<b>Добро пожаловать к нашему боту!</b>
        
<i>Выберите один из меню!</i> """,reply_markup=menu)
########## - HANDLERS of START COMMAND - END ##########



########## new update text handler  --  START ##########
@dp.message_handler(content_types=['text'])
async def text_update(message):
    if message.text == "TAN298":
        await bot.send_message(message.chat.id,"ooo axir siz TAN muxlisisizku malades")
        await bot.send_message(message.chat.id,"🙂")
        
    else:
            await bot.send_message(message.chat.id,'<i>Неизвестное сообщение</i>')
########## new update text handler -- END ##########

########## END - STATE handler ##########
@dp.callback_query_handler()
async def callbacks(call: types.CallbackQuery):

    if call.data == 'info':
        await bot.send_message(call.message.chat.id,"""выберите один из них, пожалуйста...   """,reply_markup=menu_of_allInfos)

    elif call.data == 'information':
        await bot.send_message(call.message.chat.id,"""<b>298 - School</b>
<i>Номер телефона:</i> <b>+998712494877</b>
<i>Aдрес:</i> <b>Olmazor tumani Beruniy B-1</b>

- - - - - - - - -

<i>Занятия проводятся на русском и узбекском языках. 
Количество учащихся – более 3200. 
На данный момент существует 95 классов. 
Количество преподавателей – 135. Из них 7 обладателей высших, 24 1-й категории, 35 2-й категории и международных сертификатов.</i>
""")
    elif call.data == 'location':
        await bot.copy_message(call.message.chat.id, '-1001576387195', 13)        
    elif call.data == 'rate':
        await rate.name.set()
        await bot.send_message(call.message.chat.id,'Пожалуйста, напишите свой отзыв...',reply_markup=cancel)
    ##################2
    elif call.data == 'teachers':
        await bot.send_message(call.message.chat.id,"""<code>1. Аметова Ольга Анатольевна 
2. Абдурасулова Гулшода Абдурасуловна
3. Ганиева Гуландом Хусниддиновна
4. Зимина Шахноза Шамирзаевна
5. Уроков Жамшид Махмадиёрович
6. Рузматова Дурдона Рустамовна
7. Саматова Зайнура Неъматовна </code>""")
        
    elif call.data == 'IT':
        await bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=LessonsMenu_IT)
    elif call.data == 'RUSSIAN':
        await bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=LessonsMenu_russia)
    elif call.data == 'ENGLISH':
        await bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=LessonsMenu_english)
    elif call.data == 'ss':
        pass

    elif call.data=='table':
        await bot.send_message(call.message.chat.id,"""<b>1 - смена </b>
<i>уроки начинаются - <code>8:00</code>

уроки заканчиваются - <code>13:05</code></i>
-  -  -   -   -   -
<b>2 - смена </b>
<i>уроки начинаются - <code>13:20</code>

уроки заканчиваются - <code>18:20</code></i>

""",reply_markup=classes)



    #####Classes
##############################    CALL.DATA -  start ##############################
    elif call.data == 'C1class':
        
        await bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=Class_1)
    elif call.data == 'C2class':
        
        await bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=Class_2)
    elif call.data == 'C3class':
        
        await bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=Class_3)
    elif call.data == 'C4class':
        
        await bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=Class_4)
    elif call.data == 'C5class':
        
        await bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=Class_5)
    elif call.data == 'C6class':
        
        await bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=Class_6)
    elif call.data == 'C7class':
        
        await bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=Class_7)
    elif call.data == 'C8class':
        
        await bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=Class_8)
    elif call.data == 'C9class':
        
        await bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=Class_9)
    elif call.data == 'C10class':
        
        await bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup= Class_10)
    elif call.data == 'C11class':
        
        await bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup= Class_11)
    elif call.data == 'menuu':
        await bot.delete_message(call.message.chat.id,call.message.message_id)
        await start_command(call.message)
    else:
        
        try:
            if 'week' in call.data:
                myday = call.data.replace('week_','day')
                print(myday)
                classes_name = '9_a'
                with open(f'{classes_name}/{myday}.txt') as f:
                    lines = f.read()
                    await bot.delete_message(call.message.chat.id,call.message.message_id)
                    await bot.send_message(call.message.chat.id,lines,reply_markup= week_days)
            else:
                await bot.send_message(call.message.chat.id,".",reply_markup= week_days)

                classes_name = call.data
        except Exception as e:
            print(e)
        
##############################    CALL.DATA -  END ##############################






##############################   START BOT ##############################

if __name__ == '__main__':
    print("Started ")
    executor.start_polling(dp, skip_updates=False)