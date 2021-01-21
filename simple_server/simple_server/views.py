from django.http import JsonResponse
from .tweet_dumper import get_all_tweets

#next step is to replace culk with data from a post
#request.POST['name_of_user']
def data_view(request):
    temp = get_all_tweets("Mr2dayman")
    return JsonResponse({'lines':temp})