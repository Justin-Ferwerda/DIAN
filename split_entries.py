"""script to split devotions and turn each into fixture for django"""

import re
import json

with open('devotions', 'r', encoding="utf8") as file:
    content = file.read()
    entries = re.split(r'\n(?=\d{1,2}/\d{1,2}/\d{4})', content)
    for i, entry in enumerate(entries):
        to_json = entry.split('\n\n', 1)
        date_and_verse = to_json[0].split('\n', 1)
        date = date_and_verse[0]
        verse = date_and_verse[1]
        fix = {
          "model": "DIANapi.devotion",
          "pk": i + 1,
          "fields": {
            "date": date,
            "verse": verse,
            "content": to_json[1],
          }
        }

        json_devotion = json.dumps(fix, indent=4)
        with open('devotions_fixture.json', 'a', encoding="utf8") as file:
            file.write(',')
            file.write('\n')
            file.write(json_devotion)
