# Generated by Django 3.0.3 on 2020-04-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessoryHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('entry_warehouse_date', models.DateTimeField(editable=False,blank=True,null=True)),
                ('created_at', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'accessory_history',
                'managed': False,
            },
        ),
    ]
