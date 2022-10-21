import json


def search_dictionary(word, dictionary):
    list = []

    for value in dictionary:
        for value2 in value["transcript"]:
            if value2["text"].count(word):
                print(f"[{len(list)}]text = \"{value2['text']}\", start = {value2['start']}, url = {value2['url']}")
                list.append(f"text = \"{value2['text']}\", start = {value2['start']}, url = {value2['url']}\n")

    return list[int(input("\nchose_option: "))]


data = {}

with open('transcripts.json', 'r', encoding='cp850') as jsonFile:
    data = json.load(jsonFile)

    #print(data)

with open('output.txt', 'a') as file:
    try:
        while True:
            file.write(search_dictionary(input("\ninput text: "), data))

    finally:
        file.close()