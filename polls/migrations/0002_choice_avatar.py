# Generated by Django 4.2 on 2024-08-05 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='avatar',
            field=models.FileField(default='', upload_to='upload/avatar/', verbose_name='avatar'),
            preserve_default=False,
        ),
    ]
