# Generated by Django 3.1.3 on 2021-01-12 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_delete_texts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Tytuł sekcji', max_length=30, null=True)),
                ('desc', models.TextField(blank=True, default='Opis', max_length=15000, null=True)),
                ('pub_date', models.DateTimeField(verbose_name='Data publikacji')),
                ('link', models.CharField(blank=True, default='', max_length=2000, null=True)),
                ('link_name', models.CharField(blank=True, default='', max_length=2000, null=True)),
                ('image', models.FileField(upload_to='static/')),
            ],
        ),
    ]
