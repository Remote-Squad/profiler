from rest_framework.response import Response
from rest_framework.views import APIView

from .agents.v1 import make_research
from .models import Research
from .serializers import ResearchSerializer


class ResearchAPIView(APIView):
    serializer_class = ResearchSerializer

    def get(self, request):
        query = request.GET.get('q') if request.GET.get('q') else request.GET.get("query")

        if not query:
            return Response({"error": "Missing query parameter"})

        if Research.objects.filter(query=query).exists():
            data = Research.objects.get(query=query)

            serializer = self.serializer_class(instance=data)

            return Response(serializer.data)

        data = make_research(query=query)
        research = Research.objects.create(query=query, data=data)
        serializer = self.serializer_class(instance=research)
        return Response(serializer.data)
