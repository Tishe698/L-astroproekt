# Generated by Django 4.2.5 on 2023-09-07 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sait", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="menuitem2",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="menuitem3",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]