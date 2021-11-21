from rest_framework.serializers import ModelSerializer
from .models import File


class FileSerializer(ModelSerializer):

    class Meta:
        model=File

        fields=['id','file_name','file_type','file_url','date_created']

    