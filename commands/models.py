import paramiko
from django.db import models

from machines.models import Machine


class Command(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name="command")
    sudo = models.BooleanField(default=False)
    command = models.TextField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)
    output = models.TextField(default="", blank=True, null=True)

    def run_command(self):
        if not self.check_machine():
            self.status = False
            return self.status

        ssh_client = self.init_ssh_conn()
        _, stdout, stderr = ssh_client.exec_command(self.command)
        self.output = "".join(stdout.readlines()) if stdout else "".join(stderr.readlines())

        _, stdout, _ = ssh_client.exec_command("echo $?")
        self.status = self.check_status(stdout.readlines())
        self.save()

    def init_ssh_conn(self):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(
            self.machine.ip,
            username=self.machine.user,
            password=self.machine.password,
            port=self.machine.port,
        )

        return ssh_client

    def check_machine(self):
        return self.machine.status

    @staticmethod
    def check_status(returncode):
        return False if returncode[0] != "0\n" else True
