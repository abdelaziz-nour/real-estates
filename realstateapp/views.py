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
from django.forms.models import model_to_dict


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# register if 1234 names == 1234 in register && NN== registry NN
# def for rent by city and state and price
# def for sale by city and state and price
# def for getting users estate
# def for getting estate by city
# def user delete his add
# + admin should accept add before appear


@api_view(['post'])
def register(request):

    serializer = RegisterSerializer(data=request.data)

    try:
        if serializer.is_valid(raise_exception=True):

            info_user = UserInfo(
                firstName=request.data["firstName"],
                secondName=request.data["secondName"],
                thirdName=request.data["thirdName"],
                forthName=request.data["forthName"],
                nationalID=request.data["nationalID"],
                phone=request.data["phone"],
                state=request.data["state"],
                city=request.data["city"],
            )

        else:
            return Response("wrong data entries")

        if info_user:
            registry = CivilRegistry.objects.filter(
                firstName=request.data["firstName"],
                secondName=request.data["secondName"],
                thirdName=request.data["thirdName"],
                forthName=request.data["forthName"],
                nationalID=request.data["nationalID"],
            )
            if registry:

                user = User.objects.create_user(
                    email=request.data["email"],
                    username=request.data["phone"],
                    password=request.data["password"],
                )
                try:
                    info_user.user = user
                    info_user.save()
                    token = Token.objects.create(user=user)
                    return custom_response(
                        data={
                            'token': token.key,
                            'info_user': model_to_dict(info_user)
                        },
                        success=True,
                    )

                except BaseException as exception:
                    logging.warning(f"Exception Name: {type(exception).__name__}")
                    logging.warning(f"Exception Desc: {exception}")
                    return custom_response(message="User did not created")

            else:
                return custom_response(message="User Data Not Found In Civilian Registry")

    except BaseException as exception:
        logging.warning(f"Exception Name: {type(exception).__name__}")
        logging.warning(f"Exception Desc: {exception}")


@api_view(['POST'])
def login(request):
    try:
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            token = Token.objects.get(user_id=user)
            user_info = model_to_dict(UserInfo.objects.get(user=user))
            user_info['email'] = model_to_dict(user).get("email")

            return custom_response(
                data={'token': token.key, "userInfo": user_info},
                success=True
            )
        else:
            return custom_response(message="User Not Found")
    except BaseException as exception:
        logging.warning(f"Exception Name: {type(exception).__name__}")
        logging.warning(f"Exception Desc: {exception}")
        return custom_response(message="Authentication Failure")


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def adding_real_estate(request):
    if (request.user.is_authenticated):
        try:
            current_user = User.objects.get(id=request.user.id)
            user_data = UserInfo.objects.get(user=current_user)
            newRealEstate = RealEstate(
                advertiser=current_user,
                title=request.data["title"],
                description=request.data["description"],
                nationalID=user_data.nationalID,
                facilitiesNum=request.data["facilitiesNum"],
                type=request.data["type"],
                operation=request.data["operation"],
                state=request.data["state"],
                city=request.data["city"],
                location=request.data["location"],
                price=request.data["price"],
                approval=request.data["approval"],
            )

            newRealEstate.save()
            for image in request.data.getlist('images'):
                Image(realEstate=newRealEstate, image=image, type="View").save()

            for image in request.data.getlist('ownerShipProof'):
                Image(realEstate=newRealEstate, image=image, type="Proof").save()

            return custom_response(success=True)

        except BaseException as exception:
            logging.warning(f"Exception Name: {type(exception).__name__}")
            logging.warning(f"Exception Desc: {exception}")

    else:
        return custom_response(message="Authentication Failure")


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def default_filtered_estate(request):
    current_user = User.objects.get(id=request.user.id)
    user_data = UserInfo.objects.get(user=current_user)
    user_state = user_data.state
    user_city = user_data.city
    filter_type_and_location = RealEstate.objects.filter(
        approval="Accepted", state=user_state, city=user_city, type=request.data["type"],)
    data = []
    for x in filter_type_and_location:
        field = {
            "image1": x.image1,
            "title": x.title,
            "price": x.price,
            "facilitiesNum": x.facilitiesNum,
        }
        data.append(field)
    return Response(data)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def type_filtered_estate(request):
    filter_type_and_location = RealEstate.objects.filter(
        approval="Accepted", type=request.data["type"],)
    data = []
    for x in filter_type_and_location:
        field = {
            "image1": x.image1,
            "title": x.title,
            "price": x.price,
            "facilitiesNum": x.facilitiesNum,
        }
        data.append(field)
    return Response(data)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def city_filtered_estate(request):
    filter_type_and_location = RealEstate.objects.filter(
        approval="Accepted", city=request.data["city"],)
    data = []
    for x in filter_type_and_location:
        field = {
            "image1": x.image1,
            "title": x.title,
            "price": x.price,
            "facilitiesNum": x.facilitiesNum,
        }
        data.append(field)
    return Response(data)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def state_filtered_estate(request):
    filter_type_and_location = RealEstate.objects.filter(
        approval="Accepted",
        state=request.data["state"]
    )
    data = []
    for x in filter_type_and_location:
        field = {
            "image1": x.image1,
            "title": x.title,
            "price": x.price,
            "facilitiesNum": x.facilitiesNum,
        }
        data.append(field)
    return Response(data)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def city_state_price(request):
    current_user = User.objects.get(id=request.user.id)
    user_data = UserInfo.objects.get(user=current_user)
    user_state = user_data.state
    user_city = user_data.city
    filter_type_and_location = RealEstate.objects.filter(
        state=user_state,
        city=user_city,
        approval="Accepted",
        type=request.data["type"],
        price=request.data["price"]
    )

    data = []
    for x in filter_type_and_location:
        field = {
            "image1": x.image1,
            "title": x.title,
            "price": x.price,
            "facilitiesNum": x.facilitiesNum,
        }
        data.append(field)
    return Response(data)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['get'])
