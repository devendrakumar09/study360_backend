# Generated by Django 4.2.1 on 2023-05-16 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0006_contactinformation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactInformation',
            new_name='ContestInformation',
        ),
    ]
