# Generated by Django 4.2.4 on 2023-08-29 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniblogs', '0003_remove_miniblog_replied_to_miniblogreply'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiniBlogQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MiniBlogRepost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
