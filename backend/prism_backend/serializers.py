from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from dotenv import load_dotenv
import os

load_dotenv()

User = get_user_model()


class GoogleAuthSerializer(serializers.Serializer):
    id_token = serializers.CharField()

    def validate(self, attrs):
        id_token_str = attrs.get("id_token")
        try:
            # Verify Google's id_token
            google_info = id_token.verify_oauth2_token(
                id_token=id_token_str,
                request=requests.Request(),
                audience=os.getenv("GOOGLE_CLIENT_ID"),
            )

            if "email" not in google_info:
                raise serializers.ValidationError("Invalid Google token.")

            # Check if the user exists
            email = google_info["email"]
            user = User.objects.get(email=email)

            # We'll probably need to set the claims for the user

            # Generate JWT token
            refresh = RefreshToken.for_user(user)

            return {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "id": user.id,
                    "email": user.email,
                },
            }
        except ValueError:
            raise serializers.ValidationError("Invalid token.")
