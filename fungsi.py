import json


def loadJson():
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
        return data


def simpanJson(data):
    with open('data.json', "w") as json_file:
        json.dump(data, json_file)

# tambah data


def tambah_data(tugas):
    task = tugas.split('!')
    try:
        value = task[1]  # mencoba mengambil elemen pada indeks ke-1
    except IndexError:
        pass  # jika terjadi index out of range, maka lewati saja
    else:
        matkul = task[0]
        tugas = task[1]
        deadline = task[2]
        link = task[3]
        reminder = task[4]

    # simpan dalam bentuk json
    data_masuk = {
        "matkul": matkul,
        "tugas": tugas,
        "deadline": deadline,
        "link": link,
        "reminder": reminder
    }
    data = loadJson()
    data.append(data_masuk)
    simpanJson(data)
    return data_masuk
