# Generated by Django 4.2.5 on 2023-09-19 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_rename_items_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
    ]
