# Generated by Django 4.0.3 on 2022-05-05 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Profile', '0005_remove_like_question_remove_like_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeOrDislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_dislike', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.question', verbose_name='კითხვა')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='მომხმარებელი')),
            ],
        ),
    ]
