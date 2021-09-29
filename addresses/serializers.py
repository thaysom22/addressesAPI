from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Address
		fields = ['url', 'user', 'address1', 'address2',
            'city', 'region', 'postcode', 'country', 'created_at']
		read_only_fields = ['url', 'user', 'created_at']