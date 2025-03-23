# Generated by Django 5.1.7 on 2025-03-23 07:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("github", "0018_alter_issue_managers_alter_pullrequest_managers"),
        ("owasp", "0031_merge_20250320_2001"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chapter",
            name="leaders",
            field=models.ManyToManyField(
                blank=True,
                related_name="assigned_%(class)s",
                to="github.user",
                verbose_name="Assigned leaders",
            ),
        ),
        migrations.AlterField(
            model_name="chapter",
            name="suggested_leaders",
            field=models.ManyToManyField(
                blank=True,
                related_name="matched_%(class)s",
                to="github.user",
                verbose_name="Matched Users",
            ),
        ),
        migrations.AlterField(
            model_name="committee",
            name="leaders",
            field=models.ManyToManyField(
                blank=True,
                related_name="assigned_%(class)s",
                to="github.user",
                verbose_name="Assigned leaders",
            ),
        ),
        migrations.AlterField(
            model_name="committee",
            name="suggested_leaders",
            field=models.ManyToManyField(
                blank=True,
                related_name="matched_%(class)s",
                to="github.user",
                verbose_name="Matched Users",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="leaders",
            field=models.ManyToManyField(
                blank=True,
                related_name="assigned_%(class)s",
                to="github.user",
                verbose_name="Assigned leaders",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="suggested_leaders",
            field=models.ManyToManyField(
                blank=True,
                related_name="matched_%(class)s",
                to="github.user",
                verbose_name="Matched Users",
            ),
        ),
    ]
