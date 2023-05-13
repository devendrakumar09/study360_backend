# Generated by Django 4.2.1 on 2023-05-13 06:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('practiceSet', '0006_rename_uid_answers_id_rename_uid_categories_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_category', to='practiceSet.maincategory'),
        ),
    ]