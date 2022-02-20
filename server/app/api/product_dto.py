import json
from typing import List
from fastapi import HTTPException
from app.api import models, db
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


async def add_product(product: models.ProductModel) -> models.ProductModel:
    try:
        result = db.Product(**product.dict()).save()
        return models.ProductModel(
            **json.loads(json.dumps(result.to_mongo(), cls=JSONEncoder))
        )

    except Exception as message:
        raise HTTPException(
            status_code=400,
            detail=f"échec de creation ! données invalides !!!: {message}:\n {product.__dict__}",
        )


async def get_products() -> List[models.ProductModel]:
    result = [
        models.ProductModelShow(
            **json.loads(json.dumps(obj.to_mongo(), cls=JSONEncoder))
        )
        for obj in db.Product.objects.all()
    ]
    return result


async def get_product(id: str) -> models.ProductModel:
    result = db.Product.objects.get(id=id)
    return models.ProductModel(
        **json.loads(json.dumps(result.to_mongo(), cls=JSONEncoder))
    )


async def delete_product(id: str) -> models.ProductModel:
    result = db.Product.objects.get(id=id)
    print(result)
    response = json.loads(json.dumps(result.to_mongo(), cls=JSONEncoder))
    result.delete()
    return models.ProductModel(**response)


async def put_product(id: str, request: models.ProductModelOptional):
    result = db.Product.objects.get(id=id)
    if request.id_type:
        result.id_type = request.id_type
    if request.name:
        result.name = request.name
    if request.category:
        result.category = request.category
    if request.filter:
        result.filter = request.filter
    if request.price:
        result.price = request.price
    print(result.to_mongo())
    result.save()
    return models.ProductModel(
        **json.loads(json.dumps(result.to_mongo(), cls=JSONEncoder))
    )
