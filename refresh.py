@bot.router.message(state=Bookingmsk.DATA.value)
def rename_2(mess: Notification) -> None:
    sender = mess.sender
    city = str(mess.message_text)
    state = mess.state_manager.get_state_data(sender)
    number = state ["Номер"]
    try:
        if not 5 <= len(city) <= 15:
            mess.answer("Введите корректно город!")
            mess.state_manager.set_state(sender,Bookingmsk.CITY.value)
        else:
            state = mess.state_manager.update_state_data(sender, {"Город": city})
            mess.state_manager.update_state(sender, Bookingmsk.PROGRAM.value)
            mess.answer('Ввидите программу!')
    except Exception as e:
        mess.answer('Все получиться!')

@bot.router.message(state=Bookingmsk.PROGRAM.value)
def rename_3(mess: Notification) -> None:
    sender = mess.sender
    programm = str(mess.message_text)
    city = mess.state_manager.get_state_data(sender)
    program = city["Город"]
    try:
        if not 5 <= len(programm) <= 20:
            mess.answer("Введите корректно программу!")
            mess.state_manager.set_state(sender, Bookingmsk.PROGRAM.value)
        else:
            state = mess.state_manager.update_state_data(sender, {"Программа": programm})
            mess.state_manager.update_state(sender, Bookingmsk.DATA.value)
            mess.answer('Введите дату!')
    except Exception as e:
        mess.answer('Все получиться!')


@bot.router.message(state=Bookingmsk.DATA.value)
def rename_4(mess: Notification) -> None:
    sender = mess.sender
    date = str(mess.message_text)
    programm = mess.state_manager.get_state_data(sender)
    data = programm["Программа"]
    try:
        if not 5 <= len(data) <= 10:
            mess.answer('Введите корректно дату!')
            mess.state_manager.set_state(sender, Bookingmsk.DATA.value)
        else:
            state = mess.state_manager.update_state_data(sender, {"Дата": date})
            mess.state_manager.update_state(sender, Bookingmsk.TIME.value)
            mess.answer('Ввидите время!')
    except Exception as e:
        mess.answer("Все получиться!")


@bot.router.message(state=Bookingmsk.TIME.value)
def rename_5(mess: Notification) -> None:
    sender = mess.sender
    time = mess.message_text
    data = mess.state_manager.get_state_data(sender)
    timee = data["Дата"]
    try:
        if not 5 <= len(time) <= 10:
            mess.answer("Введите корректно дату!")
            mess.state_manager.set_state(sender, Bookingmsk.TIME.value)
        else:
            state = mess.state_manager.update_state_data(sender, {"Время": time})
            mess.state_manager.update_state(sender, Bookingmsk.QUANTI.value)
            mess.answer('Ввидите колличество человек!')
    except Exception as e:
        mess.answer("Все получиться!")


@bot.router.message(state=Bookingmsk.QUANTI.value)
def rename_6(mess: Notification) -> None:
    sender = mess.sender
    quantity = str(mess.message_text)
    date = mess.state_manager.get_state_data(sender)
    time = date["Время"]
    try:
        if not 5 <= len(quantity) <= 10:
            mess.answer("Введите корректно колличество человек!")
            mess.state_manager.set_state(sender, Bookingmsk.QUANTI.value)
        else:
            state = mess.state_manager.update_state_data(sender, {"Колличество людей": quantity})
            mess.state_manager.update_state(sender, Bookingmsk.CHILD.value)
            mess.answer('Будут ли дети?')
    except Exception as e:
        mess.answer("Получилось")


