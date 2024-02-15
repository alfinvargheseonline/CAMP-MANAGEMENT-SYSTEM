# Generated by Django 4.1.13 on 2024-02-05 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintmodel',
            name='complaint_against',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='bedid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.bedmodel'),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='busid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.transportationmodel'),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='itemid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.itemmodel'),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='usertypeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.usertypemodel'),
        ),
        migrations.AddField(
            model_name='leavestatusmodel',
            name='numberofdays',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.leaverequestmodel'),
        ),
        migrations.AddField(
            model_name='roommodel',
            name='campid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.campmodel'),
        ),
        migrations.AddField(
            model_name='roommodel',
            name='flatid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.flat'),
        ),
    ]