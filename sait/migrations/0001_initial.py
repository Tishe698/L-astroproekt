# Generated by Django 2.2.16 on 2023-09-07 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='menu_images/')),
                ('text', models.TextField(max_length=67)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='menu_images/')),
                ('text', models.TextField(max_length=68)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=68)),
                ('text2', models.TextField(max_length=73)),
            ],
        ),
    ]
