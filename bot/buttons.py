from aiogram import *
b_info = types.InlineKeyboardButton('Информация ℹ︎', callback_data='info')
b_web = types.InlineKeyboardButton('Веб-сайт', url='https://298.netlify.app')
b_location = types.InlineKeyboardButton('Локация 📍', callback_data='location')
b_rate = types.InlineKeyboardButton('Оставить отзыв 🔖', callback_data='rate')
onlineDars = types.InlineKeyboardButton('- онлайн уроки 📚 - ', callback_data='ss')
RUUS = types.InlineKeyboardButton('Русский язык 🇷🇺', callback_data='RUSSIAN')
ENGG = types.InlineKeyboardButton('Английский язык 🇺🇸', callback_data='ENGLISH')
IT = types.InlineKeyboardButton('IT👨🏻‍💻', callback_data='IT')
menu = types.InlineKeyboardMarkup()
menu.add(b_info,b_location)
menu.add(b_rate,b_web)
menu.add(onlineDars)
menu.add(RUUS,ENGG,IT)
############# Online Lessons Buttons
#-English 
OnlineLesson1= types.InlineKeyboardButton(text = "1-dars",url='https://youtu.be/V98sNMEy3wE')
OnlineLesson2= types.InlineKeyboardButton(text = "2-dars",url='https://youtu.be/85fMQibGuP8')
OnlineLesson3= types.InlineKeyboardButton(text = "3-dars",url='https://youtu.be/OB5eCONr18I')
OnlineLesson4= types.InlineKeyboardButton(text = "4-dars",url='https://youtu.be/-ktzVGNoJSw')
OnlineLesson5= types.InlineKeyboardButton(text = "5-dars",url='https://youtu.be/-d0qQy06NRE')
OnlineLesson6= types.InlineKeyboardButton(text = "6-dars",url='https://youtu.be/yOkOHyNiR98')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
LessonsMenu_english = types.InlineKeyboardMarkup()
LessonsMenu_english.row(OnlineLesson1)
LessonsMenu_english.row(OnlineLesson2)
LessonsMenu_english.row(OnlineLesson3)
LessonsMenu_english.row(OnlineLesson4)
LessonsMenu_english.row(OnlineLesson5)
LessonsMenu_english.row(OnlineLesson6)
LessonsMenu_english.row(main_menu)
#Russia
OnlineLessonRu1= types.InlineKeyboardButton(text = "1-dars",url='https://youtu.be/FdCJA24HvOw')
OnlineLessonRu2= types.InlineKeyboardButton(text = "2-dars",url='https://youtu.be/2oSwqpDd3FE')
OnlineLessonRu3= types.InlineKeyboardButton(text = "3-dars",url='https://youtu.be/Nkj4Xe7eNwE')
OnlineLessonRu4= types.InlineKeyboardButton(text = "4-dars",url='https://youtu.be/FzjipqXJGyo')
OnlineLessonRu5= types.InlineKeyboardButton(text = "5-dars",url='https://youtu.be/imIWMdNvbxU')
OnlineLessonRu6= types.InlineKeyboardButton(text = "6-dars",url='https://youtu.be/e19exGmNjdk')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
LessonsMenu_russia = types.InlineKeyboardMarkup()
LessonsMenu_russia.row(OnlineLessonRu1)
LessonsMenu_russia.row(OnlineLessonRu2)
LessonsMenu_russia.row(OnlineLessonRu3)
LessonsMenu_russia.row(OnlineLessonRu4)
LessonsMenu_russia.row(OnlineLessonRu5)
LessonsMenu_russia.row(OnlineLessonRu6)
LessonsMenu_russia.row(main_menu)
#IT
OnlineLessonIT1= types.InlineKeyboardButton(text = "1-dars",url='https://youtu.be/fj_GLU344bQ')
OnlineLessonIT2= types.InlineKeyboardButton(text = "2-dars",url='https://youtu.be/Q3H1OUj_XU8')
OnlineLessonIT3= types.InlineKeyboardButton(text = "3-dars",url='https://youtu.be/-haxzF1rzZ0')
OnlineLessonIT4= types.InlineKeyboardButton(text = "4-dars",url='https://youtu.be/slMBSFsORow?t=1')
OnlineLessonIT5= types.InlineKeyboardButton(text = "5-dars",url='https://youtu.be/o5XIOTLBPIU')
OnlineLessonIT6= types.InlineKeyboardButton(text = "6-dars",url='https://youtu.be/ixc2mq0FKHA')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
LessonsMenu_IT = types.InlineKeyboardMarkup()
LessonsMenu_IT.row(OnlineLessonIT1)
LessonsMenu_IT.row(OnlineLessonIT2)
LessonsMenu_IT.row(OnlineLessonIT3)
LessonsMenu_IT.row(OnlineLessonIT4)
LessonsMenu_IT.row(OnlineLessonIT5)
LessonsMenu_IT.row(OnlineLessonIT6)
LessonsMenu_IT.row(main_menu)

