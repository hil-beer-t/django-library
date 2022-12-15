# Generated by Django 4.1.4 on 2022-12-15 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mat', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=150, unique=True)),
                ('isbn', models.CharField(blank=True, max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('publisher', models.CharField(max_length=150)),
                ('type', models.CharField(blank=True, max_length=100)),
                ('is_only_reference', models.BooleanField(default=True)),
                ('is_borrowed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('is_returned', models.BooleanField()),
                ('ok_returned', models.BooleanField()),
                ('days_late', models.PositiveSmallIntegerField()),
                ('app_user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='loans.appuser')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='loans.book')),
            ],
        ),
    ]
