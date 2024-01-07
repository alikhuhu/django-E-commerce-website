# Generated by Django 4.2.6 on 2023-11-27 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_remove_item_ss_item_l_item_m_item_s_item_xl_item_xs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='l_amaont',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='m_amaont',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='s_amaont',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='xl_amaont',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='xs_amaont',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='xxl_amaont',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='xxxl_amaont',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='user_prof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phon_number', models.CharField(max_length=11)),
                ('user_near_living', models.CharField(max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_prof', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_orderd', to='base.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
