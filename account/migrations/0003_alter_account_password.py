# Generated by Django 4.1.7 on 2023-04-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_alter_account_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="password",
            field=models.CharField(max_length=100),
        ),
    ]