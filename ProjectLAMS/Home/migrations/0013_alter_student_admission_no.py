# Generated by Django 4.2.6 on 2023-11-04 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_alter_log_card_id_alter_student_card_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
