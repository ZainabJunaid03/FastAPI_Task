import json
from fastapi import APIRouter
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent / "template.json"

template_router = APIRouter()

@template_router.get("/get")
def get_template():
    with open(TEMPLATE_PATH, "r") as file:
        template = json.load(file)
    return template

@template_router.post("/fill")
def fill_template(data: dict):
    with open(TEMPLATE_PATH, "r") as file:
        template = json.load(file)
    template.update(data)
    return {"message": "Template updated successfully", "updated_template": template}
