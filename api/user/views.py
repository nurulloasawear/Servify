from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Users, UserProfile
from rest_framework_simplejwt.tokens import RefreshToken
from .utils.face_utils import get_face_encoding
import numpy as np
import face_recognition
class FaceSignUpView(APIView):
    def post(self, request):
        face_image = request.FILES.get("face_image")
        full_name = request.data.get("full_name")
        phone = request.data.get("phone")

        if not face_image or not full_name or not phone:
            return Response({"error": "Ma'lumotlar to‘liq emas"}, status=400)

        encoding = get_face_encoding(face_image)
        if encoding is None:
            return Response({"error": "Yuz aniqlanmadi"}, status=400)

        # Convert encoding to bytes
        encoding_bytes = encoding.tobytes()

        user = Users.objects.create_user(face_scan=face_image, password=None)
        user.face_encoding = encoding_bytes
        user.save()

        UserProfile.objects.create(user=user, full_name=full_name, phone=phone)

        refresh = RefreshToken.for_user(user)
        return Response({
            "msg": "Yaratildi",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })
class FaceLoginView(APIView):
    def post(self, request):
        face_image = request.FILES.get("face_image")
        if not face_image:
            return Response({"error": "Rasm yuboring"}, status=400)

        new_encoding = get_face_encoding(face_image)
        if new_encoding is None:
            return Response({"error": "Yuz topilmadi"}, status=400)

        users = Users.objects.exclude(face_encoding=None)
        for user in users:
            saved_encoding = np.frombuffer(user.face_encoding, dtype=np.float64)
            result = face_recognition.compare_faces([saved_encoding], new_encoding)
            if result[0]:
                refresh = RefreshToken.for_user(user)
                return Response({
                    "msg": "Kirish muvaffaqiyatli",
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                })

        return Response({"error": "Foydalanuvchi topilmadi"}, status=401)
