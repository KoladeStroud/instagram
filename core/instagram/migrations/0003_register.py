# Generated by Django 4.0.2 on 2022-07-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_alter_logins_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
            ],
        ),
    ]
