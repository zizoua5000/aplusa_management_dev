# Generated by Django 3.0.3 on 2020-04-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('deleted_at', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'company',
                'managed': False,
            },
        ),
    ]
