# Generated by Django 4.2.4 on 2023-08-19 14:49

from django.db import migrations, models
import django.db.models.aggregates
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('preparation_time', models.PositiveIntegerField(blank=True, null=True, verbose_name=django.db.models.aggregates.Min(1))),
                ('image', models.ImageField(upload_to='recipe_images')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_app.recipe')),
            ],
        ),
    ]