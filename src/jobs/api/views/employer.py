from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response



from jobs.api.permissions import IsEmployer, IsJobCreator
from jobs.api.serializers import ApplicantSerializer, DashboardJobSerializer, NewJobSerializer
from jobs.models import Applicant, Job
from .common import CustomPagination


class DashboardAPIView(ListAPIView):
    serializer_class = DashboardJobSerializer
    permission_classes = [IsAuthenticated, IsEmployer]
    pagination_class = CustomPagination

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(user_id=self.request.user.id)


   

# class EditDashboardAPIView(RetrieveUpdateAPIView, CreateAPIView):
#     serializer_class = NewJobSerializer
#     permission_classes = [IsAuthenticated, IsEmployer]
#     parser_classes = [MultiPartParser]

#     def get_queryset(self):
#         return Job.objects.filter(user=self.request.user)

#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)
        
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
        
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', True)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)
    

class JobCreateAPIView(CreateAPIView):
    serializer_class = NewJobSerializer
    permission_classes = [IsAuthenticated, IsEmployer]
    parser_classes = [MultiPartParser]
    
    

class JobUpdateAPIView(UpdateAPIView):
    serializer_class = NewJobSerializer
    permission_classes = [IsAuthenticated, IsEmployer]
    parser_classes = [MultiPartParser]
    lookup_url_kwarg = "job_id"

    def get_queryset(self):
        user = self.request.user
        return Job.objects.filter(user_id=user.id)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
       
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class ApplicantsListAPIView(ListAPIView):
    serializer_class = ApplicantSerializer
    permission_classes = [IsAuthenticated, IsEmployer]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        return Applicant.objects.filter(job__user_id=user.id)


class ApplicantsPerJobListAPIView(ListAPIView):
    serializer_class = ApplicantSerializer
    permission_classes = [IsAuthenticated, IsEmployer, IsJobCreator]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Applicant.objects.filter(job_id=self.kwargs["job_id"]).order_by("id")


class UpdateApplicantStatusAPIView(APIView):
    permission_classes = [IsAuthenticated, IsEmployer]

    def post(self, request, *args, **kwargs):
        applicant_id = kwargs.get("applicant_id")
        status_code = kwargs.get("status_code")
        try:
            applicant = Applicant.objects.select_related("job__user").get(id=applicant_id)
        except Applicant.DoesNotExist:
            data = {"message": "Applicant not found"}
            return JsonResponse(data, status=404)

        if applicant.job.user != request.user:
            data = {"errors": "You are not authorized"}
            return JsonResponse(data, status=403)
        if status_code not in [1, 2]:
            status_code = 3

        applicant.status = status_code
        applicant.comment = request.data.get("comment", "")
        applicant.save()
        data = {"message": "Applicant status updated"}
        return JsonResponse(data, status=200)
