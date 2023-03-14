from fastapi import APIRouter

# create router
router = APIRouter()


@router.get("/producers/{id}")
async def get_all_producers(id):
    return [
        {"id": 1, "name": "Producer 1"},
        {"id": 2, "name": "Producer 2"},
    ]
