import time
from whatsapp_chatbot_python import GreenAPIBot, Notification, BaseStates
from BotWA import *
from scenariosmiss import *
from scenariosmsk import *
from dialoguemsk import *
from dialoguemiss import *
from whatsapp_api_client_python import API
from requests import request
from pprint import pprint
from main import post_lead
from os import environ
from test import get_list, get_txt

bot = GreenAPIBot(id_instance, api_token_instance)

greenAPI = API.GreenAPI(id_instance, api_token_instance)


class Conversationmsk(BaseStates):
    USERNAME = 'Name'
    CITY = 'City'
    DATE = 'DATE'
    PEOPLE = ' PL'
    PROGRAM = 'PG'


class Conversationmiss(BaseStates):
    USERNAME = 'Имя'
    CITY = 'Город'
    DATE= 'Дата'
    PEOPLE = 'Peopl'
    PROGRAM = 'Progm'


class Soaring_Msk(BaseStates):
    STEP_1 = 'Step'


class Soaring_Miss(BaseStates):
    STEP_1 = 'ШАГ'


class How(BaseStates):
    STEP_1 = 'Step1'
    STEP_2 = 'Step2'


class Bookingmsk(BaseStates):
    USERNAME = 'NAME'
    CITY = 'CITY'
    DATA = 'DATA'
    PEOPLE = 'People2'
    PROGRAM = 'Program2'


class Bookingmiss(BaseStates):
    USERNAME = 'NAME1'
    CITY = 'CITY1'
    DATA = 'DATA1'
    PROGRAM = 'PROGRAM1'
    PEOPLE = 'POEPLE1'


class HowWas(BaseStates):
    STEP1 = 'Печенье'
    STEP2 = 'Чай'


class HowBass(BaseStates):
    How1 = 'Про'
    How2 = 'Пра'


class Auth(BaseStates):
    MOSCOW = 'Москва'
    CHELYABINSK_MISS = 'Челябинск'
    STATE = ''
    SOARING = ''
    HOW_WAS_IT = ''


@bot.router.message(regexp=r'[\W]*([тТ][еЕ][мМ][аА])[\W]*([бБ][аА][нН][яЯ][\W]*)', state=None)
def message_yes(mess:Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.STATE.value)
    mess.answer(text_70)


@bot.router.message(type_message=filters.TEXT_TYPES, state=None)
def an_message(mess: Notification) -> None:
    sender = mess.sender
    mess.answer("""
*Я не волшебник, я только учусь Вас понимать.*
*Напишите мне:*
*Тема Баня*
*И точно следуйте подсказкам.*""")


@bot.router.message(text_message=["1", "Москва", "МОСКВА", "москва"], state=Auth.STATE.value)
def msk_handler(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.set_state(sender, Auth.MOSCOW.value)
    mess.answer(text_10)
    mess.answer(funct_msk)


@bot.router.message(text_message='1', state=Auth.MOSCOW.value)
def msk_handler_a(mess: Notification) -> None:
    sender = mess.sender
    mess.answer(text_22)
    mess.answer(text_301)
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)


@bot.router.message(text_message='2', state=Auth.MOSCOW.value)
def msk_handler_b(mess: Notification) -> None:
    sender = mess.sender
    text = mess.message_text
    # mess.state_manager.set_state(sender,How_Was_It_Msk.STEP2.value)
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    mess.answer(text_23)
    mess.answer(text_302)


@bot.router.message(text_message='3', state=Auth.MOSCOW.value)
def msk_handler_v(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    mess.answer(text_24)
    mess.answer(text_303)


@bot.router.message(text_message='4', state=Auth.MOSCOW.value)
def msk_handler_g(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    mess.answer(text_25)
    mess.answer(text_304)


@bot.router.message(text_message='5', state=Auth.MOSCOW.value)
def msk_handler_d(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    mess.answer(text_26)
    mess.answer(text_305)


@bot.router.message(text_message='6', state=Auth.MOSCOW.value)
def msk_handler_e(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    mess.answer(text_27)
    mess.answer(text_306)


@bot.router.message(text_message='7', state=Auth.MOSCOW.value)
def msk_handler_e(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    mess.answer(text_28)
    mess.answer(text_307)


@bot.router.message(text_message='Б', state=Auth.MOSCOW.value)
def msk_handler_e(mess: Notification) -> None:
    sender = mess.sender
    mess.answer(text_100)
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    mess.answer(text_101)


@bot.router.message(text_message='Г', state=Auth.MOSCOW.value)
def how_hendler(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, How.STEP_1.value)
    mess.answer('*Напишите цифру программы*')


@bot.router.message(state=How.STEP_1.value)
def how(mess: Notification) -> None:
    sender = mess.sender
    message = mess.message_text
    try:
        if message not in ["1", "2", "3", "4", "5", "6", "7"]:
            mess.answer('*Напиши цифру*')
            mess.state_manager.update_state(sender, HowWas.STEP1.value)
        elif message == '1':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_4657.MP4',
                                                    'IMG_4657.MP4',
                                                    '*«Банная ВечЁрка»*\nhttps://vk.com/wall-169974497_14581')
            mess.answer(text_101)

            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '2':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_3812.MP4',
                                                    'IMG_3812.MP4', '*«ДРУЖНАЯ БАНЯ»*\nhttps://vk.com/wall-169974497_14235')
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '3':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_4653.MP4',
                                                    'IMG_4653.MP4',
                                                    '*«БАННЫЙ КОРПОРАТИВ»*\nhttps://vk.com/wall-169974497_14315')

            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '4':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_4664.MP4',
                                                    'IMG_4664.MP4', '*«БАЛАНС БАНЯ»*\nhttps://vk.com/wall-169974497_12815')
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '5':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_4656.MP4',
                                                    'IMG_4656.MP4',
                                                    '*«МОРСКОЕ ПУТЕШЕСТВИЕ»*\nhttps://vk.com/wall-169974497_8235')
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '6':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_4656.MP4',
                                                    'IMG_4656.MP4', '*«СТРУНА БАНЯ»*\nhttps://vk.com/wall-169974497_8235')

            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '7':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_5555.mp4',
                                                    'IMG_5555.MP4', '*«Семейная программа»*\nhttps://vk.com/wall-169974497_3512')

            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    except Exception as e:
        mess.answer('Error')


