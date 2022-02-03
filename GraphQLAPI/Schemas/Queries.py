from graphene import ObjectType, String

class Query(ObjectType):
    
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    async def resolve_hello(root, info, name):
        return f'Hello {name}!'

    async def resolve_goodbye(root, info):
        return 'See ya!'