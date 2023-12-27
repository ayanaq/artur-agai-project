from rest_framework import viewsets, status
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly, CanModifyMedicine
from .models import Medicine, Type_of_med
from .serializers import MedicineSerializer, CategoriesSerializer
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from bot.main import echo, bot, dp
import requests
import asyncio


class MedicineAPIViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    lookup_field = 'link'
    permission_classes = [IsAdminOrReadOnly, CanModifyMedicine]

    async def send_telegram_message(self, user, obj):
        # Create a task and execute it asynchronously
        await echo(user, obj)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        amount_to_subtract = request.data.get('amount', 0)

        if amount_to_subtract and instance.amount >= amount_to_subtract:
            instance.amount -= amount_to_subtract
            instance.save()

            # Get user and object information
            user = request.user.username  # Adjust based on your user model
            obj = instance.name  # Adjust based on your model fields

            # Call the send_telegram_message function
            asyncio.run(self.send_telegram_message(user, obj))

            return Response({'message': f'Successfully purchased {amount_to_subtract} units.'})
        else:
            return Response({'error': 'Not enough stock available.'}, status=status.HTTP_400_BAD_REQUEST)
    def create(self, request, *args, **kwargs):
        type_of_med_id = request.data.get('type_of_med_id')

        if type_of_med_id is None:
            return Response({'error': 'type_of_med_id is required for creating Medicine.'},
                            status=status.HTTP_400_BAD_REQUEST)

        type_of_med = Type_of_med.objects.get(pk=type_of_med_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check if the image field is a URL
        image_url = request.data.get('image')
        if image_url:
            # Download the image and save it as a temporary file
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(requests.get(image_url).content)
            img_temp.flush()

            # Save the temporary file to the image field
            serializer.validated_data['image'] = File(img_temp)

        # Adding type_of_med instance to the serializer data before saving
        serializer.validated_data['type_of_med'] = type_of_med

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class CategoriesAPIViewSet(viewsets.ModelViewSet):
    queryset = Type_of_med.objects.all()
    serializer_class = CategoriesSerializer
    lookup_field = 'link'
    permission_classes = [IsAdminOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('link')
        if pk:
            medicines = Medicine.objects.filter(type_of_med__link=pk)
            serializer = MedicineSerializer(medicines, many=True)
            return Response({'medicines': serializer.data})
        else:
            return Response({'error': 'No pk provided'})