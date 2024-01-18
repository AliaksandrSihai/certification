from django.urls import reverse
from rest_framework.serializers import (ModelSerializer, SerializerMethodField,
                                        ValidationError)

from retail_chain.models import RetailChain


class RetailChainSerializer(ModelSerializer):
    """Сериалайзер для модели RetailChain"""

    supplier_url = SerializerMethodField(read_only=True)

    def get_supplier_url(self, instance):
        if instance.supplier:
            return self.context["request"].build_absolute_uri(
                reverse("retail_chain:retailchain-detail", args=[instance.supplier.pk])
            )
        else:
            return "Поставщик отсутствует"

    class Meta:
        model = RetailChain
        fields = (
            "title",
            "supplier",
            "supplier_url",
            "supplier_debt",
            "contacts",
            "products",
        )
        depth = 1

    def update(self, instance, validated_data):
        if validated_data.get("supplier_debt") is not None:
            raise ValidationError(
                "Обновление через API поля «Задолженность перед поставщиком» запрещено!"
            )
        return super().update(instance, validated_data)
