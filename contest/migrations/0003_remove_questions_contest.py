# Generated by Django 4.2.1 on 2023-05-15 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_remove_questions_category_rename_category_categories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='contest',
        ),
    ]
