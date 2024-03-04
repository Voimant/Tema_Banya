import requests


class Wasender():
    """
    :param idInstance - инстанст гринапи
    :param apiTokenInstance - токен гринапи
    """
    def __init__(self, idInstance, apiTokenInstance):
        self.idInstance = idInstance
        self.apiTokenInstance = apiTokenInstance

    def send_message(self, chat_id, text):
        """
        Метод отправки сообщений без картинки
        :param chat_id - Номер телефона абонента пример 79610344938@c.us
        :param text - текст рассылаемого сообщения"""
        url = f"https://api.green-api.com/waInstance{self.idInstance}/sendMessage/{self.apiTokenInstance}"

        payload = "\r\n\t\"chatId\": \"{ch}\",\r\n\t\"message\": \"{text}\"\r\n".format(ch=chat_id, text=text)
        payload2 = "{" + payload + "}"
        payload3 = payload2.encode('utf-8')
        headers = {
            'Content-Type': 'application/json'
        }
        # print(payload)
        #print(payload2)
        response = requests.request("POST", url, headers=headers, data=payload3)

        print(response.json())

    def send_photo_message(self, chat_id, file_path, caption):
        """
        Метод отпраки сообщений с картинкой
        :param chat_id - номер телефона абонента пример 79610344938@c.us
        :param file_path - абсолютный путь до файла
        :param caption - текст к картинке
        можно отсылать в формате jpg"""
        url = f"https://api.green-api.com/waInstance{self.idInstance}/sendFileByUpload/{self.apiTokenInstance}"
        payload = {'chatId': chat_id,
                   'caption': caption}
        files = [
            ('file',  (file_path, open(file_path, 'rb'), 'image/jpeg'))
        ]
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        print(response.text.encode('utf8'))

