# Generated by Django 4.2.1 on 2023-05-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0004_questions_contest'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contest',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
