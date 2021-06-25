from rest_framework import serializers
from .models import Comp

class CompSerializer(serializers.ModelSerializer):
    comp_url = serializers.ModelSerializer.serializer_url_field(
        view_name='comp_detail'
    )

    class Meta:
        model = Comp
        fields = ('id', 'comp_detail', 'name', 'units', 'team_formation_url', 'core_items', 'gameplan')