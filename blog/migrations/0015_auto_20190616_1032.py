# Generated by Django 2.0.13 on 2019-06-16 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190616_1027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutme',
            old_name='mybiotext',
            new_name='atext',
        ),
        migrations.AddField(
            model_name='aboutme',
            name='atitle',
            field=models.CharField(default='Welcome to My Blog', max_length=200),
        ),
    ]
