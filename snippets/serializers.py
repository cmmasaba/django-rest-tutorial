from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from users.models import CustomUserModel as User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    # To bypass the lookup_field error, explicitly define the url this way
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', format='html')
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url' 'id', 'highlight', 'title', 'code', 
                  'linenos', 'language', 'style', 'owner']