from rest_framework import serializers
from .models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    ad = serializers.SlugRelatedField(read_only=True, slug_field="title")
    author = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_first_name = serializers.SlugRelatedField(read_only=True, slug_field="author_first_name")
    author_last_name = serializers.SlugRelatedField(read_only=True, slug_field="author_last_name")
    author_id = serializers.CharField(source='author.id', read_only=True)
    author_image = serializers.CharField(source='author.image', read_only=True)
    ad_id = serializers.CharField(source='ad.id', read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description")


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_id = serializers.CharField(source='author.id', read_only=True)

    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description")