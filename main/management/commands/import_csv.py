import csv
from django.core.management.base import BaseCommand
from main.models import Question, Choice

class Command(BaseCommand):
    help = "Import questions and choices from CSV files"

    def add_arguments(self, parser):
        parser.add_argument("questions_file", type=open, help="Path to the file with question information")
        parser.add_argument("choices_file", type=open, help="Path to the file with question choices")

    def handle(self, *args, **options):
        # questions_file = options["questions_file"]
        choices_file = options["choices_file"]

        #Import questions
        # questions_reader = csv.reader(questions_file, delimiter=",")
        # for row in questions_reader:
        #     if row[0] == "question_text":
        #         continue

        #     question = Question()
        #     question.question_text = row[0]
        #     question.correct_option = row[6]
        #     question.topic = row[3]
        #     question.solution = row[2]
        #     question.level = row[5]
        #     question.subject = row[4]
        #     question.save()

        # Import choices
        check = 0 
        choices_reader = csv.reader(choices_file, delimiter=",")
        for row in choices_reader:
            if row[0] == "questions":
                continue
            if  check <= 11351:
                check = check + 1
                continue
            
            question_text = row[0]
            choice_text = row[1]
            label = row[2]
            
            question = Question.objects.get(question_text=question_text)

            choice = Choice()
            choice.question = question
            choice.choice_text = choice_text
            choice.choice_label = label
            choice.save()

        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
