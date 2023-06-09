# Generated by Django 4.1.7 on 2023-03-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_entries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Image name')),
                ('text', models.TextField(verbose_name='Image text')),
                ('img', models.ImageField(upload_to='images', verbose_name='Work image')),
            ],
        ),
    ]
