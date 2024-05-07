from django.contrib.auth.models import User
from rest_framework import generics, decorators, response
from .serializers import UserSerializer


@decorators.api_view(['GET'])
def get_routes(request):
    routes = [
        'GET /api',
        '-------------------------------------------------------------------------------------------------------------',
        'Действия с пользователями',
        'GET /api/users - список пользователей',
        'GET /api/users/:user_id - посмотреть данные пользователя user_id',
        'POST /api/users/create_user - создать пользователя',
        'POST /api/users/:user_id/delete_user - удалить пользователя user_id',
        '-------------------------------------------------------------------------------------------------------------',
        'Действия с героями',
        'GET /api/heroes_list - список героев',
        'POST /api/heroes_list/create_hero - создать героя',
        'GET /api/heroes_list/:hero_id - посмотреть детали героя hero_id',
        'DELETE /api/heroes_list/:hero_id/delete_hero - удалить героя hero_id',
        'PUT /api/heroes_list/:hero_id/level_up - поднять уровень герою hero_id',
        'GET /api/heroes_list/:hero_id/inventory - посмотреть инвентарь героя hero_id',
        'DELETE /api/heroes_list/:hero_id/remove_item/:item_id - удалить предмет item_id из инвентаря героя '
        'hero_id',
        '-------------------------------------------------------------------------------------------------------------',
        'Действия с предметами',
        'GET /api/items_list - список всех предметов',
        'POST /api/items_list/create_item - создать предмет',
        'GET /api/items_list/:item_id - посмотреть описание предмета item_id',
        'DELETE /api/items_list/:item_id/delete_item - удалить предмет item_id',
        'PUT /api/items_list/:item_id/give_item_to_hero/:hero_id - дать предмет item_id герою hero_id',
    ]
    return response.Response(routes)


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
