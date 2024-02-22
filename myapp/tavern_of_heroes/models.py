from django.db import models


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
    creation_data = models.DateTimeField("Creation data")
    health = models.IntegerField(default=100)
    mana = models.IntegerField(default=100)
    attack = models.IntegerField(default=100)
    defence = models.IntegerField(default=100)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        hero_inv = Inventory()
        hero_inv.hero = self
        hero_inv.save()


class Inventory(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, null=False)
    gold = models.IntegerField(default=1000)
    list_of_items = models.ExpressionList(models.CharField(max_length=20))
