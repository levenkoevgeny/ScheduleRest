from django.db import models


class Teacher(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="Last name")
    first_name = models.CharField(max_length=100, verbose_name="First name", blank=True, null=True)
    patronymic = models.CharField(max_length=100, verbose_name="Patronymic", blank=True, null=True)

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ('last_name',)
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class TrainingSession(models.Model):
    start_time = models.TimeField(verbose_name="Start time")
    end_time = models.TimeField(verbose_name="End time")

    def __str__(self):
        return str(self.start_time) + ' - ' + str(self.end_time)

    class Meta:
        ordering = ('start_time',)
        verbose_name = 'Training session'
        verbose_name_plural = 'Training sessions'


class Location(models.Model):
    location_address = models.TextField(verbose_name="address")

    def __str__(self):
        return self.location_address

    class Meta:
        ordering = ('id',)
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'


class ClassRoom(models.Model):
    class_room_number = models.CharField(max_length=100, verbose_name="Classroom number")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="Location", related_name="rooms")

    def __str__(self):
        return self.class_room_number + ' (' + self.location.location_address + ')'

    class Meta:
        ordering = ('class_room_number',)
        verbose_name = 'ClassRoom'
        verbose_name_plural = 'ClassRooms'


class GroupUnit(models.Model):
    group_unit = models.CharField(max_length=255, verbose_name="Group unit")

    def __str__(self):
        return self.group_unit

    class Meta:
        ordering = ('group_unit',)
        verbose_name = 'GroupUnit'
        verbose_name_plural = 'GroupUnits'


class Group(models.Model):
    group_name = models.CharField(max_length=100, verbose_name="Group name")
    group_unit = models.ForeignKey(GroupUnit, on_delete=models.CASCADE, verbose_name=" Group unit",
                                   related_name='groups')

    def __str__(self):
        return self.group_name + ' (' + self.group_unit.group_unit + ')'

    class Meta:
        ordering = ('group_name',)
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class Schedule(models.Model):
    schedule_day_date = models.DateField(verbose_name="Date")
    training_session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE, verbose_name="Training Session")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Teacher", blank=True, null=True)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, verbose_name="Class room", blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Group", blank=True, null=True)

    def __str__(self):
        return str(self.schedule_day_date)

    class Meta:
        ordering = ('schedule_day_date',)
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'






