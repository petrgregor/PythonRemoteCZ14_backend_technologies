from rest_framework import serializers
from viewer.models import Movie, Person, Comment


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        #fields = '__all__'
        fields = ['title', 'title_cz', 'year', 'description']


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        #fields = '__all__'
        exclude = ['id', 'created', 'updated']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        #fields = '__all__'
        exclude = ['id', 'created', 'updated']
