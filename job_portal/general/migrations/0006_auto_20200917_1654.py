# Generated by Django 3.0.8 on 2020-09-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_seeker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seeker',
            name='industry',
            field=models.CharField(max_length=50),
        ),
    ]
