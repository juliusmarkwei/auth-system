# Generated by Django 4.2.7 on 2023-11-19 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_access_token_usertokens_token_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertokens',
            options={'verbose_name': 'User Token', 'verbose_name_plural': 'User Tokens'},
        ),
    ]