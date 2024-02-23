from django.db import models


class Item(models.Model):
    ItemTypes = models.TextChoices('ItemTypes', 'Оружие Броня Перчатки Сапоги Шлем Особое')

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=ItemTypes.choices)

    def __str__(self):
        return self.name


class Hero(models.Model):
    CLASSES = [
        ('W', 'Воин'),
        ('M', 'Маг'),
        ('A', 'Лучник'),
        ('T', 'Вор')
    ]

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    hero_class = models.CharField(max_length=1, choices=CLASSES)
    level = models.IntegerField(default=1)
    creation_data = models.DateTimeField("Creation data", auto_now=True)

    health = models.IntegerField(default=100)
    mana = models.IntegerField(default=100)
    attack = models.IntegerField(default=100)
    defence = models.IntegerField(default=100)

    gold = models.IntegerField(default=1000)
    list_of_items = models.ManyToManyField(Item)

    def __str__(self):
        return self.name

    def stats(self):
        stats = {
            'HP': self.health,
            'MP': self.mana,
            'ATK': self.attack,
            'DEF': self.defence
        }
        return stats

    def inventory(self):
        inventory = self.list_of_items.get_queryset().all()
        return inventory

    def level_up(self):
        self.level += 1
        self.save()

    def remove_item_from_inventory(self, item: Item):
        self.list_of_items.remove(item)
        self.save()

    def give_item_to_hero(self, item: Item):
        self.list_of_items.add(item)
        self.save()
