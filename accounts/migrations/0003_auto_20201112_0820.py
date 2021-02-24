# Generated by Django 3.1 on 2020-11-12 00:20
from __future__ import unicode_literals
from django.db import migrations
from accounts.models import CustomUser, Authority
import sys

def forwards_func(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    db_alias = schema_editor.connection.alias
    Group.objects.using(db_alias).bulk_create([
        Group(name='Landgate'),
        Group(name='Geodesy'),
        Group(name='Others'),
        Group(name='Admin'),
    ])
    
    uname = input("Enter your email: ")
    pword1 = input("Enter a password: ")
    pword2 = input("Re-confirm your password: ")
    
    if pword1 == pword2:
        CustomUser.objects.create_superuser(
        	email=uname,  
        	password=pword1,
            authority= Authority.objects.get(authority_abbrev='LG')
        	)
    else:
        print("Your passwords do not match. Start again!")
        sys.exit()

def reverse_func(apps, schema_editor):
	Group = apps.get_model("auth", "Group")
	Group.object.all().delete()

	CustomUser.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201110_0811'),
    ]

    operations = [
	    migrations.RunPython(
	            forwards_func, reverse_func
	        ),
    ]
