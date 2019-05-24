# Generated by Django 2.1.4 on 2019-01-30 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_blogpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='user_number',
            new_name='update_count',
        ),
        migrations.CreateModel(
            name='DateConversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('timezone', models.CharField(default='PST', max_length=50)),
                ('status', models.CharField(default='In Progress', max_length=50)),
            ],
        ),
    ]