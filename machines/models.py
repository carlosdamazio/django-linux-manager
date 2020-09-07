import subprocess

from django.db import models


class Machine(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    ip = models.CharField(max_length=20, blank=False, null=False)
    ssh_pub_key = models.TextField(blank=True, null=True)
    ssh_priv_key = models.TextField(blank=True, null=True)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=255, default="")
    port = models.IntegerField(null=False, blank=False, default=22)
    status = models.BooleanField(default=False)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def ping(self):
        return True if subprocess.run(["ping", self.ip, "-c", "1"], ).returncode == 0 else False

    def save(self, *args, **kwargs):
        self.status = self.ping()
        super(Machine, self).save(*args, **kwargs)
