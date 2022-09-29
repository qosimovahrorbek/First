from asyncio.base_subprocess import ReadSubprocessPipeProto
from rest_framework.decorators import api_view
from main.models import *
from .serializer import *
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework import authentication, permissions


@api_view(['POST'])
def Register(request):
    try:
        username = request.data['username']
        password = request.data['password']
        usrs = User.objects.create_user(username=username, password=password)
        token = Token.objects.create(user=usrs)
        data = {
            'username' : username,
            'user_id' : usrs.id,
            'token' : token.key,
        }
        return Response(data)
    except Exception as err:
        return Response({"error": f'{err}'})

@api_view(['POST'])
def Login(request):
    try:
        username = request.data['username']
        passsword = request.data['password']
        try:
            usrs = User.objects.get(username=username)
            if usrs is not None:
                token, created = Token.objects.get_or_create(user=usrs)
                data = {
                    'username' : username,
                    'user_id' : usrs.id,
                    'token' : token.key,
                }
            else:
                message = 'Username yoki Password notugri!'
                data = {
                    'message' : message,
                }
        except:
            message = 'Bunday user mavjud emas!'
            data = {
                'message' : message,
            }
        return Response(data)
    except  Exception as err:
        return Response({"error" : f'{err}'}, 'HTTP_500_INTERNAL_SERVER_ERROR')

class CreateUser(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        types = request.POST['types']
        date_born = request.POST['date_born']
        img = request.POST['img']
        query = User.objects.create(username=username, password=password, types=types, date_born=date_born,img=img)
        return Response(UserSerializer(query).data)


class CreateMusic(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        name = request.POST['name']
        musicant = request.POST['musicant']
        img = request.POST['img']
        music = request.POST['music']
        img = request.POST['img']
        min = request.POST['min']
        sec = request.POST['sec']
        query = Music.objects.create(name=name, musicant=musicant, music=music, min=min,img=img, sec=sec)
        return Response(MusicSerializer(query).data)


class CreateCard(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(request):
        user = request.user.is_anonymous
        card = []
        card_number = 0
        total = 0
        user = request.POST.get('user')
        music = request.POST.get('music')
        if user:
            card = []
        else:
            card = Card.objects.create(music=music,user=user)
        data = {
            'music' : music.name,
            'author' : music.musicant.username
        }
        return Response(CardSerializer(data))

class DeleteCard(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def Delete(request, pk):
        Card.objects.get(id=pk).delete()
        return Response('done')


class GetAllMusic(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(request):
        all = Music.objects.all()
        query = MusicSerializer(all)
        return Response(MusicSerializer(query, many=True).data)

class AuthorMusics(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(request, pk):
        get = Music.objects.filter(musicant_id=pk)
        quontity = 0
        for i in get:
            quontity +=1
        query  =MusicSerializer(quontity)
        return Response({"data" : query})

class AllUsers(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(request, pk):
        get = User.objects.all()
        quontity = 0
        for i in get:
            quontity +=1
        query  =MusicSerializer(quontity)
        return Response({"data" : query})
