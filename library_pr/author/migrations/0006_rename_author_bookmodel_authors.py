# Generated by Django 5.1.4 on 2025-03-17 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0005_alter_articlemodel_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmodel',
            old_name='author',
            new_name='authors',
        ),
    ]
