# Generated by Django 4.1.7 on 2023-05-03 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images_files", "0002_zipimagepart"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagepart",
            name="oneimage",
            field=models.FileField(blank=True, default=1, upload_to="oneimage"),
            preserve_default=False,
        ),
    ]
