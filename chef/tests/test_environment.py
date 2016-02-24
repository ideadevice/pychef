from chef import Environment
from chef.exceptions import ChefAPIVersionError
from chef.tests import ChefTestCase, test_chef_api

class EnvironmentTestCase(ChefTestCase):
    def test_version_error_list(self):
        with test_chef_api(version='0.9.0') as capi:
            with self.assertRaises(ChefAPIVersionError):
                Environment.list(capi)

    def test_version_error_create(self):
        with test_chef_api(version='0.9.0') as capi:
            with self.assertRaises(ChefAPIVersionError):
                Environment.create(self.random(), capi)

    def test_version_error_init(self):
        with test_chef_api(version='0.9.0') as capi:
            with self.assertRaises(ChefAPIVersionError):
                Environment(self.random(), capi)
