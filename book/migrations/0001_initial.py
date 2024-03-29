# Generated by Django 2.2.5 on 2019-11-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100, null=True)),
                ('logo', models.TextField(null=True)),
                ('publisher', models.CharField(max_length=100, null=True)),
                ('published', models.CharField(max_length=20, null=True)),
                ('page', models.CharField(max_length=10, null=True)),
                ('price', models.CharField(max_length=10, null=True)),
                ('designed', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(default='', null=True)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
