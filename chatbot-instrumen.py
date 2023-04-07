from whatsapp_api_client_python import API
import requests
import datetime
import fungsi as fs
import json
import time
import threading


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
    messageData = body['messageData']
    tugas = messageData["textMessageData"]['textMessage']
    if tugas == "!intro":
        result = greenAPI.sending.sendMessage(
            '120363107764474123@g.us', '''Halo! saya adalah bot untuk mengingatkan tugas. hehe 
            \nUntuk memberikan instruksi pengingat silakan kirim pesan ke grup ini dengan format : 
            \nmatkul!jenis tugas!deadline tugas(format : HH-BB-TTTT JJ:MM )!link pengumpulan!waktu pengingat yang diinginkan (format : HH-BB-TTTT JJ:MM )
            \ncontoh : Mikroprosesor dan Sistem Antarmuka!Melakukan simulasi wokwi!01-04-2023(ini spasi)23:59!http://gugel.drive.com!01-04-2023(ini spasi)15:00
            \n\n*Note : harus diberi pemisah ! sesuai dengan contoh jika tidak akan menimbulkan kesalahan sistem.*
            \nInstruksi pengingat akan berhasil ketika ada balasan dari saya
            \nSekian dan Terima kasih!''')
    else:
        # matkul!tugas!deadline!linkpengumpulan!waktureminder
        tugas = messageData["textMessageData"]['textMessage']
        tambah = fs.tambah_data(tugas)
        result = greenAPI.sending.sendMessage(
            '120363107764474123@g.us', f"pengingat matkul {tambah['matkul']} yang dipasang pengingat pada {tambah['reminder']}berhasil ditambahkan!")


def reminder():
    while True:
        data = fs.loadJson()
        waktu = datetime.datetime.now()
        waktu_n = waktu.strftime("%d-%m-%Y %H:%M")
        for item in data:
            if item['reminder'] == waktu_n:
                matkul = item['matkul']
                tugas = item['tugas']
                link = item['link']

                reminder = f'''Diingatkan kembali untuk segera mengirimkan tugas :\nMata kuliah : {matkul}\ntugas : {tugas}\nlink pengumpulan : {link}\nyang harus sudah dikumpulkan pada : {item['deadline']}\nterimakasih!'''
                result = greenAPI.sending.sendMessage(
                    '120363107764474123@g.us', reminder)
                time.sleep(120)


if __name__ == "__main__":
    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=reminder)
    t1.start()
    t2.start()
