import json
USER= PASS= HOST= DATABASE= ''

def init():
    global USER, PASS, HOST, DATABASE
    # read file
    data = None
    with open('settings.json', 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    USER = obj['db']['user']
    HOST = obj['db']['host']
    PASS = obj['db']['pass']
    DATABASE = obj['db']['database']
