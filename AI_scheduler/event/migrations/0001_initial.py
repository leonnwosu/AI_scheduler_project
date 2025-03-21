# Generated by Django 5.1.7 on 2025-03-13 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_type', models.CharField(choices=[('Original', 'original'), ('User-added', 'user-added'), ('AI-added', 'ai-added')], default='User added', max_length=255)),
                ('event_title', models.CharField(max_length=255)),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('event_description', models.CharField(max_length=2083)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
