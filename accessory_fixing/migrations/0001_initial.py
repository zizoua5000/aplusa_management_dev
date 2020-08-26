# Generated by Django 3.0.3 on 2020-04-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('deleted_at', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'accessory',
                'managed': False,
            },
        ),
    ]
