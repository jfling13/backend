# Generated by Django 4.2.4 on 2023-08-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_pub_time_post_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comfirmed',
            field=models.BooleanField(default=False),
        ),
    ]