from commons.utils.pagination import create_pagination_url
from commons.utils.response import OK
from commons.utils.http_error import BadRequest
from django.views.decorators.http import require_http_methods
import json
from videos.models import Video
from videos.tasks import fetch_videos


@require_http_methods(["GET"])
def manage_videos(request):
    """View to manage videos request
    Args:
        request: A Django HttpRequest
    Returns:
        response: videos list
    """

    query_params = request.GET
    limit = query_params.get("limit", 10)
    reference_id = query_params.get("reference_id", "")
    path_info = request.META.get("PATH_INFO")

    fetch_videos()
    video_list = Video.objects.fetch_videos(reference_id, limit)

    pagination_url = None

    if len(video_list) == int(limit):
        reference_id = video_list[-1].get("_id")
        pagination_url = create_pagination_url(
            url=path_info, limit=limit, query_params={"reference_id": reference_id}
        )

    response = {
        "metadata": {"count": len(video_list), "nextUrl": pagination_url},
        "data": video_list,
    }

    return OK(response)


@require_http_methods(["POST"])
def manage_videos_search(request):
    """View to manage videos request
    Args:
        request: A Django HttpRequest
    Returns:
        response: videos list
    """

    if request._body:
        request_data = json.loads(request._body)
    else:
        raise BadRequest("No query in POST body")

    # set of allowed search keys
    search_keys = {"title", "description", "channelTitle", "videoURL"}

    query = {}

    for term, value in request_data.items():
        if term in search_keys:
            query[term] = value

    # searching videos with required query
    video_list = Video.objects.search_videos(query)

    response = {"metadata": {"count": len(video_list)}, "data": video_list}

    return OK(response)
