# Generated by Django 3.2.25 on 2024-04-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0199_status_bookwyrm_st_remote__06aeba_idx"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="status",
            index=models.Index(
                fields=["thread_id"], name="bookwyrm_st_thread__cf064f_idx"
            ),
        ),
    ]
