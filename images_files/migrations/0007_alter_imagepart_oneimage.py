# Generated by Django 4.1.7 on 2023-04-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images_files", "0006_alter_imagepart_oneimage_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagepart",
            name="oneimage",
            field=models.FileField(default=1, upload_to="oneimage"),
            preserve_default=False,
        ),
    ]