@bot.router.message(text_message='В', state=Auth.MOSCOW.value)
def certificate(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Conversationmsk.USERNAME.value)
    mess.answer('*Как вас звать-величать?*')


@bot.router.message(state=Conversationmsk.USERNAME.value)
def certificate_1(mess: Notification) -> None:
    sender = mess.sender
    user_name = str(mess.message_text)
    try:
        if not 2 <= len(user_name) <= 50:
            mess.answer('*Введите корректно Имя*')
            mess.state_manager.set_state(sender, Conversationmsk.USERNAME.value)
        else:
            mess.state_manager.update_state(sender, Conversationmsk.PEOPLE.value)
            mess.state_manager.update_state_data(sender, {"Имя": user_name})
            mess.answer('*Сколько человек планируется в гости на пар?*')
    except Exception as e:
        mess.answer('Ошибка!')


@bot.router.message(state=Conversationmsk.PEOPLE.value)
def certificate_1(mess: Notification) -> None:
    sender = mess.sender
    people = str(mess.message_text)
    state = mess.state_manager.get_state_data(sender)
    user = state["Имя"]
    try:
        if not 1 <= len(people) <= 10:
            mess.answer('*Введите корректно сколько гостей*')
            mess.state_manager.set_state(sender, Conversationmsk.PEOPLE.value)
        else:
            mess.state_manager.update_state(sender, Conversationmsk.PROGRAM.value)
            mess.state_manager.update_state_data(sender, {"Люди": people})
            mess.answer('*Укажите какая программа приглянулась?*')
    except Exception as e:
        mess.answer('Ошибка!')


@bot.router.message(state=Conversationmsk.PROGRAM.value)
def certificate_1(mess: Notification) -> None:
    sender = mess.sender
    program = str(mess.message_text)
    state = mess.state_manager.get_state_data(sender)
    user = state["Имя"]
    people = state["Люди"]
    try:
        if not 1 <= len(program) <= 20:
            mess.answer('*Введите корректно программу*')
            mess.state_manager.set_state(sender, Conversationmsk.USERNAME.value)
        else:
            mess.state_manager.update_state(sender, Conversationmsk.CITY.value)
            mess.state_manager.update_state_data(sender, {"Программа": program})
            mess.answer('*В каком городе изволите попариться?*')
    except Exception as e:
        mess.answer('Ошибка!')


@bot.router.message(state=Conversationmsk.CITY.value)
def certificate_1(mess: Notification) -> None:
    sender = mess.sender
    city = str(mess.message_text)
    state = mess.state_manager.get_state_data(sender)
    user = state["Имя"]
    people = state["Люди"]
    program = state["Программа"]
    try:
        if not 1 <= len(city) <= 20:
            mess.answer('*Введите корректно Город*')
            mess.state_manager.set_state(sender, Conversationmsk.USERNAME.value)
        else:
            mess.state_manager.update_state(sender, Conversationmsk.DATE.value)
            mess.state_manager.update_state_data(sender, {"Город": city})
            mess.answer('*Подскажи желаемую дату банного отдыха*')
    except Exception as e:
        mess.answer('Ошибка!')


