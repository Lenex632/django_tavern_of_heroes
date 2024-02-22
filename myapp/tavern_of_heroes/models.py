from django.db import models


class Item(models.Model):
    ItemTypes = models.TextChoices("ItemTypes", "Armor Helmet Gloves Boots Weapon Special")

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
    creation_data = models.DateTimeField("Creation data")

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
