# Generated by Django 4.2.5 on 2023-10-01 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0007_alter_newpost_content_alter_newpost_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(blank=True, max_length=50, null=True)),
                ('instagram', models.CharField(blank=True, max_length=50, null=True)),
                ('facebook', models.CharField(blank=True, max_length=50, null=True)),
                ('twitter', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/profile/')),
                ('contact', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_page_emails', to=settings.AUTH_USER_MODEL)),
                ('firstname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_page_firstnames', to=settings.AUTH_USER_MODEL)),
                ('lastname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_page_lastnames', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_page_usernames', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]