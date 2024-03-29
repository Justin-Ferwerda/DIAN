"""script to split devotions and turn each into fixture for django"""

import re
import json
from datetime import datetime

with open('devotions', 'r', encoding="utf8") as file:
    content = file.read()
    entries = re.split(r'\n(?=\d{1,2}/\d{1,2}/\d{4})', content)
    for i, entry in enumerate(entries):
        to_json = entry.split('\n\n', 1)
        date_and_verse = to_json[0].split('\n', 1)
        date = date_and_verse[0]
        input_format = "%m/%d/%Y"
        output_format = "%Y-%m-%d"
        parsed_date = datetime.strptime(date, input_format)
        formatted_date = parsed_date.strftime(output_format)
        verse = date_and_verse[1]
        verse_split = verse.split(':', 1)
        formatted_verse = verse_split[1].replace('"', '').replace('\n', '')
        content = to_json[1].replace('\n', '')

        fix = {
          "model": "DIANapi.devotion",
          "pk": i + 1,
          "fields": {
            "date": formatted_date,
            "verse": formatted_verse,
            "content": content,
          }
        }

        json_devotion = json.dumps(fix, indent=4)
        with open('devotions_fixture.json', 'a', encoding="utf8") as file:
            file.write(',')
            file.write('\n')
            file.write(json_devotion)
