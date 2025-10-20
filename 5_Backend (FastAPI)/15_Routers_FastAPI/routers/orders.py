from fastapi import APIRouter

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("/")
def list_users():
    return ["order1", "order2"]

@router.get("/{order_id}")
def get_user(order_id: int):
    return {"order_id": order_id, "name": f"Order {order_id}"}