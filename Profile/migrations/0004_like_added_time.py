# Generated by Django 4.0.3 on 2022-04-25 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_favoritequestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='added_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