@bot.router.message(state=Bookingmsk.CHILD.value)
def rename_7(mess: Notification) -> None:
    sender = mess.sender
    children = str(mess.message_text)
    quantitu = mess.state_manager.get_state_data(sender)
    name = quantitu["ФИО"]
    number = quantitu["Номер"]
    city = quantitu["Город"]
    programm = quantitu["Программа"]
    date = quantitu["Дата"]
    time = quantitu["Время"]
    childr = quantitu["Колличество людей"]
    try:
        if not 2 <= len(children) <= 10:
            mess.answer('Введите корректно!')
        else:
            state = mess.state_manager.update_state_data(sender, {"Дети": children})
            print(post_lead(name, number, city, programm, date, time, childr, children))
            mess.answer('Ваши данны:\n'
                        f'ФИО: {name}\n'
                        f'Номер: {number}\n'
                        f'Город: {city}\n'
                        f'Программа: {programm}\n'
                        f'Дата: {date}\n'
                        f'Время: {time}\n'
                        f'Колличество людей: {childr}\n'
                        f'Дети: {children}'
                                            )
            mess.answer(""" У вас все получилось, я отправил весточку хозяевам, Анна Пихта, свяжется
с вами в рабочее время. Ежели у вас горит, позвоните сами
по номеру +7-963-090-6000""")
            mess.state_manager.delete_state(sender)
    except Exception as e:
        mess.answer('Успешно!')




















@bot.router.message(state=Bookingmiss.USERNAME.value)
def miss_1(mess: Notification) -> None:
    sender = mess.sender
    user_name = mess.message_text
    state = mess.state_manager.update_state_data(sender, {"ФИО": user_name})
    mess.state_manager.update_state(sender, Bookingmiss.NUMBER.value)
    mess.answer('Ввидите ваш номер!')


@bot.router.message(state=Bookingmiss.NUMBER.value)
def miss_2(mess: Notification) -> None:
    sender = mess.sender
    number = mess.message_text
    state = mess.state_manager.update_state_data(sender, {"Номер": number})
    mess.state_manager.update_state(sender, Bookingmiss.CITY.value)
    mess.answer('Ввидите город!')


@bot.router.message(state=Bookingmiss.CITY.value)
def miss_3(mess: Notification) -> None:
    sender = mess.sender
    city = mess.message_text
    state = mess.state_manager.get_state_data(sender)
    number = state ["Номер"]
    state = mess.state_manager.update_state_data(sender, {"Город": city})
    mess.state_manager.update_state(sender, Bookingmiss.PROGRAM.value)
    mess.answer('Ввидите программу!')


@bot.router.message(state=Bookingmiss.PROGRAM.value)
def miss_4(mess: Notification) -> None:
    sender = mess.sender
    programm = mess.message_text
    city = mess.state_manager.get_state_data(sender)
    program = city["Город"]
    state = mess.state_manager.update_state_data(sender, {"Программа": programm})
    mess.state_manager.update_state(sender, Bookingmiss.DATA.value)
    mess.answer('Введите дату!')


@bot.router.message(state=Bookingmiss.DATA.value)
def miss_5(mess: Notification) -> None:
    sender = mess.sender
    date = mess.message_text
    programm = mess.state_manager.get_state_data(sender)
    data = programm["Программа"]
    state = mess.state_manager.update_state_data(sender, {"Дата": date})
    mess.state_manager.update_state(sender, Bookingmiss.TIME.value)
    mess.answer('Ввидите время!')


@bot.router.message(state=Bookingmiss.TIME.value)
def miss_6(mess: Notification) -> None:
    sender = mess.sender
    time = mess.message_text
    data = mess.state_manager.get_state_data(sender)
    timee = data["Дата"]
    state = mess.state_manager.update_state_data(sender, {"Время": time})
    mess.state_manager.update_state(sender, Bookingmiss.QUANTI.value)
    mess.answer('Ввидите колличество человек!')


@bot.router.message(state=Bookingmiss.QUANTI.value)
def miss_7(mess: Notification) -> None:
    sender = mess.sender
    quantity = mess.message_text
    date = mess.state_manager.get_state_data(sender)
    time = date["Время"]
    state = mess.state_manager.update_state_data(sender, {"Колличество людей": quantity})
    mess.state_manager.update_state(sender, Bookingmiss.CHILD.value)
    mess.answer('Будут ли дети?')


