# Generated by Django 4.1.7 on 2023-04-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images_files", "0005_remove_imagefile_title_imagefile_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagepart",
            name="oneimage",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="imagepart",
            name="qrcode_image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
