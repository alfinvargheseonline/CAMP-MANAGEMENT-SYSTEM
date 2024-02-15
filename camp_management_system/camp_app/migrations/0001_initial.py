# Generated by Django 4.1.13 on 2024-02-05 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampModel',
            fields=[
                ('campid', models.AutoField(primary_key=True, serialize=False)),
                ('campname', models.CharField(default='', max_length=400)),
                ('location', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=400)),
                ('phone', models.BigIntegerField(null=True)),
                ('numberofrooms', models.IntegerField(default='', max_length=100)),
                ('numberoffloors', models.IntegerField(default='', max_length=100)),
                ('numberofBeds', models.IntegerField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('employeeid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.BigIntegerField(null=True)),
                ('dob', models.DateField()),
                ('address', models.CharField(default=' ', max_length=400)),
                ('nationality', models.CharField(default='', max_length=100)),
                ('jobcategory', models.CharField(default='', max_length=100)),
                ('passport', models.CharField(default='', max_length=100)),
                ('passportexpiry', models.DateField()),
                ('department', models.CharField(default='', max_length=100)),
                ('bloodgroup', models.CharField(default='', max_length=100)),
                ('diagnosisdiseases', models.CharField(default='', max_length=100)),
                ('emergencymedicine', models.CharField(default='', max_length=100)),
                ('emergencyphone', models.BigIntegerField(null=True)),
                ('domesticaddress', models.CharField(default='', max_length=400)),
                ('education', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('flatid', models.AutoField(primary_key=True, serialize=False)),
                ('flatnumber', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HRManagerModel',
            fields=[
                ('hrmanagerid', models.AutoField(primary_key=True, serialize=False)),
                ('hrmanagername', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('itemid', models.AutoField(primary_key=True, serialize=False)),
                ('itemname', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveTypeModel',
            fields=[
                ('leavetypeid', models.AutoField(primary_key=True, serialize=False)),
                ('leavetypename', models.CharField(default='', max_length=100)),
                ('totalnoofdays', models.IntegerField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RoomTypeModel',
            fields=[
                ('roomtypeid', models.AutoField(primary_key=True, serialize=False)),
                ('roomtypename', models.CharField(default='', max_length=100)),
                ('occupancy', models.IntegerField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserTypeModel',
            fields=[
                ('usertypeid', models.AutoField(primary_key=True, serialize=False)),
                ('usertypename', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TransportationModel',
            fields=[
                ('busid', models.AutoField(primary_key=True, serialize=False)),
                ('busname', models.CharField(default='', max_length=100)),
                ('destination', models.CharField(default='', max_length=200)),
                ('time', models.TimeField()),
                ('campid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.campmodel')),
            ],
        ),
        migrations.CreateModel(
            name='StorageModel',
            fields=[
                ('storageid', models.AutoField(primary_key=True, serialize=False)),
                ('fromdate', models.DateTimeField()),
                ('todate', models.DateTimeField()),
                ('items', models.CharField(default='', max_length=100)),
                ('employeeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.employeemodel')),
            ],
        ),
        migrations.CreateModel(
            name='RoomModel',
            fields=[
                ('roomid', models.AutoField(primary_key=True, serialize=False)),
                ('floor', models.IntegerField(default='', max_length=100)),
                ('roomtypeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.roomtypemodel')),
            ],
        ),
        migrations.CreateModel(
            name='MessModel',
            fields=[
                ('messid', models.AutoField(primary_key=True, serialize=False)),
                ('messcaptainname', models.CharField(default='', max_length=100)),
                ('cuisine', models.CharField(default='', max_length=100)),
                ('timingfrom', models.TimeField()),
                ('timingto', models.TimeField()),
                ('campid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.campmodel')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveStatusModel',
            fields=[
                ('leavestatusid', models.AutoField(primary_key=True, serialize=False)),
                ('remainingdays', models.IntegerField(default='', max_length=100)),
                ('employeeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.employeemodel')),
                ('leavetypeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.leavetypemodel')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRequestModel',
            fields=[
                ('requestid', models.AutoField(primary_key=True, serialize=False)),
                ('reason', models.CharField(default='', max_length=400)),
                ('numberofdays', models.IntegerField(default='', max_length=100)),
                ('fromdate', models.DateField()),
                ('todate', models.DateField()),
                ('approvalstatus', models.CharField(default='', max_length=100)),
                ('employeeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.employeemodel')),
                ('leavetypeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.leavetypemodel')),
            ],
        ),
        migrations.CreateModel(
            name='complaintModel',
            fields=[
                ('complaintid', models.AutoField(primary_key=True, serialize=False)),
                ('reason', models.CharField(default='', max_length=400)),
                ('date', models.DateField()),
                ('employeeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.employeemodel')),
            ],
        ),
        migrations.CreateModel(
            name='BedModel',
            fields=[
                ('bedid', models.AutoField(primary_key=True, serialize=False)),
                ('roomid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp_app.roommodel')),
            ],
        ),
    ]