@bot.router.message(state=Bookingmiss.CHILD.value)
def miss_8(mess: Notification) -> None:
    sender = mess.sender
    children = mess.message_text
    quantitu = mess.state_manager.get_state_data(sender)
    name = quantitu ["ФИО"]
    number = quantitu["Номер"]
    city = quantitu ["Город"]
    programm = quantitu ["Программа"]
    date = quantitu ["Дата"]
    time = quantitu ["Время"]
    childr = quantitu["Колличество людей"]
    state = mess.state_manager.update_state_data(sender, {"Дети": children})
    post_lead(name, number, city, programm, date, time, childr, children)
    mess.answer('Ваши данны:\n'
                f'ФИО: {name}\n'
                f'Номер: {number}\n'
                f'Город: {city}\n'
                f'Программа: {programm}\n'
                f'Дата: {date}\n'
                f'Время: {time}\n'
                f'Колличество людей: {childr}\n'
                f'Дети: {children}'
                )

    mess.answer('*Вы успешно осуществили бронь,в билжайшее время с вами свяжеться менеджер!*')
    mess.answer('*Вернуться к прайлисту напишите - 1*')

    #mess.state_manager.delete_state(sender)








@bot.router.message(text_message='А', state=Auth.CHELYABINSK_MISS.value)
def certificate(mess: Notification) -> None:
    sender = mess.sender
    mess.state_manager.set_state(sender, Conversation.USERNAME.value)
    mess.answer('Введите свое имя!')


@bot.router.message(state=Conversation.USERNAME.value)
def certificate_1(mess: Notification) -> None:
    sender = mess.sender
    user_name = mess.message_text
    mess.state_manager.update_state(sender, Conversation.CITY.value)
    mess.state_manager.set_state_data(sender, {"Имя": user_name})
    mess.answer('Введите свой номер телефона!')


@bot.router.message(state=Conversation.CITY.value)
def certificate_2(mess: Notification) -> None:
    sender = mess.sender
    number = mess.message_text
    data = mess.state_manager.get_state_data(sender)
    user_name = data["Имя"]
    mess.answer('Уведомили сотрудника,в ближайшее время с вами свяжеться мененджер,для приобретения сертификата!')
    message = greenAPI.sending.sendMessage("79610344938@c.us", "Хочет приобрести сертификат!\n\n"
            f"Имя: {user_name}.\n"
            f"Номер: {number}.")

    mess.answer(text_41)
    mess.answer('*Вернуться к Прайсу Напишите -2*')

    mess.state_manager.update_state(sender, Auth.CHELYABINSK_MISS.value)







@bot.router.message(state=Bookingmsk.DATA.value)
def rename_2(mess: Notification) -> None:
    sender = mess.sender
    date = str(mess.message_text)
    state = mess.state_manager.get_state_data(sender)
    name = state["Имя"]
    city = state["Город"]

    try:
        if not 3 <= len(date) <= 15:
            mess.answer("Введите корректно дату!")
            mess.state_manager.set_state(sender, Bookingmsk.DATA.value)
        else:
            state = mess.state_manager.update_state_data(sender, {"Дата": date})
            mess.answer('Ваши данны:\n'
                        f'Величать: {name}\n'
                        f'Город: {city}\n'
                        f'Дата: {date}\n'
                        )
            mess.answer(""" У вас все получилось, я отправил весточку хозяевам, Анна Пихта, свяжется
            с вами в рабочее время. Ежели у вас горит, позвоните сами
            по номеру +7-963-090-6000""")
            mess.answer('*ВЕРНУТЬСЯ К ПРАЙСУ НАПИШИТЕ - 1*')
            mess.state_manager.delete_state(sender)
            mess.state_manager.update_state(sender, Auth.STATE.value)
    except Exception as e:
        mess.answer('Отлично')






        if not 3 <= len(date) <= 15:
            mess.answer("Введите корректно дату!")
            mess.state_manager.set_state(sender, Bookingmsk.DATA.value)