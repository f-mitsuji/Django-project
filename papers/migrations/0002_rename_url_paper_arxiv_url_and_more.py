# Generated by Django 5.0.2 on 2024-02-23 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='url',
            new_name='arxiv_url',
        ),
        migrations.RenameField(
            model_name='paper',
            old_name='publish_date',
            new_name='published_at',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='arxiv_id',
        ),
    ]