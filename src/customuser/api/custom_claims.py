from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from rest_framework.response import Response

from .serializers import UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    # user = UserSerializer(many=True)
    
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)

    #     # Add custom claims
    #     # token["user"] = UserSerializer(user, many=False).data
    #     token["role"]=user.role
    #     token["message"]="testseeion"
    #     print(token)
    #     print(type(token))
    #     # print(str(token['role']),token['user'])
    #     return token
    
    def validate(self, attrs):
        # data = UserSerializer(user, many=False).data
        # Add your extra responses here
        data = super().validate(attrs)
    
        refresh= self.get_token(self.user)
        data['email']=self.user.email
        data['refresh']= str(refresh)
        data['access']= str(refresh.access_token)
        data['role']=self.user.role
        return data



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        # you need to instantiate the serializer with the request data
        # serializer=MyTokenObtainPairSerializer
        serializer = self.serializer_class(data=request.data)
        # you must call .is_valid() before accessing validated_data
        serializer.is_valid(raise_exception=True)  

        # get access and refresh tokens to do what you like with
        access = serializer.validated_data.get("access", None)
        refresh = serializer.validated_data.get("refresh", None)
        email = serializer.validated_data.get("email", None)
        role = serializer.validated_data.get("role", None)


        # build your response and set cookie
        if access is not None:
            response = Response({"access": access, "refresh": refresh, "email": email,"role":role}, status=200)
            response.set_cookie('token', access, httponly=True)
            response.set_cookie('refresh', refresh, httponly=True)
           
            return response


        return Response({"Error": "Something went wrong"}, status=400)

