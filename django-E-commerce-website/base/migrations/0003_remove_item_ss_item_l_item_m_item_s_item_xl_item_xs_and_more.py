# Generated by Django 4.2.6 on 2023-11-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_item_ss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='ss',
        ),
        migrations.AddField(
            model_name='item',
            name='l',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='m',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='s',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='xl',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='xs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='xxl',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='xxxl',
            field=models.BooleanField(default=False),
        ),
    ]
