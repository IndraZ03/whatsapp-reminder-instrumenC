from whatsapp_api_client_python import API
import requests
from datetime import datetime
import json

ID_INSTANCE = '1101806751'
API_TOKEN_INSTANCE = '63015a43115a4ed58f340756ac948c105b2a4cf63f664db08c'


greenAPI = API.GreenApi(ID_INSTANCE, API_TOKEN_INSTANCE)


def main():
    greenAPI.webhooks.startReceivingNotifications(onEvent)


def onEvent(typeWebhook, body):
    if typeWebhook == 'incomingMessageReceived':
        onIncomingMessageReceived(body)
    else:
        pass


def onIncomingMessageReceived(body):
    waktu = datetime.fromtimestamp(body['timestamp'])
    messageData = body['messageData']
    tugas = messageData['textMessageData']['textMessage']

    result = greenAPI.sending.sendMessage(
        '120363103102610040@g.us', waktu)


if __name__ == "__main__":
    main()
