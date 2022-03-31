import json

with open("output.json") as jsonFile:
    data = json.load(jsonFile)
    jsonData = data["track"]
    coverart_image_link = jsonData["images"]["coverart"]
    backround_image_link = jsonData["images"]["background"]
    print(jsonData.get("title"))
    print(jsonData.get("subtitle"))
    print(coverart_image_link)
    print(backround_image_link)