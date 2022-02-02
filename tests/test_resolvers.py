from unittest import IsolatedAsyncioTestCase
from graphene import Schema
import sys
sys.path.append('.')
from GraphQLAPI.Schemas.Queries import Query

class test_resolvers(IsolatedAsyncioTestCase):
    def setUp(self):
        self.schema = Schema(query=Query)
    
    async def test_hello(self):
        result = await self.schema.execute_async('{hello}')
        self.assertEqual(result.data['hello'], 'Hello stranger!')
    
    async def test_goodbye(self):
        result = await self.schema.execute_async('{goodbye}')
        self.assertEqual(result.data['goodbye'], 'See ya!')