import unittest2

from chef import Client
from chef.tests import ChefTestCase

class ClientTestCase(ChefTestCase):
    def test_list(self):
        self.assertIn('test_1', Client.list(self.api))

    def test_get(self):
        client = Client('test_1', self.api)
        self.assertTrue(client.platform)
        self.assertEqual(client.orgname, 'pycheftest')
        self.assertTrue(client.public_key)
        self.assertTrue(client.certificate)
        self.assertEqual(client.private_key, None)

    def test_create(self):
        name = self.random()
        client = Client.create(name, self.api)
        self.register(client)
        self.assertEqual(client.name, name)
        #self.assertEqual(client.orgname, 'pycheftest') # See CHEF-2019
        self.assertTrue(client.private_key)
        self.assertTrue(client.public_key)
        self.assertIn(name, Client.list(self.api))

        client2 = Client(name, self.api)
        client2.rekey()
        self.assertEqual(client.public_key, client2.public_key)
        self.assertNotEqual(client.private_key, client2.private_key)

    def test_delete(self):
        name = self.random()
        client = Client.create(name, self.api)
        client.delete()
        self.assertNotIn(name, Client.list(self.api))
