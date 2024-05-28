# Generated by Django 5.0.6 on 2024-05-28 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256, unique=True, verbose_name='Bolim nomi')),
            ],
            options={
                'verbose_name': 'Bolim',
                'verbose_name_plural': 'Bolimlar',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(verbose_name='Izoh')),
            ],
            options={
                'verbose_name': 'Izoh',
                'verbose_name_plural': 'Izohlar',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256, verbose_name='Sarlavhasi')),
                ('content', models.TextField(verbose_name='Matni')),
                ('picture', models.ImageField(upload_to='media/', verbose_name='Post uchun rasm')),
                ('is_published', models.BooleanField(default=False, verbose_name='Ruxsat?')),
                ('view_count', models.IntegerField(default=0, verbose_name='Korishlar soni')),
                ('recommended', models.BooleanField(default=False, verbose_name='Tavsiya qilinsinmi?')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Postlar',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='Teg nomi')),
            ],
            options={
                'verbose_name': 'Teg',
                'verbose_name_plural': 'Teglar',
            },
        ),
    ]
