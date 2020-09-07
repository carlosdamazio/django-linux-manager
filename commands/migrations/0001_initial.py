# Generated by Django 3.1.1 on 2020-09-07 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.TextField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.machine')),
            ],
        ),
    ]
