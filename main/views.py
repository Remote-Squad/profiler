# learning_types/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer


class LearningTypeAPIView(APIView):
    serializer_class = AnswerSerializer

    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        answers_data = serializer.validated_data.get('answers')

        print(answers_data)

        # Assuming classify_learning_type function is implemented to return learning types
        # You can integrate your classification logic here
        classified_types, _ = classify_learning_type(answers_data)

        return Response({'classified_types': classified_types}, status=status.HTTP_200_OK)
