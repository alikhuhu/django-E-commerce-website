# Generated by Django 4.2.6 on 2023-12-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_item_l_amaont_item_m_amaont_item_s_amaont_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='image1',
            field=models.ImageField(default='Null', upload_to='static/items_images'),
        ),
        migrations.AddField(
            model_name='image',
            name='image10',
            field=models.ImageField(default='Null', upload_to='static/items_images'),
        ),
        migrations.AddField(
            model_name='image',
            name='image2',
            field=models.ImageField(default='Null', upload_to='static/items_images'),
        ),
        migrations.AddField(
            model_name='image',
            name='image3',
            field=models.ImageField(default='Null', upload_to='static/items_images'),
        ),
        migrations.AddField(
            model_name='image',
            name='image4',
            field=models.ImageField(default='Null', upload_to='static/items_images'),
        ),
        migrations.AddField(
            model_name='image',
            name='image5',
            field=models.ImageField(default='Null', upload_to='static/items_images'),
        ),
        migrations.AddField(
            model_name='image',
            name='image6',
            field=models.ImageField(default='Null', upload_to='static/items_images'),
        ),
        migrations.AddField(
            model_name='image',
            name='image7',
            field=models.ImageField(default='Null', upload_to='static/items_images'),
        ),
        migrations.AddField(
            model_name='image',
            name='image8',
            field=models.ImageField(default='Null', upload_to='static/items_images'),
        ),
        migrations.AddField(
            model_name='image',
            name='image9',
            field=models.ImageField(default='Null', upload_to='static/items_images'),
        ),
    ]
