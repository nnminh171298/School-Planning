# Generated by Django 2.0.1 on 2018-02-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0003_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
