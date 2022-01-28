import azure.functions as func
from azure.functions import AsgiMiddleware

from graphene import ObjectType, String, Schema
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

class Query(ObjectType):
    
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'

schema = Schema(query=Query)
#app = GraphQLApp(schema, on_get=make_graphiql_handler())
app = GraphQLApp(schema)

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return AsgiMiddleware(app).handle(req, context)
