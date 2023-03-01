import random
import string

from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from sslcommerz_lib import SSLCOMMERZ

from accounts.models import Student
from course.api.v1.serializers import CourseSerializer, CourseCategorySerializer, VideoSerializer, BlogSerializer, \
    CommentSerializer, CourseListCreateSerializer
from course.models import Course, CourseCategory, Video, Blog, Comment

# Course CRUD apis
from teach_and_learn.settings import SSL_COMMERZ_STORE_ID, SSL_COMMERZ_SANDBOX, SSL_COMMERZ_STORE_PASS, HOST_URL


class CourseListCreateApiView(ListCreateAPIView):
    serializer_class = CourseListCreateSerializer

    def get_queryset(self):
        search_text = self.request.GET.get('search_text', None)
        return Course.objects.filter(title__icontains=search_text) if search_text else Course.objects.all()


class CourseRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "id"


# noinspection PyMethodMayBeStatic
class CourseJoinApi(APIView):
    def get(self, request, course_id):
        try:
            student = Student.objects.get_or_create(user=request.user)[0]
            Course.objects.get(id=course_id).student.add(student)
            context = {
                "result": "Successfully joined"
            }
            status_code = status.HTTP_200_OK
        except (Exception,) as e:
            context = {
                "result": "Something went wrong",
                "error": str(e)
            }
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(context, status=status_code)


class PersonalCoursesListAPIView(APIView):
    serializer_class = CourseSerializer

    def get(self, request):
        created_courses = Course.objects.filter(teacher=request.user.teacher)
        taken_courses = Course.objects.filter(student=request.user.student)
        return Response({
            'createdCourses': CourseListCreateSerializer(created_courses, many=True).data,
            'takenCourses': CourseListCreateSerializer(taken_courses, many=True).data
        })


# CourseCategorySerializer CRUD apis

class CourseCategoryListCreateApiView(ListCreateAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer


class CourseCategoryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
    lookup_field = "id"


# Video CRUD apis

class VideoListCreateApiView(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = "id"


# Blog CRUD apis

class BlogListCreateApiView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"


# Comment CRUD apis

class CommentListCreateApiView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"


# SSL Commerz

SSL_COMMERZ_CATEGORY = {
    'program_purchase': 'program_purchase'
}


# noinspection PyMethodMayBeStatic
class SSLCommerzSessionAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        settings = {'store_id': SSL_COMMERZ_STORE_ID, 'store_pass': SSL_COMMERZ_STORE_PASS,
                    'issandbox': bool(SSL_COMMERZ_SANDBOX == 'True')}

        tran_id = 'teach'.join(
            random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(9))
        data = request.data
        ssl = SSLCOMMERZ(settings)

        user = request.user
        username = user.username
        user_mail = "sauravpaul.sunnny@gmail.com"
        user_phone = "+8801781427983"
        product_id = data.get('product_id')
        category = data.get('category')

        post_body = dict()
        post_body['total_amount'] = 199
        post_body['currency'] = "BDT"
        post_body['tran_id'] = tran_id
        post_body['success_url'] = f"{HOST_URL}api/course/v1/product-redirect/?status=success"
        post_body['fail_url'] = f"{HOST_URL}api/course/v1/product-redirect//?status=fail"
        post_body['cancel_url'] = f"{HOST_URL}api/course/v1/product-redirect/?status=cancel"
        post_body['emi_option'] = 0
        post_body['cus_name'] = username
        post_body['cus_email'] = user_mail
        post_body['cus_phone'] = user_phone
        post_body['cus_add1'] = "customer address"
        post_body['cus_city'] = "Dhaka"
        post_body['cus_country'] = "Bangladesh"
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = 1
        post_body['product_name'] = ""
        post_body['product_category'] = category
        post_body['product_profile'] = "general"
        post_body['ipn_url'] = f"{HOST_URL}api/billing/v1/ipn-verify/"
        post_body['value_a'] = ''
        post_body['value_c'] = request.headers['Origin']

        if SSL_COMMERZ_CATEGORY.get('program_purchase') == category:
            validated = True
            if product_id:
                try:
                    obj = Course.objects.get(id=product_id)
                    post_body['total_amount'] = obj.price
                    post_body['product_name'] = "Program"
                    post_body['value_a'] = obj.id,
                    post_body['value_b'] = self.request.user.id

                except (Course.DoesNotExist,) as e:
                    validated = False
                    print(e)
            else:
                validated = False

            if not validated:
                print('not validated')

        response = ssl.createSession(post_body)

        print(post_body)

        return Response(response)


# noinspection PyMethodMayBeStatic
class IPNVerifyAPIView(APIView):

    def program_purchase_process(self, user, data):
        program_data = {'program': data.get('value_a')}
        #
        # logger.info(f"program data {program_data}")
        #
        # serializer = PurchaseProgramSerializer(data=program_data, context={
        #     "way": "money"})
        # serializer.is_valid(raise_exception=True)
        #
        # program = serializer.validated_data.get('program')
        # # TODO SOLVE THE ISSUE PERMANENTLY
        # with TempSignalDisconnector(post_save, '__all__', Transaction):
        #     Transaction.objects.create(
        #         user=user, category='program_purchase', type='debit', amount=program.cost,
        #         extra=json.dumps({'program_id': program.id, 'payment_response': data})
        #     )
        # user.billingprofile.purchased_programs.add(program)

    def post(self, request, *args, **kwargs):
        settings = {'store_id': SSL_COMMERZ_STORE_ID, 'store_pass': SSL_COMMERZ_STORE_PASS,
                    'issandbox': bool(SSL_COMMERZ_SANDBOX == 'True')}

        data = request.data
        # tran_id = data.get('tran_id', None)
        # val_id = data.get('val_id', None)
        # amount = data.get('amount', None)
        # sslcz = SSLCOMMERZ(settings)
        # post_body = {k: v[0] for k, v in dict(data).items()}
        # post_body["val_id"] = val_id
        #
        # # print(post_body)
        # # logger.info(post_body)
        #
        # # logger.info(f"okkkkk, {post_body.get('val_id')} {data.get('val_id')}")
        # # logger.info(f"okkkkk2, {post_body.get('value_a')} {data.get('value_a')}")
        # # logger.info(val_id)
        #
        # if sslcz.hash_validate_ipn(post_body):
        #     response = sslcz.validationTransactionOrder(post_body['val_id'])
        #     if response['status'] == "VALID" or response['status'] == "VALIDATED":
        #         try:
        #             user_session_info = TransactionSessionInfo.objects.get(tran_id=tran_id)
        #             user = user_session_info.user
        #             user_session_info.status = "Approved"
        #             user_session_info.save()
        #
        #             self.program_purchase_process(user=user, data=post_body)
        #
        #             logger.info("hamaisi", user)
        #         except (Exception,) as e:
        #             print(e)
        #             logger.info('sslcz ipn verify ,', str(e))
        #
        #     # logger.info(response)
        # else:
        #     logger.info("Hash verification failed")

        return Response(request.data)


@method_decorator(csrf_exempt, name='dispatch')
class ProductRedirectView(View):
    def post(self, request):
        product_id = request.POST.get('value_a', None)
        user_id = request.POST.get('value_b', None)
        request_origin = request.POST.get('value_c', None)
        print(product_id, user_id)

        _status = request.GET.get('status', None)

        if _status == "success":
            student = Student.objects.get_or_create(user_id=user_id)[0]
            print(student)
            Course.objects.get(id=product_id).student.add(student)

        url = f"{request_origin}/course/{product_id}"
        return redirect(url)
