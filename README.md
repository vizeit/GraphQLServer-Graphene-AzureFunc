# GraphQL Server - Graphene - Azure Function
Boilerplate [Serverless](https://en.wikipedia.org/wiki/Serverless_computing) implementation of [GraphQL](https://graphql.org/) server in [Python](https://www.python.org/) using [Graphene](https://graphene-python.org/)

## Features
- Code-first approach
- Implemented in Python
- Serverless
- Hosting on Azure Cloud
- Modular
- Support for ASGI
- Lightweight
- Test-driven Development

## Quickstart
### Prerequisites
- Active [Azure cloud](https://azure.microsoft.com/en-us/) account
- Local development environment setup for [Azure functions using Python](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=azure-cli%2Cbash%2Cbrowser)

### Steps
1. Clone the repo,
```
git clone https://github.com/vizeit/GraphQLServer-Graphene-AzureFunc.git
``` 

2. Install graphene and starlette for graphene
```
pip install graphene starlette-graphene3
```

3. Go to [*\_\_init\_\_.py*](/GraphQLAPI/__init__.py)

4. Import *Schema* class from *Graphene* 
```
from graphene import Schema
```

5. Import *GraphQLApp* and *make_graphiql_handler* from *starlette_graphene3*
```
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
```

6. Import *AsgiMiddleware* class from *azure.functions* module
```
from azure.functions import AsgiMiddleware
```

7. Create *app* object from *GraphQLApp* class
```
app = GraphQLApp(schema, on_get=make_graphiql_handler())
```
If you prefer to turn off the Graph*i*QL playground, remove the second parameter to the *GraphQLApp* constructor
```
app = GraphQLApp(schema)
```

8. Return *AsgiMiddleware* object from the *main* function
```
return AsgiMiddleware(app).handle(req, context)
```

9. Define GraphQL types in [*Types.py*](/GraphQLAPI/Schemas/Types.py)

10. Write GraphQL query resolvers in [*Queries.py*](/GraphQLAPI/Schemas/Queries.py)

11. Add the unit tests under *tests* folder. Run the unit tests after any changes,
```
python -m unittest -v tests/*.py
```