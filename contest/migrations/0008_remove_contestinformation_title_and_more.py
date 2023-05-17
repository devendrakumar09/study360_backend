# Generated by Django 4.2.1 on 2023-05-16 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0007_rename_contactinformation_contestinformation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestinformation',
            name='title',
        ),
        migrations.AddField(
            model_name='contestinformation',
            name='Top50Price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='contestinformation',
            name='close',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='contestinformation',
            name='firstPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='contestinformation',
            name='open',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='contestinformation',
            name='secondPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='contestinformation',
            name='thirdPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
