from django.utils import timezone
from rest_framework import serializers

from api.v1.payments.serializers import PaymentSerializers
from api.v1.users.serializers import UserSerializer
from collects.models import Collect
from payments.models import Payment


class CollectsSerializers(serializers.ModelSerializer):
    all_donors = PaymentSerializers(many=True, read_only=True)
    total_number_donors = serializers.SerializerMethodField()
    amount_donate = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Collect
        fields = (
            'id', 'user', 'name', 'reason', 'description',
            'total_goal_amount', 'image', 'date_end',
            'target_amount', 'amount_donate',
            'total_number_donors', 'all_donors'
        )

    def validate(self, value):
        date_end = value.get('date_end', None)
        if date_end < timezone.now():
            raise serializers.ValidationError(
                'Дата окончания сбора не может быть меньше текущей даты'
            )

        return value

    def get_total_number_donors(self, obj):
        total_number_donors = Payment.objects.filter(
            collect=obj
        ).count()
        return total_number_donors

    def get_amount_donate(self, obj):
        donors = Payment.objects.filter(
            collect=obj
        )
        amount_donate = sum([donor.amount for donor in donors])
        return amount_donate


class PatchCollectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Collect
        fields = (
            'name', 'description',
            'total_goal_amount', 'image',
            'target_amount',
        )

    def to_representation(self, instance):
        serializer = CollectsSerializers(instance)
        return serializer.data
