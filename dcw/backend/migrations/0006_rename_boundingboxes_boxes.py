# Generated by Django 4.1.3 on 2023-05-14 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_rename_bounding_boxes_boundingboxes_boxes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BoundingBoxes',
            new_name='Boxes',
        ),
    ]
