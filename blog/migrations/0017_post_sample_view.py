# Generated by Django 2.1.7 on 2019-03-26 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190325_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sample_view',
            field=models.ImageField(default='sample_score.jpg', null=True, upload_to='sample_sheet'),
        ),
    ]
