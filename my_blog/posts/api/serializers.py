# Los serializers indican los datos de salida y tambien datos de entrada.

from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "description",
            "order",
            "created_at"
        ]
        #Con "__all__" podemos traer todos los campos
