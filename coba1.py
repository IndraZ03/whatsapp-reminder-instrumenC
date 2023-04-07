from whatsapp_api_client_python import API
import requests
from datetime import datetime
import json

ID_INSTANCE = '1101806751'
API_TOKEN_INSTANCE = '63015a43115a4ed58f340756ac948c105b2a4cf63f664db08c'

greenAPI = API.GreenApi(ID_INSTANCE, API_TOKEN_INSTANCE)


def main():
    chatIds = [
        "6289666444301@c.us"
    ]

    resultCreate = greenAPI.groups.createGroup('Reminder Tugas Instrumentasi C',
                                               chatIds)

    if resultCreate.code == 200:
        print(resultCreate.data)
        resultSend = greenAPI.sending.sendMessage(resultCreate.data['chatId'],
                                                  'Percobaan')
        if resultSend.code == 200:
            print(resultSend.data)
        else:
            print(resultSend.error)
    else:
        print(resultCreate.error)


if __name__ == "__main__":
    main()
