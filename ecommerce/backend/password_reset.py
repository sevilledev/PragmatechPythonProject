from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .serializers import *


class ResetPasswordEmail(APIView):
    serializer_class = EmailSerializers
    def post(self,request):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        email = serializers.validated_data['email']
        check_user = User.objects.filter(email=email)
        if check_user.count() > 0:
            get_user = User.objects.get(email=email)
            create_verify = UserVerify.objects.get_or_create(user_id=get_user.id)

            subject = "Mail For Password Reset"
            message = f"Go to given link below: \n\n http://127.0.0.1:8000/check_email?token={create_verify[0].token}"
            recepient = f"{get_user.email}"
            send_mail(subject,message,settings.EMAIL_HOST_USER,[recepient],fail_silently=True)

            return Response({'success':'Email has sent!'})
        return Response({'data':'None'})

