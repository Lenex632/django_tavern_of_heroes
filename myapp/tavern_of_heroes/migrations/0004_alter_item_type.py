# Generated by Django 4.2 on 2024-02-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tavern_of_heroes', '0003_item_hero_gold_delete_inventory_hero_list_of_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('Оружие', 'Оружие'), ('Броня', 'Броня'), ('Перчатки', 'Перчатки'), ('Сапоги', 'Сапоги'), ('Шлем', 'Шлем'), ('Особое', 'Особое')], max_length=20),
        ),
    ]
