# Generated by Django 4.1.7 on 2023-05-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_remove_test_questions_testquestion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="test",
            name="date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
