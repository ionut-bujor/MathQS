# Generated by Django 4.2.7 on 2024-02-12 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details_quiz',
            name='username',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
