# Generated by Django 3.0.8 on 2020-08-26 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20200825_2246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='htmltag',
            old_name='html',
            new_name='html_tag',
        ),
    ]