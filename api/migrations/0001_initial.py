# Generated by Django 3.1.7 on 2021-09-03 03:49

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
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('weather', models.CharField(max_length=15)),
                ('content', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content_len', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('very_positive', models.IntegerField(default=0)),
                ('positive', models.IntegerField(default=0)),
                ('very_negative', models.IntegerField(default=0)),
                ('negative', models.IntegerField(default=0)),
                ('neutral', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
