# Generated by Django 4.1.7 on 2023-07-01 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_rename_locatiion_tbl_restaurantaccount_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('restname', models.CharField(max_length=30)),
                ('fooditemname', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_cart',
            },
        ),
        migrations.CreateModel(
            name='tbl_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('restname', models.CharField(max_length=30)),
                ('totalprice', models.IntegerField()),
                ('paymentmode', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_order',
            },
        ),
    ]
