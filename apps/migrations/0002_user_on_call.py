# Generated by Django 3.0.2 on 2020-02-02 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='on_call',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]