# Generated by Django 3.0.8 on 2020-09-29 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_auto_20200929_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='lists',
            new_name='item',
        ),
    ]
