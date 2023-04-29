# Generated by Django 4.1.7 on 2023-04-28 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("common", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageFile",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="common.basemodel",
                    ),
                ),
                ("image_pdf", models.FileField(unique=True, upload_to="images_pdf")),
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("state", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "ImageFile",
                "verbose_name_plural": "ImageFiles",
            },
            bases=("common.basemodel",),
        ),
        migrations.CreateModel(
            name="ImagePart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "oneimage",
                    models.FileField(blank=True, null=True, upload_to="oneimage"),
                ),
                ("title", models.CharField(blank=True, max_length=250, null=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "imagefile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="imageparts",
                        to="images_files.imagefile",
                    ),
                ),
            ],
            options={
                "verbose_name": "ImagePart",
                "verbose_name_plural": "ImageParts",
            },
        ),
    ]
