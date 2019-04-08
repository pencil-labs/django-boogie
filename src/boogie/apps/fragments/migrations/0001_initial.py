# Generated by Django 2.1.7 on 2019-03-10 22:15

import boogie.apps.fragments.enums
import boogie.fields.enum_field
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fragment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ref",
                    models.CharField(
                        db_index=True,
                        help_text="Unique identifier for fragment name",
                        max_length=100,
                        unique=True,
                        verbose_name="Identifier",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="Optional description that helps humans identify the content and role of the fragment.",
                        max_length=100,
                    ),
                ),
                (
                    "format",
                    boogie.fields.enum_field.EnumField(
                        boogie.apps.fragments.enums.Format,
                        help_text="Defines how content is interpreted.",
                        verbose_name="Format",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        blank=True,
                        help_text="Raw fragment content in HTML or Markdown",
                        verbose_name="content",
                    ),
                ),
                ("editable", models.BooleanField(default=True, editable=False)),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="FragmentLock",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fragment",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="lock_ref",
                        to="fragments.Fragment",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
    ]
