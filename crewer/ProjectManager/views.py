from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
# from crewer.constants import MANAGER, MEMBER, TASK_TRACKER_URL


def project_list(request):
    if request.user.is_authenticated:
        if request.user.role == settings.MANAGER:
            return HttpResponse("to-do: send a list of projects")
        elif request.user.role == settings.MEMBER:
            return redirect(settings.TASK_TRACKER_URL)
        else:
            return HttpResponse('Unauthorized', status=401)
    else:
        return HttpResponse('Unauthorized', status=401)


# class ProjectDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)