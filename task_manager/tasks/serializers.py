from rest_framework import serializers
from .models import Task
from datetime import date

class TaskSerializer(serializers.ModelSerializer):
    is_overdue = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('user',)

    def get_is_overdue(self, obj):
        return obj.status != 'done' and obj.due_date < date.today()