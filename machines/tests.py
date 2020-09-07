from django.test import TestCase

from machines.models import Machine


class MachineTestCase(TestCase):

    def setUp(self):
        Machine.objects.create(name="localhost", ip="127.0.0.1")
        Machine.objects.create(name="not-exist", ip="200.0.0.1")

    def test_machine_can_ping(self):
        exists = Machine.objects.get(name="localhost")
        not_exists = Machine.objects.get(name="not-exist")

        self.assertEqual(exists.ping(), True)
        self.assertEqual(not_exists.ping(), False)