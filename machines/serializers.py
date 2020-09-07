from rest_framework import serializers

from machines.models import Machine


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = [
            'id',
            'name',
            'ip',
            'ssh_pub_key',
            'ssh_priv_key',
            'user',
            'password',
            'port',
            'status'
        ]

    def create(self, validated_data):
        return Machine.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.ip = validated_data.get("ip", instance.ip)
        instance.ssh_pub_key = validated_data.get("ssh_pub_key", instance.ssh_pub_key)
        instance.ssh_priv_key = validated_data.get("ssh_priv_key", instance.ssh_priv_key)
        instance.user = validated_data.get("user", instance.user)
        instance.password = validated_data.get("password", instance.password)
        instance.port = validated_data.get("port", instance.port)
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance
