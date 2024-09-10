from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer


class Endpoint(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = ["advocates", "advocates/:username"]
        return Response(data)


class AdvocateList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get("query")
        if query:
            advocates = Advocate.objects.filter(
                Q(username__icontains=query) | Q(bio__icontains=query)
            )
        else:
            advocates = Advocate.objects.all()
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvocateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdvocateDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        advocate = get_object_or_404(Advocate, username=username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def put(self, request, username):
        advocate = get_object_or_404(Advocate, username=username)
        serializer = AdvocateSerializer(advocate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        advocate = get_object_or_404(Advocate, username=username)
        advocate.delete()
        return redirect("advocate_list")


class CompanyList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get("query")
        if query:
            companies = Company.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        else:
            companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        advocate = get_object_or_404(Advocate, username=username)
        advocate.delete()
        return redirect("company_list")
