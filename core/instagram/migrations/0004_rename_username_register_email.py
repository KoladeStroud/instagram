# Generated by Django 4.0.2 on 2022-07-04 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='username',
            new_name='email',
        ),
    ]
