# Generated by Django 4.2.1 on 2023-05-24 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_member_address_member_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='memid',
            field=models.CharField(max_length=255, null=True),
        ),
    ]