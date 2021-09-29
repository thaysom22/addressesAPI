from rest_framework import (generics, status,
    filters, permissions)
from rest_framework.response import Response

from .models import Address
from .serializers import AddressSerializer
from .permissions import CurrentUserIsOwner


class CurrentUserAddressListDestroyCreate(generics.GenericAPIView):
	"""
	View to create address or to list or delete all addresses for current user
	Methods allowed: GET, POST, DELETE
	GET returns list of address instances associated with the current authenticated user
	POST creates a new address instance associated with the current authenticated user
	"""
	search_fields = ['address1', 'address2', 'city', 'region', 'postcode', 'country'] 
	filter_backends = [filters.SearchFilter]
	serializer_class = AddressSerializer
	
	def get_queryset(self):
        """
        Return addresses for currently authenticated user only
        """
        return Address.objects.filter(user=self.request.user)
	
	def get(self, request):
		user_addresses = self.get_queryset()
		if user_addresses.exists():
			serializer = self.get_serializer(user_addresses, many=True)
			return Response(
				serializer.data,
				status=status.HTTP_200_OK)
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	def post(self, request):
		address_data = request.data
		# add the current user to payload for deserialization
		address_data['user'] = request.user
		serializer = self.get_serializer(data=address_data)
		if serializer.is_valid:
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request):
		user_addresses = self.get_queryset()
		if user_addresses.exists():
			serializer = self.get_serializer(user_addresses, many=True)
			count = user_addresses.delete()[0]
			return Response(
				{"count": count, "data": serializer.data}, 
				status=status.HTTP_200_OK)
		return Response(status=status.HTTP_404_NOT_FOUND)


# generic class provides get, put, patch and delete method handlers via built-in mixins
class AddressRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView): 
	queryset = Address.objects.all()
	permissions_classes = [CurrentUserIsOwner|permissions.IsAdminUser]
	serializer = AddressSerializer