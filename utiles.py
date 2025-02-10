import json
import os

def json_loader(route):
    json_list = []
    for root , _, files in os.walk(route):
        for filename in files:
            if filename.endswith('.json'):
                filepath = os.path.join(root,filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    json_list.append(json.load(file))
    return json_list       