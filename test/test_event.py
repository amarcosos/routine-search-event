import unittest
import json

from server import server
from models import User
from repositories import UserRepository


class TestEvent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def test_get(self):
        UserRepository.create(id='curso-departamento-pessoal---presencial-manha__534240')
        response = self.client.get('/application/event/curso-departamento-pessoal---presencial-manha__534240')

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(
            response_json,
            {'event': {'id': 'curso-departamento-pessoal---presencial-manha__534240'}}
        )
