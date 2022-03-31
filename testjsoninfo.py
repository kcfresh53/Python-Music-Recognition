import json

with open("output.json") as jsonFile:
    data = json.load(jsonFile)
    jsonData = data["track"]
    coverart_image_link = jsonData["coverart"]
    backround_image_link = jsonData["background"]
    print(jsonData.get("title"))