# Generated by Django 3.0.2 on 2020-02-02 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_user_on_call'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='on_call',
            field=models.BooleanField(),
        ),
    ]
