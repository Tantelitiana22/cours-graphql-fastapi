import graphene
from app.api import models
from app.api import product_dto
from graphene_pydantic import PydanticObjectType, PydanticInputObjectType


class Product(PydanticObjectType):
    class Meta:
        model = models.ProductModelShow


class Query(graphene.ObjectType):
    products = graphene.List(Product)
    product = graphene.Field(Product, id=graphene.String(required=True))

    @staticmethod
    def resolve_products(parent, info):
        return product_dto.get_products()

    @staticmethod
    def resolve_product(parent, info, id):
        return product_dto.get_product(id)


## Mutation: (update, create)
class ProductInput(PydanticInputObjectType):
    class Meta:
        model = models.ProductModel


class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.String()

    ok = graphene.Boolean()
    result = graphene.Field(Product)

    @staticmethod
    def mutate(parent, info, id):
        result = product_dto.delete_product(id)
        ok = True if result else False
        return DeleteProduct(ok=ok, result=result)


class CreateProduct(graphene.Mutation):
    class Arguments:
        product = ProductInput()

    @staticmethod
    async def mutate(parent, info, product):
        product_to_create = models.ProductModel(**product)
        return await product_dto.add_product(product_to_create)

    Output = Product


class ProductForUpdateInput(PydanticInputObjectType):
    class Meta:
        model = models.ProductModelOptional


class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.String()
        product = ProductForUpdateInput()

    ok = graphene.Boolean()
    result = graphene.Field(Product)

    @staticmethod
    def mutate(parent, info, id, product):
        print("Where is the problem?")
        result = product_dto.put_product(id, models.ProductModelOptional(**product))
        ok = True if result else False
        return UpdateProduct(ok=ok, result=result)


class Mutations(graphene.ObjectType):
    createProduct = CreateProduct.Field()
    deleteProduct = DeleteProduct.Field()
    updateProduct = UpdateProduct.Field()
