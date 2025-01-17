# Generated by Django 5.0.4 on 2024-07-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('region', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=50)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
