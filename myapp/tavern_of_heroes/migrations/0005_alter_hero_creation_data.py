# Generated by Django 4.2 on 2024-02-23 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tavern_of_heroes', '0004_alter_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='creation_data',
            field=models.DateTimeField(auto_now=True, verbose_name='Creation data'),
        ),
    ]