def get_real_estates(request):
    filter_type_and_location = RealEstate.objects.all()

    data = []
    for realEstate in filter_type_and_location:

        images = Image.objects.filter(realEstate=realEstate)

        field = {
            "id": realEstate.pk,
            "advertiser": realEstate.advertiser.id,
            "nationalID": str(realEstate.nationalID),
            "title": realEstate.title,
            "price": str(realEstate.price),
            "facilitiesNum": str(realEstate.facilitiesNum),
            "description": realEstate.description,
            "type": realEstate.type,
            "operation": realEstate.operation,
            "state": realEstate.state,
            "city": realEstate.city,
            "location": realEstate.location,
            "approval": realEstate.approval,
            "images": [{"url": str(image.image), "type": image.type} for image in images],
        }
        data.append(field)

    return custom_response(data={'data': data}, success=True)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def my_real_estate(request):

    current_user = User.objects.get(id=request.user.id)
    filter_type_and_location = RealEstate.objects.filter(advertiser=current_user)

    data = []
    for x in filter_type_and_location:
        field = {
            "title": x.title,
            "price": x.price,
            "facilitiesNum": x.facilitiesNum,
            "type": x.type,
            "operation": x.operation,
            "state": x.state,
            "city": x.city,
            "location": x.location,
            "description": x.description,
            "approval": x.approval,
            "image1": x.image1,
            "image2": x.image2,
            "image3": x.image3,
        }
        data.append(field)
    return Response(data)


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def delete_my_estate(request):
    current_user = User.objects.get(id=request.user.id)
    filter_my_estates = RealEstate.objects.filter(advertiser=current_user)
    filter_my_estates.get(id=request.data["id"]).delete()
    return Response("Real estate successfully deleted")


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def accept_real_estate(request):
    estates = RealEstate.objects.get(id=request.data["id"])
    estates.approval = "Accepted"
    estates.save()
    return Response("Accepted")


@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['post'])
def reject_real_estate(request):
    estates = RealEstate.objects.get(id=request.data["id"])
    estates.approval = "Rejected"
    estates.save()
    return Response("Rejected")
