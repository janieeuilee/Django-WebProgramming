# Generated by Django 2.1.2 on 2018-10-31 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='who',
            field=models.CharField(choices=[('1', '기업'), ('2', '개인')], max_length=1),
        ),
    ]
