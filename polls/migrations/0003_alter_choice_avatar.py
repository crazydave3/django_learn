# Generated by Django 4.2 on 2024-08-05 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='avatar',
            field=models.FileField(upload_to='polls/', verbose_name='avatar'),
        ),
    ]
