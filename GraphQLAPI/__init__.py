import azure.functions as func
from azure.functions import AsgiMiddleware

from graphene import Schema
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from .Schemas.Queries import Query

schema = Schema(query=Query)
app = GraphQLApp(schema, on_get=make_graphiql_handler())

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return AsgiMiddleware(app).handle(req, context)
