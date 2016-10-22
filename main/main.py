import errno
#import io
import json
import os
#import system
from googlefinance import getQuotes

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def get_quotes():
    json_quote = json.dumps(getQuotes('XXII'), indent=2)
    return json_quote

def write_json_to_file(json_quote):
    with open('./exported_json/exported_json.json', 'w') as outfile:
        json.dump(json_quote, outfile)

path = "./exported_json"
json_quote = get_quotes()
make_sure_path_exists(path)
write_json_to_file(json_quote)
