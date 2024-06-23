# learning_types/models.py

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    choices = [("Visual Learner", "Visual Learner"), ("Auditory Learner", "Auditory Learner"), ("Kinesthetic Learner", "Kinesthetic Learner"), ("Communicative Learner", "Communicative Learner")]
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    learning_type = models.CharField(max_length=50, choices=choices)  # Visual Learner, Auditory Learner, Kinesthetic Learner, Communicative Learner

    def __str__(self):
        return self.answer_text


class LearningType(models.Model):
    learning_type = models.CharField(max_length=100)