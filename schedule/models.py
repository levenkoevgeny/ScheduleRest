from django.db import models


class Teacher(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="Last name")

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


class ClassRoom(models.Model):
    class_room_number = models.CharField(max_length=100, verbose_name="Classroom number")

    def __str__(self):
        return self.class_room_number

    class Meta:
        ordering = ('class_room_number',)
        verbose_name = 'ClassRoom'
        verbose_name_plural = 'ClassRooms'


class Group(models.Model):
    group_name = models.CharField(max_length=100, verbose_name="Group name")

    def __str__(self):
        return self.group_name

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






