from django.http import JsonResponse
from .tweet_dumper import get_all_tweets
from django.views.decorators.csrf import csrf_exempt

# next step is to replace culk with data from a post
# request.POST['name_of_user']
@csrf_exempt
def data_view(request):
    temp = get_all_tweets("Mr2dayman")
    return JsonResponse({"Hate Speech": "25%"})
