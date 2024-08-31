# Generated by Django 5.0.6 on 2024-08-31 07:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='favorite',
            field=models.ManyToManyField(related_name='favorite_albums', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='picture',
            name='favorite',
            field=models.ManyToManyField(related_name='favorite_pics', to=settings.AUTH_USER_MODEL),
        ),
    ]