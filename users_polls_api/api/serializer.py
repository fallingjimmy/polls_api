from rest_framework import serializers
from .models import Poll, Question, Choice, Answer, AnonymousUser

class PollSerializer(serializers.ModelSerializer):
	# name =serializers.CharField(max_length=100)
	# start_date = serializers.DateTimeField()
	# end_date = serializers.DateTimeField()
	# description = serializers.CharField()	
	class Meta:
		model = Poll
		fields = ('name', 'description')

class ChoiceSerializer(serializers.ModelSerializer):
	# text = serializers.CharField()
	class Meta:
		model = Choice
		fields = ('text', 'question', 'id')		

class QuestionSerializer(serializers.ModelSerializer):
	# text = serializers.CharField()
	# type_of_question = serializers.CharField(max_length=40)
	choices = ChoiceSerializer(many=True)
	class Meta:
		model = Question
		fields = ('text', 'choices', 'type_of_question', 'poll', 'id')

class AnonymousUserSerializer(serializers.Serializer):
	name = serializers.CharField()
	name_id = serializers.IntegerField()
	def create(self, validated_data):
		return AnonymousUser.objects.create(**validated_data)

class OwnAnswerSerializer(serializers.Serializer):
	name_id = serializers.IntegerField()
	question_id = serializers.IntegerField()
	# one_choice_id = serializers.IntegerField()
	# several_choice_id = serializers.IntegerField()
	own_text = serializers.CharField()
	poll_id = serializers.IntegerField()
	# fields = ('user_name','user_name_id', 'question', 'one_choice', 'several_choice', 'own_text')

	def create(self, validated_data):
		return Answer.objects.create(**validated_data)

class OneChoiceSerializer(serializers.Serializer):
	name_id = serializers.IntegerField()
	question_id = serializers.IntegerField()
	one_choice_id = serializers.IntegerField()
	poll_id = serializers.IntegerField()

	def create(self, validated_data):
		return Answer.objects.create(**validated_data)

# class SeveralChoicesListSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Choice
# 		fields = ('choice_id')


class SeveralChoiceSerializer(serializers.Serializer):
	# several_choice = SeveralChoicesListSerializer(many=True)
	name_id = serializers.IntegerField()
	question_id = serializers.IntegerField()
	#several_choice = serializers.ListField()
	poll_id = serializers.IntegerField()
	
	def create(self, validated_data):
		return Answer.objects.create(**validated_data)

class GetAnswersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ('name', 'question', 'one_choice', 'several_choice', 'own_text')