# Generated by Django 2.1.7 on 2019-03-07 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiManagement', '0002_email_send_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='subject',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
