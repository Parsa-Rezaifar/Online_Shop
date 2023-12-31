# Generated by Django 4.2.5 on 2023-09-11 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_slug', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_slug', models.SlugField(max_length=100, unique=True)),
                ('product_image', models.ImageField(upload_to='product/')),
                ('product_description', models.TextField()),
                ('product_price', models.IntegerField()),
                ('product_availability', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('related_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Home.category')),
            ],
            options={
                'ordering': ('product_name',),
            },
        ),
    ]