############## END ONLINE LESSON


parent = types.KeyboardButton('👨‍👨‍👧 Я родитель')
student = types.KeyboardButton('👨‍🎓 Я студент')
guest = types.KeyboardButton('🙎‍♂️ Я гость')
type_of_reviewer = types.ReplyKeyboardMarkup()
type_of_reviewer.add(parent,student)
type_of_reviewer.add(guest)


cancel = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
c_b = types.KeyboardButton("Отмена ❌")
cancel.row(c_b)



teachers = types.InlineKeyboardButton(text = "учителя с высшей категории 🧑🏻‍🏫",callback_data='teachers')
table_time = types.InlineKeyboardButton(text = "расписание",callback_data='table')
infos = types.InlineKeyboardButton(text = "Полная информация ℹ️",callback_data='information')
menu_of_allInfos = types.InlineKeyboardMarkup()
menu_of_allInfos.row(teachers)
menu_of_allInfos.row(table_time)
menu_of_allInfos.row(infos)



A1 = types.InlineKeyboardButton(text = "1 - A",callback_data='1_a')
B1 = types.InlineKeyboardButton(text = "1 - B",callback_data='1_b')
C1 = types.InlineKeyboardButton(text = "1 - C",callback_data='1_c')
Z1 = types.InlineKeyboardButton(text = "1 - Z",callback_data='1_z')
J1 = types.InlineKeyboardButton(text = "1 - J",callback_data='1_j')
E1 = types.InlineKeyboardButton(text = "1 - E",callback_data='1_e')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
Class_1 = types.InlineKeyboardMarkup()
Class_1.row(A1)
Class_1.row(B1)
Class_1.row(C1)
Class_1.row(Z1)
Class_1.row(J1)
Class_1.row(E1)
Class_1.row(main_menu)



A2 = types.InlineKeyboardButton(text = "2 - A",callback_data='2_a')
B2 = types.InlineKeyboardButton(text = "2 - B",callback_data='2_b')
E2 = types.InlineKeyboardButton(text = "2 - E",callback_data='2_e')
J2 = types.InlineKeyboardButton(text = "2 - J",callback_data='2_h')
L2 = types.InlineKeyboardButton(text = "2 - L",callback_data='2_l')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
Class_2 = types.InlineKeyboardMarkup()
Class_2.row(A2)
Class_2.row(B2)
Class_2.row(E2)
Class_2.row(L2)
Class_2.row(J2) 
Class_2.row(main_menu)

A3 = types.InlineKeyboardButton(text = "3 - A",callback_data='3_a')
B3 = types.InlineKeyboardButton(text = "3 - B",callback_data='3_b')
C3 = types.InlineKeyboardButton(text = "3 - C",callback_data='3_c')
I3 = types.InlineKeyboardButton(text = "3 - I",callback_data='3_i')
J3 = types.InlineKeyboardButton(text = "3 - J",callback_data='3_j')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
Class_3 = types.InlineKeyboardMarkup()
Class_3.row(A3)
Class_3.row(B3)
Class_3.row(C3)
Class_3.row(I3)
Class_3.row(J3)
Class_2.row(main_menu)


A4 = types.InlineKeyboardButton(text = "4 - A",callback_data='4_a')
B4 = types.InlineKeyboardButton(text = "4 - B",callback_data='4_b')
C4 = types.InlineKeyboardButton(text = "4 - C",callback_data='4_c')
J4 = types.InlineKeyboardButton(text = "4 - J",callback_data='4_j')
L4 = types.InlineKeyboardButton(text = "4 - L",callback_data='4_l')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
Class_4 = types.InlineKeyboardMarkup()
Class_4.row(A4)
Class_4.row(B4)
Class_4.row(C4)
Class_4.row(J4)
Class_4.row(L4)
Class_4.row(main_menu)

#######Nachalniy

A5 = types.InlineKeyboardButton(text = "5 - A",callback_data='5_A')
B5 = types.InlineKeyboardButton(text = "5 - B",callback_data='5_B')
C5 = types.InlineKeyboardButton(text = "5 - C",callback_data='5_C')
E5 = types.InlineKeyboardButton(text = "5 - E",callback_data='5_E')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
Class_5 = types.InlineKeyboardMarkup()
Class_5.row(A5)
Class_5.row(B5)
Class_5.row(C5)
Class_5.row(E5)
Class_5.row(main_menu)

