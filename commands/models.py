import paramiko
from django.db import models

from machines.models import Machine


class Command(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    sudo = models.BooleanField(default=False)
    command = models.TextField(null=True)
    action = models.TextField(null=True)
    status = models.BooleanField(default=False)

    def run_command(self):
        if not self.check_machine():
            self.status = False
            return self.status

    def init_ssh_conn(self):
        ssh_client = paramiko.SSHClient()

        if not self.machine.ssh_pub:
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh_client.

    def check_machine(self):
        return self.machine.status
