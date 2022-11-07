from rest_framework import viewsets, mixins
from .models import Location, ClassRoom, Group, GroupUnit, Teacher, TrainingSession, Schedule
from .serializers import LocationSerializer, ClassRoomSerializer, GroupSerializer, GroupUnitSerializer, \
    TeacherSerializer, TrainingSessionSerializer, ScheduleSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupUnitViewSet(viewsets.ModelViewSet):
    queryset = GroupUnit.objects.all()
    serializer_class = GroupUnitSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TrainingSessionViewSet(viewsets.ModelViewSet):
    queryset = TrainingSession.objects.all()
    serializer_class = TrainingSessionSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filterset_fields = ['group__id', 'teacher__id']