@bot.router.message(state=Conversationmsk.DATE.value)
def certificate_3(mess: Notification) -> None:
    sender = mess.sender
    date = str(mess.message_text)
    data = mess.state_manager.get_state_data(sender)
    user_name = data["Имя"]
    city = data["Город"]
    people = data["Люди"]
    program = data["Программа"]
    consult = 'Консультация'
    try:
        if not 4 <= len(date) <= 20:
            mess.answer('*Введите корректно Дату*')
            mess.state_manager.update_state(sender, Conversationmsk.DATE.value)
        else:
            mess.state_manager.update_state_data(sender, {"Дата": date})
            mess.answer('*Я всё записал, отправил телеграмму хозяйке, вскоре с Вами свяжется- Анна Пихта.*')
            #message = greenAPI.sending.sendMessage("79610344938@c.us", "Требуется разговор с Менеджером\n\n"
            #print(post_lead(user_name, city, date, people, program, sender[0:11], consult))
            vbot.send_message('79630906000@c.us', 'Требуется разговор с Менеджером\\n'
                    f'Имя: {user_name}.\\n'
                    f'Город: {city}.\\n'
                    f'Дата: {date}.\\n'
                    f'Номер: {sender[0:11]}.\\n'
                    f'Гости: {people}\\n'
                    f'Программа: {program}'
                    )
            # mess.answer(text_65)
            mess.answer(text_102)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    except Exception as e:
        mess.answer('*Что-то не так*')


@bot.router.message(text_message='Ж', state=Auth.MOSCOW.value)
def rout(mess: Notification) -> None:
    sender = mess.sender
    mess.answer('*Введите цифру программы*')
    mess.state_manager.set_state(sender, HowWas.STEP1.value)


@bot.router.message(state=HowWas.STEP1.value)
def rout(mess: Notification) -> None:
    sender = mess.sender
    message = mess.message_text
    try:
        if message not in ["1", "2", "3", "4", "5", "6", "7"]:
            mess.answer('*Напиши цифру*')
            mess.state_manager.update_state(sender, HowWas.STEP1.value)
        elif message == '1':
            sender = mess.sender
            mess.answer(text_200)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '2':
            mess.answer(text_201)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '3':
            mess.answer(text_202)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '4':
            mess.answer(text_203)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '5':
            mess.answer(text_204)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '6':
            mess.answer(text_205)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '7':
            mess.answer(text_207)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    except Exception as e:
        mess.answer('Error')


@bot.router.message(text_message='Д', state=Auth.MOSCOW.value)
def f_consult(mess: Notification) -> None:
    sender = mess.sender
    mess.answer(text_63)
    mess.answer(text_101)
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)


@bot.router.message(text_message='М', state=Auth.MOSCOW.value)
def f_consult(mess: Notification) -> None:
    sender = mess.sender
    mess.answer(text_10)
    mess.answer(text_30)
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)



@bot.router.message(text_message='Меню', state=Auth.MOSCOW.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Тема Баня', state=Auth.MOSCOW.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Тема баня', state=Auth.MOSCOW.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Auth.STATE.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Тема Баня', state=Auth.STATE.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Тема баня', state=Auth.STATE.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Тема Баня', state=Auth.CHELYABINSK_MISS.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Тема баня', state=Auth.CHELYABINSK_MISS.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Auth.CHELYABINSK_MISS.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Auth.SOARING.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Auth.HOW_WAS_IT.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Conversationmsk.USERNAME.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Conversationmsk.CITY.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Conversationmsk.DATE.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Conversationmsk.PEOPLE.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Conversationmsk.PROGRAM.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Conversationmiss.USERNAME.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Conversationmiss.CITY.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Conversationmiss.DATE.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Conversationmiss.PEOPLE.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Conversationmiss.PROGRAM.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Bookingmsk.USERNAME.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Bookingmsk.CITY.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Bookingmsk.PEOPLE.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Bookingmsk.PROGRAM.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Bookingmiss.USERNAME.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Bookingmiss.CITY.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Bookingmiss.PEOPLE.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='Меню', state=Bookingmiss.PROGRAM.value)
def exit(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Вы в главном меню*')
    mess.answer(text_70)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='К', state=Auth.MOSCOW.value)
