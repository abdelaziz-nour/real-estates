import logging
from rest_framework.response import Response

from realstateapp.helpers import custom_response
from .serializer import *
from .models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import *
from rest_framework.decorators import *
from rest_framework.permissions import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# register if 1234 names == 1234 in register && NN== registry NN
# def for rent by city and state and price
# def for sale by city and state and price
# def for getting users estate
# def for getting estate by city
# def user delete his add
# + admin should accept add befor apear


@api_view(['post'])
def register(request):

    serializer = RegisterSerializer(data=request.data)
    print("test")
    try:
        if serializer.is_valid(raise_exception=True):

            info_user = userInfo(
                first_name=request.data["first_name"],
                second_name=request.data["second_name"],
                thired_name=request.data["thired_name"],
                forth_name=request.data["forth_name"],
                national_number=request.data["national_number"],
                phone=request.data["phone"],
                email=request.data["email"],
                username=request.data["username"],
                password=request.data["password"],
                state=request.data["state"],
                city=request.data["city"],
            )

        else:
            return Response("wrong data entries")

        if info_user:
            registry = civil_registry.objects.filter(
                first_name=request.data["first_name"],
                second_name=request.data["second_name"],
                thired_name=request.data["thired_name"],
                forth_name=request.data["forth_name"],
                national_number=request.data["national_number"],
            )
            if registry:
                user = User.objects.create_user(
                    email=request.data["email"],
                    username=request.data["username"],
                    password=request.data["password"],
                )
                info_user.user = user
                info_user.save()
                token = Token.objects.create(user=user)
                return Response(token.key)
            else:
                return Response("no matching data in database")
    except BaseException as exception:
        logging.warning(f"Exception Name: {type(exception).__name__}")
        logging.warning(f"Exception Desc: {exception}")


@api_view(['POST'])
def login(request):
    username = request.data["username"]
    password = request.data["password"]
    try:
        user = authenticate(username=username, password=password)
        if user is not None:
            token = Token.objects.get(user_id=user)
            return custom_response(data={'token': token.key})
        else:
            return custom_response(error="NOT_FOUND", message="User Not Found")
    except:
        return custom_response(error="AUTH_FAILURE", message="Authentication Failure")


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def adding_realstate(request):
    current_user = User.objects.get(id=request.user.id)
    user_data = userInfo.objects.get(user=current_user)
    added_estate = real_estate(
        addvertiser=current_user,
        estate_name=request.data["estate_name"],
        estate_description=request.data["estate_description"],
        owner_national_number=user_data.national_number,
        estate_type=request.data["estate_type"],
        number_of_facilities=request.data["number_of_facilities"],
        state=request.data["state"],
        city=request.data["city"],
        location=request.data["location"],
        authentication_image=request.FILES["authentication_image"],
        estate_image1=request.FILES["estate_image1"],
        estate_image2=request.FILES["estate_image2"],
        estate_image3=request.FILES["estate_image3"],
        map_location=request.data["map_location"],
        price=request.data["price"],
    )
    added_estate.save()
    return Response("Done")


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def defalute_filttered_estate(request):
    current_user = User.objects.get(id=request.user.id)
    user_data = userInfo.objects.get(user=current_user)
    user_state = user_data.state
    user_city = user_data.city
    filtter_type_and_location = real_estate.objects.filter(
        estate_status="Accepted", state=user_state, city=user_city, estate_type=request.data["estate_type"],)
    data = []
    for x in filtter_type_and_location:
        field = {
            "estate_image1": x.estate_image1,
            "estate_name": x.estate_name,
            "price": x.price,
            "number_of_facilities": x.number_of_facilities,
        }
        data.append(field)
    return Response(data)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def type_filttered_estate(request):
    filtter_type_and_location = real_estate.objects.filter(
        estate_status="Accepted", estate_type=request.data["estate_type"],)
    data = []
    for x in filtter_type_and_location:
        field = {
            "estate_image1": x.estate_image1,
            "estate_name": x.estate_name,
            "price": x.price,
            "number_of_facilities": x.number_of_facilities,
        }
        data.append(field)
    return Response(data)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def city_filttered_estate(request):
    filtter_type_and_location = real_estate.objects.filter(
        estate_status="Accepted", city=request.data["city"],)
    data = []
    for x in filtter_type_and_location:
        field = {
            "estate_image1": x.estate_image1,
            "estate_name": x.estate_name,
            "price": x.price,
            "number_of_facilities": x.number_of_facilities,
        }
        data.append(field)
    return Response(data)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def state_filttered_estate(request):
    filtter_type_and_location = real_estate.objects.filter(
        estate_status="Accepted", state=request.data["state"],)
    data = []
    for x in filtter_type_and_location:
        field = {
            "estate_image1": x.estate_image1,
            "estate_name": x.estate_name,
            "price": x.price,
            "number_of_facilities": x.number_of_facilities,
        }
        data.append(field)
    return Response(data)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def city_state_price(request):
    current_user = User.objects.get(id=request.user.id)
    user_data = userInfo.objects.get(user=current_user)
    user_state = user_data.state
    user_city = user_data.city
    filtter_type_and_location = real_estate.objects.filter(
        estate_status="Accepted", state=user_state, city=user_city, estate_type=request.data["estate_type"], price=request.data["price"])
    data = []
    for x in filtter_type_and_location:
        field = {
            "estate_image1": x.estate_image1,
            "estate_name": x.estate_name,
            "price": x.price,
            "number_of_facilities": x.number_of_facilities,
        }
        data.append(field)
    return Response(data)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['get'])
def getting_states(request):
    filtter_type_and_location = real_estate.objects.all()
    data = []
    for x in filtter_type_and_location:
        field = {
            "addvertiser": x.addvertiser.username,
            "owner_national_number": x.owner_national_number,
            "estate_name": x.estate_name,
            "price": x.price,
            "number_of_facilities": x.number_of_facilities,
            "estate_description": x.estate_description,
            "estate_type": x.estate_type,
            "state": x.state,
            "city": x.city,
            "location": x.location,
            "map_location": x.map_location,
            "estate_status": x.estate_status,
            "estate_image": x.estate_image1,
            "estate_image2": x.estate_image2,
            "estate_image3": x.estate_image3,
        }
        data.append(field)
    return Response(data)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def getting_my_estate(request):
    current_user = User.objects.get(id=request.user.id)
    filtter_type_and_location = real_estate.objects.filter(
        addvertiser=current_user)
    data = []
    for x in filtter_type_and_location:
        field = {
            "estate_name": x.estate_name,
            "price": x.price,
            "number_of_facilities": x.number_of_facilities,
            "estate_type": x.estate_type,
            "state": x.state,
            "city": x.city,
            "location": x.location,
            "estate_description": x.estate_description,
            "estate_status": x.estate_status,
            "estate_image1": x.estate_image1,
            "estate_image2": x.estate_image2,
            "estate_image3": x.estate_image3,
        }
        data.append(field)
    return Response(data)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def delete_my_estate(request):
    current_user = User.objects.get(id=request.user.id)
    filtter_my_estates = real_estate.objects.filter(addvertiser=current_user)
    filtter_my_estates.get(id=request.data["id"]).delete()
    return Response("estate succefully deleted")


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def accept_estate(request):
    estates = real_estate.objects.get(id=request.data["id"])
    estates.estate_status = "Accepted"
    estates.save()
    return Response("Accepted")


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def reject_estate(request):
    estates = real_estate.objects.get(id=request.data["id"])
    estates.estate_status = "Rejected"
    estates.save()
    return Response("Rejected")
