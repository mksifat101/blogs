# Generated by Django 3.1 on 2021-11-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeBanner2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('banner', models.ImageField(upload_to='home_banner1')),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]