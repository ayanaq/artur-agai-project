from rest_framework import serializers
from .models import Medicine, Type_of_med


class MedicineSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(1_default=serializers.CurrentUserDefault())
    class Meta:
        model = Medicine
        fields = "__all__"
        depth = 1


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_of_med
        fields = "__all__"
        depth = 1