def how(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Введите цифру программы*')
    mess.state_manager.update_state(sender, HowBass.How1.value)


@bot.router.message(state=HowBass.How1.value)
def how_1(mess: Notification) -> None:
    sender = mess.sender
    message = mess.message_text
    try:
        if message not in ["1", "2", "3", "4", "5", "6", "7"]:
            mess.answer('*Напиши цифру*')
            mess.state_manager.update_state(sender, HowBass.How1.value)
        elif message == '1':
            mess.answer(text_123)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '2':
            mess.answer(text_125)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '3':
            mess.answer(text_124)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '4':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_8820.MP4',
                                                    'IMG_8820.MP4', text_126)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '5':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_8820.MP4',
                                                    'IMG_8820.MP4', """*«МОРСКОЕ ПУТЕШЕСТВИЕ»*\n📍 Адрес:
                                                                        Салтан Баня
                                                                        https://yandex.ru/maps/org/147745164760
                                                                        Баня-Сенсация!
                                                                        Сруб из огромнейшего кедра, в мотивах сказок Пушкина о царе Салтане, массив, русский стиль, резьба. Печь по-серому и белому, вкуснейший пар, обходной полог, ЧАН на свежем воздухе, ледяной колодец, сенные качели. Природа, уют, энергетика!
                                                                        Выбор ЧЕМПИОНОВ! Лучшая Баня из всех, где Ты был!
                                                                        Дата проведения:
                                                                        С 20 по 29.02 с 10:00, с 15:00 или с 20:00
                                                                        """)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '6':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_8820.MP4',
                                                    'IMG_8820.MP4', """*«СТРУНА БАНЯ»*\n📍 Адрес:
                                                                        Салтан Баня
                                                                        https://yandex.ru/maps/org/147745164760
                                                                        Баня-Сенсация!
                                                                        Сруб из огромнейшего кедра, в мотивах сказок Пушкина о царе Салтане, массив, русский стиль, резьба. Печь по-серому и белому, вкуснейший пар, обходной полог, ЧАН на свежем воздухе, ледяной колодец, сенные качели. Природа, уют, энергетика!
                                                                        Выбор ЧЕМПИОНОВ! Лучшая Баня из всех, где Ты был!
                                                                        Дата проведения:
                                                                        С 20 по 29.02 с 10:00, с 15:00 или с 20:00
                                                                        """)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
        elif message == '7':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_8820.MP4',
                                                    'IMG_8820.MP4', """*«Семейная программа»*\n📍 Адрес:
                                                                        Салтан Баня
                                                                        https://yandex.ru/maps/org/147745164760
                                                                        Баня-Сенсация!
                                                                        Сруб из огромнейшего кедра, в мотивах сказок Пушкина о царе Салтане, массив, русский стиль, резьба. Печь по-серому и белому, вкуснейший пар, обходной полог, ЧАН на свежем воздухе, ледяной колодец, сенные качели. Природа, уют, энергетика!
                                                                        Выбор ЧЕМПИОНОВ! Лучшая Баня из всех, где Ты был!
                                                                        Дата проведения:
                                                                        С 20 по 29.02 с 10:00, с 15:00 или с 20:00
                                                                        """)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    except Exception as e:
        mess.answer('Error')


@bot.router.message(text_message=['Да','ДА','да','дА'], state=Auth.MOSCOW.value)
def rename(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.set_state(sender, Bookingmsk.USERNAME.value)
    mess.answer('*Как тебя звать-величать?*')


@bot.router.message(state=Bookingmsk.USERNAME.value)
def rename_1(mess: Notification) -> None:
    sender = mess.sender
    user_name = str(mess.message_text)
    try:
        if not 2 <= len(user_name) <= 50:
            mess.answer('*Введите корректно Имя*')
            mess.state_manager.set_state(sender, Bookingmsk.USERNAME.value)
        else:
            state = mess.state_manager.update_state_data(sender, {"Имя": user_name})
            mess.state_manager.update_state(sender, Bookingmsk.PEOPLE.value)
            mess.answer('*Сколько человек планируется в гости на пар?*')
    except Exception as e:
        mess.answer('*Что-то не так!*')


@bot.router.message(state=Bookingmsk.PEOPLE.value)
def rename_1(mess: Notification) -> None:
    sender = mess.sender
    people = str(mess.message_text)
    date = mess.state_manager.get_state_data(sender)
    name = date["Имя"]
    try:
        if not 1 <= len(people) <= 20:
                mess.answer("*Введидете корректно сколько гостей*")
                mess.state_manager.set_state(sender, Bookingmsk.CITY.value)
                pass
        else:
            state = mess.state_manager.update_state_data(sender, {"Люди": people})
            mess.state_manager.update_state(sender, Bookingmsk.PROGRAM.value)
            mess.answer('*Укажите какая программа приглянулась?*')
            pass
    except Exception as e:
        mess.answer("*Что-то не так*")


@bot.router.message(state=Bookingmsk.PROGRAM.value)
def rename_1(mess: Notification) -> None:
    sender = mess.sender
    program = str(mess.message_text)
    date = mess.state_manager.get_state_data(sender)
    name = date["Имя"]
    try:
        if not 1 <= len(program) <= 20:
                mess.answer("*Введите корректно программу*")
                mess.state_manager.set_state(sender, Bookingmsk.CITY.value)
                pass
        else:
            state = mess.state_manager.update_state_data(sender, {"Программа": program})
            mess.state_manager.update_state(sender, Bookingmsk.CITY.value)
            mess.answer('*Русь большая,в каком городе будем париться?*')
            pass
    except Exception as e:
        mess.answer("*Что-то пошло не так*")


@bot.router.message(state=Bookingmsk.CITY.value)
def rename_1(mess: Notification) -> None:
    sender = mess.sender
    city = str(mess.message_text)
    date = mess.state_manager.get_state_data(sender)
    #name = date["Имя"]
    try:
        if not 1 <= len(city) <= 20:
                mess.answer("*Введите корректно город*")
                mess.state_manager.set_state(sender, Bookingmsk.CITY.value)
                pass
        else:
            state = mess.state_manager.update_state_data(sender, {"Город": city})
            mess.state_manager.update_state(sender, Bookingmsk.DATA.value)
            mess.answer('*Подскажи желаемую дату банного отдыха*')
            pass
    except Exception as e:
        mess.answer("*Что-то пошло не так*")


@bot.router.message(state=Bookingmsk.DATA.value)
def rename_2(mess: Notification) -> None:
    sender = mess.sender
    date = str(mess.message_text)
    state = mess.state_manager.get_state_data(sender)
    name = state["Имя"]
    city = state["Город"]
    people = state["Люди"]
    program = state["Программа"]
    booking = 'Бронирование'
    try:
        if not 2 <= len(date) <= 15:
            mess.answer("*Введите корректно дату*")
            mess.state_manager.update_state(sender, Bookingmsk.DATA.value)
        else:
            print(post_lead(name, city, date, sender[0:11], booking, people, program))
            state = mess.state_manager.update_state_data(sender, {"Дата": date})
            vbot.send_message('79630906000@c.us', 'Бронирование!\\n'
                                                  f'Имя: {name}.\\n'
                                                  f'Город: {city}.\\n'
                                                  f'Дата: {date}.\\n'
                                                  f'Номер: {sender[0:11]}.\\n'
                                                  f'Люди: {people}\\n'
                                                  f'Программа: {program}'
                              )
            mess.answer(text_111)
            mess.answer(text_103)
            mess.state_manager.delete_state(sender)
            mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    except Exception as e:
        mess.answer('*Что-то пошло не так!*')


@bot.router.message(text_message='П', state=Auth.MOSCOW.value)
def bay(mess:Notification) -> None:
    sender = mess.sender
    mess.answer(text_65)
    mess.state_manager.update_state(sender, Auth.STATE.value)
    mess.answer(text_70)


@bot.router.message(text_message='А', state=Auth.MOSCOW.value)
def miss_handler(mess: Notification) -> None:
    sender = mess.sender
    mess.answer(text_12)
    mess.answer(text_101)
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)


