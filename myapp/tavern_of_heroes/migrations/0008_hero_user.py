# Generated by Django 4.2 on 2024-05-05 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tavern_of_heroes', '0007_alter_hero_creation_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
