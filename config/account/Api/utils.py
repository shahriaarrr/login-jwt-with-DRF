from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    print(refresh)  
    print(str(refresh.access_token))
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh),
        }