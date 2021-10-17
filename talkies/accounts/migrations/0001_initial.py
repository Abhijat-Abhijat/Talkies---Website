# Generated by Django 3.2.8 on 2021-10-14 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=120)),
                ('login_count', models.PositiveBigIntegerField(default=0)),
            ],
        ),
    ]