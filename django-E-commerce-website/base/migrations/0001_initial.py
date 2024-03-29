# Generated by Django 4.2.6 on 2023-11-27 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.CharField(max_length=50)),
                ('item_desc', models.TextField()),
                ('item_created_at', models.DateTimeField(auto_now_add=True)),
                ('is_solde', models.BooleanField(default=False)),
                ('item_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itekms_brand', to='base.brand')),
                ('item_deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itekms_deal', to='base.deal')),
            ],
        ),
        migrations.CreateModel(
            name='size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='messegis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('items_messegis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_messegis', to='base.item')),
                ('messegis_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_messegis', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itekms_size', to='base.size'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itekms_tipes', to='base.tipe'),
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/items_images')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='base.item')),
            ],
        ),
    ]
