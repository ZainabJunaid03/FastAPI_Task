import json

def get_template():
    with open("template.json", "r") as file:
        return json.load(file)

def fill_template(data: dict):
    template = get_template()
    return {"message": "Template filled", "data": data}