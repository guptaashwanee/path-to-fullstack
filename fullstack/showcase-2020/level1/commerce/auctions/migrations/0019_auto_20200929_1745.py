# Generated by Django 3.0.8 on 2020-09-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_watchlist_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='item',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='list',
            field=models.ManyToManyField(to='auctions.List'),
        ),
    ]
