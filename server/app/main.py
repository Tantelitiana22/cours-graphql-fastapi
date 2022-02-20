import graphene
from fastapi import FastAPI
from app.api import schema, close_connection, create_connection
from starlette_graphene3 import GraphQLApp, make_graphiql_handler


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Contact Applications!"}


@app.on_event("startup")
def startup():
    create_connection()


@app.on_event("shutdown")
def shutdown():
    close_connection()


schemaGrapql = graphene.Schema(query=schema.Query, mutation=schema.Mutations)
graphql_app = GraphQLApp(schema=schemaGrapql, on_get=make_graphiql_handler())

app.add_route("/graphql", graphql_app)
