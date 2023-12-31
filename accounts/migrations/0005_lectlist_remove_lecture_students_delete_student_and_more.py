# Generated by Django 4.2 on 2023-05-22 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LectList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='students',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='lectlist',
            name='myLect',
            field=models.ManyToManyField(to='accounts.lecture'),
        ),
    ]
