# Generated by Django 4.2.1 on 2023-05-18 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0015_alter_categories_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='static\\contest'),
        ),
    ]