# Generated by Django 4.2.7 on 2023-12-15 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestatairesoinsprofile',
            name='type',
        ),
    ]