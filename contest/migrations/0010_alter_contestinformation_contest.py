# Generated by Django 4.2.1 on 2023-05-16 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0009_remove_answers_created_at_remove_answers_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestinformation',
            name='contest',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contest_information', to='contest.contest'),
        ),
    ]