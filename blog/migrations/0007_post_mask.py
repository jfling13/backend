# Generated by Django 4.2.4 on 2023-09-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mask',
            field=models.ImageField(default='masks/img_0560.jpg', upload_to='masks/'),
            preserve_default=False,
        ),
    ]
