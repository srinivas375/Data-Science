from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
def list_items():
    return ["item1", "item2"]

@router.get("/{item_id}")
def get_item(item_id:int):
    return {"item_id": item_id, "name": f"Item {item_id}"}
