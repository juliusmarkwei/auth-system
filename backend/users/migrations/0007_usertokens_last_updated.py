# Generated by Django 4.2.7 on 2023-11-19 10:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_usertokens_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertokens',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]