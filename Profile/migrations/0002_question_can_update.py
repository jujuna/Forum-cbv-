# Generated by Django 4.0.3 on 2022-04-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='can_update',
            field=models.IntegerField(default=2),
        ),
    ]
