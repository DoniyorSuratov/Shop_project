# Generated by Django 4.2.6 on 2023-10-26 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_blogphotos_user_comment_blogphotos_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userblogcomments',
            old_name='user',
            new_name='author',
        ),
    ]
