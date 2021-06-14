from analytics.serializers import UserSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'response_message': "successful",
        'user': UserSerializer(user, context={'request': request}).data
    }