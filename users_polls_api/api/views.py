from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Poll, Question, Choice, Answer, AnonymousUser
from .serializer import (
	PollSerializer, QuestionSerializer, 
	OwnAnswerSerializer, OneChoiceSerializer,
	SeveralChoiceSerializer, GetAnswersSerializer,
	AnonymousUserSerializer,
)

class AnonymousUserView(APIView):
	def post(self, request):
		name = request.data.get('user')
		serializer = AnonymousUserSerializer(data=name)
		if serializer.is_valid(raise_exception=True):
			user_saved = serializer.save()
		return Response({"success": f"AnonymousUser {user_saved.name} created"})

class PollView(APIView):
	def get(self, request):
		polls = Poll.objects.all()
		serializer = PollSerializer(polls, many=True)
		return Response({"polls": serializer.data})

class OnePollReturnQuestionsView(APIView):
	def get(self, request, pk):
		poll = Poll.objects.get(pk=pk)
		questions = poll.questions.all()
		serializer = QuestionSerializer(questions, many=True)
		return Response({'questions': serializer.data})

class AnswerView(APIView):
	def post(self, request):
		answer = request.data.get('answer')
		question_type = int(answer["question_id"])
		question = Question.objects.get(pk=question_type)
		if question.type_of_question == "text_answer":
			serializer = OwnAnswerSerializer(data=answer)
		elif question.type_of_question == "one_choice_answer":
			serializer = OneChoiceSerializer(data=answer)
		elif question.type_of_question == "several_choice_answer":
			serializer = SeveralChoiceSerializer(data=answer)
		if serializer.is_valid(raise_exception=True):
			answer_saved = serializer.save()
		return Response({"success": f"Your answer for was saved"})

class GetAnswersView(APIView):
	def get(self, request, name_id):
		answers = Answer.objects.filter(name_id=name_id)
		serializer = GetAnswersSerializer(answers, many=True)
		return Response({'answers': serializer.data})	




