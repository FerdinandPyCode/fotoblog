# Generated by Django 4.1.1 on 2022-10-01 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='titre')),
                ('content', models.CharField(max_length=5000, verbose_name='contenu')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('starred', models.BooleanField(default=False)),
                ('word_count', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('caption', models.CharField(blank=True, max_length=128, verbose_name='légende')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogContributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribution', models.CharField(blank=True, max_length=255)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('contributor', 'blog')},
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='contributors',
            field=models.ManyToManyField(related_name='contributions', through='blog.BlogContributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.photo'),
        ),
    ]
