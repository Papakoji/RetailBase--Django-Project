# Generated by Django 5.0.6 on 2024-07-10 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_customer_table'),
    ]

    operations = [
        migrations.RunSQL(
            """ 
            INSERT INTO store_collection (title) 
            VALUES ('collection1')
            """,
            """ 
            DELETE FROM store_collection 
            WHERE title = 'collection1'
            """
        )
    ]
