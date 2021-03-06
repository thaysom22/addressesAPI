from rest_framework import (generics, status,
    filters)
from rest_framework.response import Response
from .models import Address
from .serializers import AddressSerializer
from .permissions import CurrentUserIsOwnerOrAdmin


class CurrentUserAddressListDestroyCreate(generics.GenericAPIView):
    """
    View to create address or to list or delete addresses belonging to current user
    with optional request query parameter filtering
    Methods allowed: GET, POST, DELETE
    """
    search_fields = ['address1', 'address2', 'city', 'region', 'postcode', 'country']
    filter_backends = [filters.SearchFilter]
    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
    
    def get(self, request):
        """
        Returns (optionally filtered) list of address instances associated with the 
        current authenticated user
        """
        user_addresses = self.get_queryset()
        filtered_addresses = self.filter_queryset(user_addresses)
        if filtered_addresses.exists():
            serializer = self.get_serializer(filtered_addresses, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        """
        Creates a new address instance associated with the current authenticated user
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # add the current user before creating object in DB
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        Deletes all (or optionally filtered subset) address instances 
        associated with the current authenticated user
        """ 
        user_addresses = self.get_queryset()
        filtered_addresses = self.filter_queryset(user_addresses)
        if filtered_addresses.exists():
            serializer = self.get_serializer(filtered_addresses, many=True)
            count = filtered_addresses.delete()[0]
            return Response(
                {"count": count, "data": serializer.data}, 
                status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class AddressRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete single address instances identified
    by primary key
    Methods allowed: GET, PUT, PATCH, DELETE
    Generic class provides get, put, patch and delete method handler 
    implementations via built-in mixins
    """ 
    queryset = Address.objects.all()
    permission_classes = [CurrentUserIsOwnerOrAdmin]
    serializer_class = AddressSerializer
    search_fields = ['address1', 'address2', 'city', 'region', 'postcode', 'country'] 
