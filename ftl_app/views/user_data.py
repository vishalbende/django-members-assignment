from utility.utils import CreateRetrieveUpdateViewSet
from ftl_app.models import User
from django.http import JsonResponse


class FTLTestView(CreateRetrieveUpdateViewSet):

    def list(self, request, *args, **kwargs):

        # fetch users and its related activities in one query
        user_data = User.objects.prefetch_related('user').all()

        # get response data
        response_data = self.transform_list_user(user_data)
        response_dict = {'ok': True, 'members': response_data}

        # return ok response
        return JsonResponse(response_dict)

    # transform single user
    def transform_single_user(self, instance):
        resp_dict = dict()
        resp_dict['id'] = instance.id
        resp_dict['real_name'] = instance.real_name()
        resp_dict['tz'] = instance.tz

        # get all activities of current user
        activity_data = instance.user.all()
        activity_periods = self.transform_list_activity(activity_data)
        resp_dict['activity_periods'] = activity_periods

        return resp_dict

    # transform single activity
    def transform_single_activity(self, instance):
        resp_dict = dict()
        resp_dict['start_time'] = instance.start_time.strftime("%b %d %Y %I:%M%p")
        resp_dict['end_time'] = instance.end_time.strftime("%b %d %Y %I:%M%p")
        return resp_dict

    # map and get list of users
    def transform_list_user(self, data):
        return list(map(self.transform_single_user, data))

    # map and get list of activities
    def transform_list_activity(self, data):
        return list(map(self.transform_single_activity, data))
