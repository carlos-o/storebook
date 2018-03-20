from django.db import models, migrations


def group_migration(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.bulk_create([
        Group(name=u'Admin'),
        Group(name=u'Normal'),
        Group(name=u'Observer'),
    ])


# def revert_migration(apps, schema_editor):
#     Group = apps.get_model('auth', 'Group')
#     Group.objects.filter(
#         name__in=[
#             u'group1',
#             u'group2',
#             u'group3',
#         ]
#     ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(group_migration)
    ]