# Generated by Django 2.1.7 on 2019-04-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story_search', '0003_auto_20190418_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='ao3_userlink',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='ffnet_userlink',
            field=models.URLField(null=True),
        ),
    ]