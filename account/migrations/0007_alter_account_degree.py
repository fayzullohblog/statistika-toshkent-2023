# Generated by Django 4.1.7 on 2023-05-08 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0006_alter_account_degree"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="degree",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
