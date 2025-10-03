from rest_framework import serializers

from payments.models import Payment


class PaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = (
            'id', 'collect', 'date', 'amount', 'is_anonymous'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.is_anonymous:
            data['amount'] = None
        return data
