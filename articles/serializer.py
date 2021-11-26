from rest_framework.serializers import ModelSerializer

from .models import Article, Author

class AuthorSerializer(ModelSerializer):
    
    class Meta:
        model = Author
        fields = ('name', 'email')

class ArticleSerializer(ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('title', 'content')
    
    def create(self, validated_data):
        #auther_data = validated_data.pop('author')
        #author = Author.objects.create(**auther_data)
        article = Article.objects.create(**validated_data)
        return article
    
    