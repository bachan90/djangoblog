# Generated by Django 4.2.6 on 2023-12-03 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_publish_date_post_published_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='publish_date',
        ),
    ]
