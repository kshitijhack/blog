# Generated by Django 2.2.6 on 2019-11-06 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='text',
            new_name='textarea',
        ),
    ]
