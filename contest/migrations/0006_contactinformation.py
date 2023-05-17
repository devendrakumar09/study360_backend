# Generated by Django 4.2.1 on 2023-05-16 03:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0005_categories_thumbnail_contest_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=50)),
                ('thumbnail', models.ImageField(null=True, upload_to='')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contest_information', to='contest.contest')),
            ],
        ),
    ]
