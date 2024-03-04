@bot.router.message(text_message='1', state=Auth.MOSCOW.value)
def msk_handler_a(mess: Notification) -> None:
    sender = mess.sender
    # mess.state_manager.set_state(sender, How_Was_It_Msk.STEP1.value)
    # mess.state_manager.update_state(sender, Auth.MOSCOW.value,)
    mess.answer(text_22)
    mess.answer(text_31)
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)


@bot.router.message(text_message='2', state=Auth.MOSCOW.value)
def msk_handler_b(mess: Notification) -> None:
    sender = mess.sender
    text = mess.message_text
    # mess.state_manager.set_state(sender,How_Was_It_Msk.STEP2.value)
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    mess.answer(text_23)
    mess.answer(text_31)


@bot.router.message(text_message='Г', state=How_Was_It_Msk.STEP2.value)
def msk_handler_b(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    result = greenAPI.sending.sendFileByUpload(sender,
                                               'D:\BotWA\IMG_3812.MP4',
                                               'IMG_3812.MP4', 'Тест')

    mess.answer('*Вернуться к Прайсу Напишеть - 1*')
    mess.state_manager.delete_state(sender)
    mess.state_manager.update_state(sender, Auth.STATE.value)


@bot.router.message(text_message='3', state=Auth.MOSCOW.value)
def msk_handler_v(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    mess.answer(text_24)
    mess.answer(text_31)


@bot.router.message(text_message='4', state=Auth.MOSCOW.value)
def msk_handler_g(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    mess.answer(text_25)
    mess.answer(text_31)


@bot.router.message(text_message='5', state=Auth.MOSCOW.value)
def msk_handler_d(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    mess.answer(text_26)
    mess.answer(text_31)


@bot.router.message(text_message='6', state=Auth.MOSCOW.value)
def msk_handler_e(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    mess.answer(text_27)
    mess.answer(text_31)

    result = greenAPI.sending.sendFileByUpload(sender,
                                               'D:\BotWA\IMG_3812.MP4',
                                               'IMG_3812.MP4', 'Тест')




@bot.router.message(text_message='Г', state=How_Was_It_Msk.STEP2.value)
def msk_handler_b(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.update_state(sender, Auth.MOSCOW.value)
    result = greenAPI.sending.sendFileByUpload(sender,
                                               'D:\BotWA\IMG_3812.MP4',
                                               'IMG_3812.MP4', 'Тест')

    mess.answer('*Вернуться к Прайсу Напишеть - 1*')
    mess.state_manager.delete_state(sender)
    mess.state_manager.update_state(sender, Auth.STATE.value)