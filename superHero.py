import json
from pprint import pprint


str = """{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    },
    {
      "name": "Spider man",
      "age": 17,
      "secretIdentity": "Peter Parker",
      "powers": [
        "Jumps",
        "Net",
        "Spider flair"
      ]
    },
    {
      "name": "Iron man",
      "age": 50,
      "secretIdentity": "Tony Stark",
      "powers": [
        "Money"
      ]
    }
  ]
}"""


data = json.loads(str)
list = []
for item in data['members']:
    list.append(item['age'])
print(sorted(list))