@bot.router.message(regexp=r'[\W]*([тТ][еЕ][мМ][аА])[\W]*([бБ][аА][нН][яЯ][\W]*)', state=Auth.MOSCOW.value)
def message_yes(mess:Notification) -> None:
    sender = mess.sender
    mess.answer(text_10)
    mess.answer(text_30)
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)


@bot.router.message(type_message=filters.TEXT_TYPES, state=Auth.MOSCOW.value)
def an_message(mess: Notification) -> None:
    sender = mess.sender
    mess.answer("""
*Я не волшебник, я только учусь Вас понимать.*
*Напишите мне:*
*Тема Баня*
*И точно следуйте подсказкам.*""")
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)


@bot.router.message(text_message=["2", "Миасс", "МИАСС", "миасс", "Миас", "миас", "МИАС", "Челябинск", "ЧЕЛЯБИНСК", "челябинск"], state=Auth.STATE.value)
def miss_handler(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.set_state(sender, Auth.CHELYABINSK_MISS.value)
    mess.answer(text_1)
    mess.answer(text_30)


@bot.router.message(text_message='1', state=Auth.CHELYABINSK_MISS.value)
def msk_handler_a(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
    mess.answer(text_33)
    mess.answer(text_401)


@bot.router.message(text_message='2', state=Auth.CHELYABINSK_MISS.value)
def msk_handler_b(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
    mess.answer(text_34)
    mess.answer(text_402)


@bot.router.message(text_message='3', state=Auth.CHELYABINSK_MISS.value)
def msk_handler_v(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
    mess.answer(text_35)
    mess.answer(text_403)


@bot.router.message(text_message='4', state=Auth.CHELYABINSK_MISS.value)
def msk_handler_g(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
    mess.answer(text_36)
    mess.answer(text_404)


@bot.router.message(text_message='5', state=Auth.CHELYABINSK_MISS.value)
def msk_handler_d(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
    mess.answer(text_37)
    mess.answer(text_405)


@bot.router.message(text_message='6', state=Auth.CHELYABINSK_MISS.value)
def msk_handler_e(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
    mess.answer(text_38)
    mess.answer(text_406)


@bot.router.message(text_message='7', state=Auth.CHELYABINSK_MISS.value)
def certificate(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.set_state(sender, Auth.CHELYABINSK_MISS.value)
    mess.answer(text_39)
    mess.answer(text_407)


@bot.router.message(text_message='8', state=Auth.CHELYABINSK_MISS.value)
def certificate(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.set_state(sender, Auth.CHELYABINSK_MISS.value)
    mess.answer(text_45)
    mess.answer(text_408)


@bot.router.message(text_message='Г', state=Auth.CHELYABINSK_MISS.value)
def how_hendler(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender,How.STEP_2.value )
    mess.answer('*Напишите цифру программы*')


@bot.router.message(state=How.STEP_2.value)
def how(mess: Notification) -> None:
    sender = mess.sender
    message = mess.message_text
    try:
        if message not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            mess.answer('*Напиши цифру*')
            mess.state_manager.update_state(sender, HowWas.STEP1.value)
        elif message == '1':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_4658.MP4',
                                                    'IMG_4658.MP4', """*«Бизнес Баня»*\n"Бизнес Баня"- Парение и Нетворкинг для предпринимателей- управленцев твоего города.
                                                                    5 восхитительных коллективных парений,
                                                                    8 предпринимателей,
                                                                    Крутое окружение, общение-обогащение,
                                                                    Ужин, угощения, напитки.\nhttps://vk.com/wall-169974497_14423""")
            mess.answer(text_101)

            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '2':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_4653.MP4',
                                                    'IMG_4653.MP4', '*«БАННЫЙ КОРПОРАТИВ»*\nhttps://vk.com/wall-169974497_14315')
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '3':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_4657.MP4',
                                                    'IMG_4657.MP4', '*«Дружная Баня»*\nhttps://vk.com/wall-169974497_14581')

            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '4':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_5555.mp4',
                                                    'IMG_5555.mp4', '*«СЕМЕЙНАЯ БАНЯ»*\nhttps://vk.com/wall-169974497_3512')
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '5':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_4656.MP4',
                                                    'IMG_4656.MP4', '*«КЛАСИЧЕСКОЕ ПАРЕНИЕ»*\nhttps://vk.com/wall-169974497_3746\nhttps://vk.com/album-169974497_282891853')
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '6':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_4656.MP4',
                                                    'IMG_4656.MP4', '*«МОРСКОЕ ПУТЕШЕСТВИЕ»*\nhttps://vk.com/wall-169974497_8235')

            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '7':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                    'media/IMG_4656.MP4',
                                                    'IMG_4656.MP4', '*«СТРУНА БАНЯ»*\nhttps://vk.com/wall-169974497_8235')
        elif message == '8':
            result = greenAPI.sending.sendFileByUpload(sender,
                                                       'media/IMG_4664.MP4 ',
                                                       'IMG_4664.MP4', '*«БАЛАНС БАНЯ»*\nhttps://vk.com/wall-169974497_12815')

            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
    except Exception as e:
        mess.answer('Error')


@bot.router.message(text_message='Ж', state=Auth.CHELYABINSK_MISS.value)
def rout (mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Введите цифру программы*')
    mess.state_manager.set_state(sender, HowWas.STEP2.value)


@bot.router.message(state=HowWas.STEP2.value)
def rout (mess:Notification) -> None:
    sender = mess.sender
    print(mess.message_text)
    message = mess.message_text
    print(type(message))
    try:
        if message not in ["1","2","3","4","5","6","7","8"]:
            mess.answer('*Напиши цифру*')
            mess.state_manager.update_state(sender, HowWas.STEP2.value)
        elif message == '1':
            sender = mess.sender
            mess.answer(text_709)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '2':
            mess.answer(text_702)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '3':
            mess.answer(text_707)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '4':
            mess.answer(text_707)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '5':
            mess.answer(text_706)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '6':
            mess.answer(text_704)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '7':
            mess.answer(text_705)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '8':
            mess.answer(text_703)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
    except Exception as e:
        mess.answer('Error')


@bot.router.message(text_message='К', state=Auth.CHELYABINSK_MISS.value)
def how(mess:Notification) -> None:
    sender = mess.sender
    mess.answer('*Введите цифру программы*')
    mess.state_manager.update_state(sender, HowBass.How2.value)


@bot.router.message(state=HowBass.How2.value)
def how(mess: Notification) -> None:
    sender = mess.sender
    message = mess.message_text
    try:
        if message not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            mess.answer('*Напиши цифру*')
            mess.state_manager.update_state(sender, HowBass.How2.value)
        elif message == '1':
            mess.answer(text_600)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '2':
            mess.answer(text_600)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '3':
            mess.answer(text_600)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '4':
            mess.answer(text_600)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '5':
            mess.answer(text_600)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '6':
            mess.answer(text_600)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '7':
            mess.answer(text_600)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
        elif message == '8':
            mess.answer(text_600)
            mess.answer(text_101)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
    except Exception as e:
        mess.answer('Error')


@bot.router.message(text_message='Д', state=Auth.CHELYABINSK_MISS.value)
def certificate(mess: Notification) -> None:
    sender = mess.sender
    mess.answer(text_63)
    mess.answer(text_101)
    mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)


@bot.router.message(text_message='М', state=Auth.CHELYABINSK_MISS.value)
def f_consult(mess: Notification) -> None:
    sender = mess.sender
    mess.answer(text_1)
    mess.answer(text_30)
    mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)


@bot.router.message(text_message='В', state=Auth.CHELYABINSK_MISS.value)
def certificate(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.set_state(sender, Conversationmiss.USERNAME.value)
    mess.answer('*Как Вас звать-величать?*')


@bot.router.message(state=Conversationmiss.USERNAME.value)
def certificate_1(mess: Notification) -> None:
    sender = mess.sender
    user_name = str(mess.message_text)
    try:
        if not 2 <= len(user_name) <= 30:
            mess.answer('*Введите корректно Имя*')
            mess.state_manager.update_state(sender, Conversationmiss.USERNAME.value)
        else:
            mess.state_manager.update_state(sender, Conversationmiss.PEOPLE.value)
            mess.state_manager.update_state_data(sender, {"Имя": user_name})
            mess.answer('*Сколько человек планируется в гости на пар?*')
    except Exception as e:
        mess.answer('*Что-то пошло не так*')


@bot.router.message(state=Conversationmiss.PEOPLE.value)
def certificate_1(mess: Notification) -> None:
    sender = mess.sender
    people = str(mess.message_text)
    state = mess.state_manager.get_state_data(sender)
    user = state["Имя"]
    try:
        if not 1 <= len(people) <= 10:
            mess.answer('*Введите корректно сколько гостей*')
            mess.state_manager.set_state(sender, Conversationmiss.PEOPLE.value)
        else:
            mess.state_manager.update_state(sender, Conversationmiss.PROGRAM.value)
            mess.state_manager.update_state_data(sender, {"Люди": people})
            mess.answer('*Укажите какая программа приглянулась?*')
    except Exception as e:
        mess.answer('Ошибка!')


@bot.router.message(state=Conversationmiss.PROGRAM.value)
def certificate_1(mess: Notification) -> None:
    sender = mess.sender
    program = str(mess.message_text)
    state = mess.state_manager.get_state_data(sender)
    user = state["Имя"]
    people = state["Люди"]
    try:
        if not 1 <= len(program) <= 20:
            mess.answer('*Введите корректно программу*')
            mess.state_manager.set_state(sender, Conversationmiss.USERNAME.value)
        else:
            mess.state_manager.update_state(sender, Conversationmiss.CITY.value)
            mess.state_manager.update_state_data(sender, {"Программа": program})
            mess.answer('*В каком городе изволите попариться?*')
    except Exception as e:
        mess.answer('Ошибка!')


@bot.router.message(state=Conversationmiss.CITY.value)
def certificate_1(mess: Notification) -> None:
    sender = mess.sender
    city = str(mess.message_text)
    state = mess.state_manager.get_state_data(sender)
    user = state["Имя"]
    people = state["Люди"]
    program = state["Программа"]
    try:
        if not 1 <= len(city) <= 20:
            mess.answer('*Введите корректно Город*')
            mess.state_manager.set_state(sender, Conversationmiss.USERNAME.value)
        else:
            mess.state_manager.update_state(sender, Conversationmiss.DATE.value)
            mess.state_manager.update_state_data(sender, {"Город": city})
            mess.answer('*Подскажи желаемую дату банного отдыха?*')
    except Exception as e:
        mess.answer('Ошибка!')


@bot.router.message(state=Conversationmiss.DATE.value)
def certificate_3(mess: Notification) -> None:
    sender = mess.sender
    date = str(mess.message_text)
    data = mess.state_manager.get_state_data(sender)
    user_name = data["Имя"]
    city = data["Город"]
    people = data["Люди"]
    program = data["Программа"]
    consult = 'Консультация'
    try:
        if not 1 <= len(date) <= 15:
            mess.answer('*Введите корректно Дату*')
            mess.state_manager.update_state(sender, Conversationmiss.DATE.value)
        else:
            #print(post_lead(user_name, city, date, sender[0:11], consult, people, program))
            mess.state_manager.update_state_data(sender, {"Дата": date})
            mess.answer('*Я всё записал, отправил телеграмму хозяйке, вскоре с Вами свяжется- Анна Пихта.*')
            message = greenAPI.sending.sendMessage("79630906000@c.us", "Требуется разговор с Менеджером\n\n"
                    f'Имя: {user_name}.\n'
                    f'Город: {city}.\n'
                    f'Дата: {date}\n'
                    f'Номер: {sender[0:11]}\\n'
                    f'Люди: {people}\\n'
                    f'Программа: {program}'
                        )
            mess.answer(text_102)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
    except Exception as e:
        mess.answer("*Что-то пошло не так*")


@bot.router.message(state=Auth.CHELYABINSK_MISS.value, text_message='В')
def f_consult(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.set_state(sender, Soaring_Miss.STEP_1.value)
    mess.answer(text_90)
    mess.answer(text_101)
    mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)


@bot.router.message(state=Auth.CHELYABINSK_MISS.value, text_message=['Да','ДА','да','дА'])
def miss(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.set_state(sender, Bookingmiss.USERNAME.value)
    mess.answer('*Как Вас звать-величать?*')


@bot.router.message(state=Bookingmiss.USERNAME.value)
def rename_1(mess: Notification) -> None:
    sender = mess.sender
    user_name = str(mess.message_text)
    try:
        if not 2 <= len(user_name) <= 20:
            mess.answer('*Введите корректно Имя*')
            mess.state_manager.set_state(sender, Bookingmiss.USERNAME.value)
        else:
            state = mess.state_manager.update_state_data(sender, {"Имя": user_name})
            mess.state_manager.update_state(sender, Bookingmiss.PROGRAM.value)
            mess.answer('*Укажите какая программа приглянулась?*')
    except Exception as e:
        print(e)


@bot.router.message(state=Bookingmiss.PROGRAM.value)
def rename_2(mess: Notification) -> None:
    sender = mess.sender
    programm = str(mess.message_text)
    date = mess.state_manager.get_state_data(sender)
    user = date["Имя"]
    try:
        if not 1 <= len(programm) <= 40:
            mess.answer("*Введите корректно программу*")
            mess.state_manager.set_state(sender, Bookingmiss.PROGRAM.value)
        else:
            state = mess.state_manager.update_state_data(sender, {"Программа": programm})
            mess.state_manager.update_state(sender, Bookingmiss.PEOPLE.value)
            mess.answer('*Сколько человек планируется в гости на пар?*')
    except Exception as e:
        print(e)


@bot.router.message(state=Bookingmiss.PEOPLE.value)
def rename_3(mess: Notification) -> None:
    sender = mess.sender
    people = str(mess.message_text)
    date = mess.state_manager.get_state_data(sender)
    user = date["Имя"]
    program = date["Программа"]
    try:
        if not 1 <= len(people) <= 20:
            mess.answer("*Введите корректно сколько гостей*")
            mess.state_manager.set_state(sender, Bookingmiss.PEOPLE.value)
        else:
            state = mess.state_manager.update_state_data(sender, {"Люди": people})
            mess.state_manager.update_state(sender, Bookingmiss.CITY.value)
            mess.answer('*Русь большая,в каком городе будем париться?*')
    except Exception as e:
        pass


@bot.router.message(state=Bookingmiss.CITY.value)
def rename_4(mess: Notification) -> None:
    sender = mess.sender
    city = str(mess.message_text)
    date = mess.state_manager.get_state_data(sender)
    user = date["Имя"]
    program = date["Программа"]
    people = date["Люди"]
    try:
        if not 1 <= len(city) <= 20:
            mess.answer("*Введите корректно Город*")
            mess.state_manager.set_state(sender, Bookingmiss.CITY.value)
        else:
            state = mess.state_manager.update_state_data(sender, {"Город": city})
            mess.state_manager.update_state(sender, Bookingmiss.DATA.value)
            mess.answer('*Подскажи желаемую дату банного отдыха?*')
    except Exception as e:
        pass


@bot.router.message(state=Bookingmiss.DATA.value)
def rename_5(mess: Notification) -> None:
    sender = mess.sender
    date = str(mess.message_text)
    state = mess.state_manager.get_state_data(sender)
    name = state["Имя"]
    program = state["Программа"]
    people = state["Люди"]
    city = state["Город"]
    boking = 'Бронирование'
    try:
        if not 1 <= len(date) <= 15:
            mess.answer("*Введите корректно дату*")
            mess.state_manager.set_state(sender, Bookingmiss.DATA.value)
        else:
            print(post_lead(name, city, date, sender[0:11], boking, people, program))
            state = mess.state_manager.update_state_data(sender, {"Дата": date})
            message = greenAPI.sending.sendMessage("79630906000@c.us", "Бронирование\n\n"
                                                                       f'Имя: {name}.\n'
                                                                       f'Город: {city}.\n'
                                                                       f'Дата: {date}\n'
                                                                       f'Номер: {sender[0:11]}\n'
                                                                       f'Программа: {program}\n'
                                                                       f'Люди: {people}'
                                                                                               )
            mess.answer(text_112)
            mess.answer(text_103)
            mess.state_manager.delete_state(sender)
            mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
            pass
    except Exception as e:
        mess.answer('*Что-то пошло не так*')


@bot.router.message(text_message='А', state=Auth.CHELYABINSK_MISS.value)
def miss_handler(mess: Notification) -> None:
    sender = mess.sender
    mess.answer(text_500)
    mess.answer(text_101)
    mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)


@bot.router.message(text_message='П', state=Auth.CHELYABINSK_MISS.value)
def bay(mess:Notification) -> None:
    sender = mess.sender
    mess.answer(text_65)
    mess.state_manager.update_state(sender, Auth.STATE.value)
    mess.answer(text_70)


@bot.router.message(text_message='Б', state=Auth.CHELYABINSK_MISS.value)
def msk_handler_e(mess: Notification) -> None:
    sender = mess.sender
    mess.answer(text_100)
    mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)
    mess.answer(text_101)


@bot.router.message(regexp=r'[\W]*([тТ][еЕ][мМ][аА])[\W]*([бБ][аА][нН][яЯ][\W]*)', state=Auth.CHELYABINSK_MISS.value)
def message_yes(mess:Notification) -> None:
    sender = mess.sender
    mess.answer(text_1)
    mess.answer(text_30)
    mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)


@bot.router.message(type_message=filters.TEXT_TYPES, state=Auth.CHELYABINSK_MISS.value)
def an_message(mess: Notification) -> None:
    sender = mess.sender
    mess.answer("""
*Я не волшебник, я только учусь Вас понимать.*
*Напишите мне:*
*Тема Баня*
*И точно следуйте подсказкам.*""")
    mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)


@bot.router.message(text_message='Нет', state=None)
def message_no(mess: Notification) -> None:
    sender = mess.sender
    state = mess.state_manager.set_state(sender, Auth.STATE.value)
    mess.state_manager.set_state_data(sender, {"number": sender})
    data = mess.state_manager.get_state(sender)
    number = {'number': sender}
    mess.answer(text_13)


def run_forever_with_error_handler(bot : GreenAPIBot):
    time.sleep(5)
    try:
        bot.run_forever()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        run_forever_with_error_handler(bot)


run_forever_with_error_handler(bot)



