# Generated by Django 4.2.4 on 2023-10-03 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_delete_time_remove_log_all_total_student_time_spend'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='log',
            name='card_id',
            field=models.IntegerField(default=0),
        ),
    ]