A6 = types.InlineKeyboardButton(text = "6 - A",callback_data='6_A')
B6 = types.InlineKeyboardButton(text = "6 - B",callback_data='6_B')
C6 = types.InlineKeyboardButton(text = "6 - C",callback_data='6_C')
E6 = types.InlineKeyboardButton(text = "6 - E",callback_data='6_E')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
Class_6 = types.InlineKeyboardMarkup()
Class_6.row(A6)
Class_6.row(B6)
Class_6.row(C6)
Class_6.row(E6)
Class_6.row(main_menu)
A7 = types.InlineKeyboardButton(text = "7 - A",callback_data='7_A')
B7 = types.InlineKeyboardButton(text = "7 - B",callback_data='7_B')
C7 = types.InlineKeyboardButton(text = "7 - C",callback_data='7_C')
E7 = types.InlineKeyboardButton(text = "7 - E",callback_data='7_E')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
Class_7 = types.InlineKeyboardMarkup()
Class_7.row(A7)
Class_7.row(B7)
Class_7.row(C7)
Class_7.row(E7)
Class_7.row(main_menu)
A8 = types.InlineKeyboardButton(text = "8 - A",callback_data='8_A')
B8 = types.InlineKeyboardButton(text = "8 - B",callback_data='8_B')
C8 = types.InlineKeyboardButton(text = "8 - C",callback_data='8_C')
E8 = types.InlineKeyboardButton(text = "8 - E",callback_data='8_E')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
Class_8 = types.InlineKeyboardMarkup()
Class_8.row(A8)
Class_8.row(B8)
Class_8.row(C8)
Class_8.row(E8)
Class_8.row(main_menu)
A9 = types.InlineKeyboardButton(text = "9 - A",callback_data='9_A')
B9 = types.InlineKeyboardButton(text = "9 - B",callback_data='9_B')
C9 = types.InlineKeyboardButton(text = "9 - C",callback_data='9_C')
E9 = types.InlineKeyboardButton(text = "9 - E",callback_data='9_E')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
Class_9 = types.InlineKeyboardMarkup()
Class_9.row(A9)
Class_9.row(B9)
Class_9.row(C9)
Class_9.row(E9)
Class_9.row(main_menu)

A10 = types.InlineKeyboardButton(text = "10 - A",callback_data='10_A')
B10 = types.InlineKeyboardButton(text = "10 - B",callback_data='10_B')
C10 = types.InlineKeyboardButton(text = "10 - C",callback_data='10_C')
E10 = types.InlineKeyboardButton(text = "10 - E",callback_data='10_E')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
Class_10 = types.InlineKeyboardMarkup()
Class_10.row(A10)
Class_10.row(B10)
Class_10.row(C10)
Class_10.row(E10)
Class_10.row(main_menu)

A11 = types.InlineKeyboardButton(text = "11 - A",callback_data='11_A')
B11 = types.InlineKeyboardButton(text = "11 - B",callback_data='11_B')
C11 = types.InlineKeyboardButton(text = "11 - C",callback_data='11_C')
E11 = types.InlineKeyboardButton(text = "11 - E",callback_data='11_E')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
Class_11 = types.InlineKeyboardMarkup()
Class_11.row(A11)
Class_11.row(B11)
Class_11.row(C11)
Class_11.row(E11)
Class_11.row(main_menu)


C1 = types.InlineKeyboardButton(text = "класс  - 1",callback_data='C1class')
C2 = types.InlineKeyboardButton(text = "класс  - 2",callback_data='C2class')
C3 = types.InlineKeyboardButton(text = "класс  - 3",callback_data='C3class')
C4 = types.InlineKeyboardButton(text = "класс  - 4",callback_data='C4class')
C5 = types.InlineKeyboardButton(text = "класс  - 5",callback_data='C5class')
C6 = types.InlineKeyboardButton(text = "класс  - 6",callback_data='C6class')
C7 = types.InlineKeyboardButton(text = "класс  - 7",callback_data='C7class')
C8 = types.InlineKeyboardButton(text = "класс  - 8",callback_data='C8class')
C9 = types.InlineKeyboardButton(text = "класс  - 9",callback_data='C9class')
C10 = types.InlineKeyboardButton(text = "класс  - 10",callback_data='C10class')
C11 = types.InlineKeyboardButton(text = "класс  - 11",callback_data='C11class')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
classes = types.InlineKeyboardMarkup()
classes.row(C1)
classes.row(C2)
classes.row(C3)
classes.row(C4)
classes.row(C5)
classes.row(C6)
classes.row(C7)
classes.row(C8)
classes.row(C9)
classes.row(C10)
classes.row(C11)
classes.row(main_menu)



#days 


C1_days = types.InlineKeyboardButton(text = "1 - понедельник",callback_data='week_1')
C2_days = types.InlineKeyboardButton(text = "2 - вторник",callback_data='week_2')
C3_days = types.InlineKeyboardButton(text = "3 - среда",callback_data='week_3')
C4_days = types.InlineKeyboardButton(text = "4 - четверг",callback_data='week_4')
C5_days = types.InlineKeyboardButton(text = "5 - пятница",callback_data='week_5')
C6_days = types.InlineKeyboardButton(text = "6 - суббота",callback_data='week_6')
main_menu = types.InlineKeyboardButton(text = 'главное меню 🏠',callback_data = "menuu")
week_days = types.InlineKeyboardMarkup()
week_days.row(C1_days)
week_days.row(C2_days)
week_days.row(C3_days)
week_days.row(C4_days)
week_days.row(C5_days)
week_days.row(C6_days)
classes.row(main_menu)



