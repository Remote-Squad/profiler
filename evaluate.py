import random

# Define the questions with unique identifiers and their corresponding answers
questions = [
    {
        'id': 1,
        'question': "When studying for a test, what helps you most?",
        'answers': {
            'a': ('Colorful diagrams and pictures in your notes.', 'Visual Learner'),
            'b': ('Listening to recordings of the lesson or classmates explaining things.', 'Auditory Learner'),
            'c': ('Highlighting important information in your textbook or making flashcards.', 'Kinesthetic Learner'),
            'd': ('Discussing the material with friends and explaining it to each other.', 'Communicative Learner')
        }
    },
    {
        'id': 2,
        'question': "When learning new things, would you rather:",
        'answers': {
            'a': ('See pictures or diagrams that show the steps.', 'Visual Learner'),
            'b': ('Hear instructions or explanations spoken aloud.', 'Auditory Learner'),
            'c': ('Try things out yourself and learn by doing.', 'Kinesthetic Learner'),
            'd': ('Talk about it with someone and ask questions.', 'Communicative Learner')
        }
    },
    {
        'id': 3,
        'question': "You're lost in the forest. How would you find your way back?",
        'answers': {
            'a': ('Use a map or draw a picture of your path if you have paper and pencil.', 'Visual Learner'),
            'b': ('Listen for familiar sounds or follow someone\'s directions.', 'Auditory Learner'),
            'c': ('Try different paths and remember your movements (like turning left at the big tree).',
                  'Kinesthetic Learner'),
            'd': ('Ask someone for help or discuss the situation with a friend.', 'Communicative Learner')
        }
    },
    {
        'id': 4,
        'question': "How do you best remember things you need to do?",
        'answers': {
            'a': ('Writing them down in a colorful to-do list.', 'Visual Learner'),
            'b': ('Setting an alarm or repeating things to yourself.', 'Auditory Learner'),
            'c': ('Tying a knot in a string or using physical reminders like putting your shoes by the door.',
                  'Kinesthetic Learner'),
            'd': ('Telling a friend or making a plan with them.', 'Communicative Learner')
        }
    },
    {
        'id': 5,
        'question': "Imagine you're learning a new language. What would help you most?",
        'answers': {
            'a': ('Watching videos of people speaking the language.', 'Visual Learner'),
            'b': ('Listening to music and audiobooks in the new language.', 'Auditory Learner'),
            'c': ('Practicing speaking with a friend or partner.', 'Kinesthetic Learner'),
            'd': ('Discussing the material with friends and explaining it to each other.', 'Communicative Learner')
        }
    }
]


def shuffle_questions_and_answers(questions):
    # Shuffle the questions
    shuffled_questions = random.sample(questions, len(questions))

    # Shuffle the answers for each question
    for question in shuffled_questions:
        items = list(question['answers'].items())
        random.shuffle(items)
        question['answers'] = dict(items)

    return shuffled_questions


import random

# Define the questions with unique identifiers and their corresponding answers
questions = [
    {
        'id': 1,
        'question': "When studying for a test, what helps you most?",
        'answers': {
            'a': ('Colorful diagrams and pictures in your notes.', 'Visual Learner'),
            'b': ('Listening to recordings of the lesson or classmates explaining things.', 'Auditory Learner'),
            'c': ('Highlighting important information in your textbook or making flashcards.', 'Kinesthetic Learner'),
            'd': ('Discussing the material with friends and explaining it to each other.', 'Communicative Learner')
        }
    },
    {
        'id': 2,
        'question': "When learning new things, would you rather:",
        'answers': {
            'a': ('See pictures or diagrams that show the steps.', 'Visual Learner'),
            'b': ('Hear instructions or explanations spoken aloud.', 'Auditory Learner'),
            'c': ('Try things out yourself and learn by doing.', 'Kinesthetic Learner'),
            'd': ('Talk about it with someone and ask questions.', 'Communicative Learner')
        }
    },
    {
        'id': 3,
        'question': "You're lost in the forest. How would you find your way back?",
        'answers': {
            'a': ('Use a map or draw a picture of your path if you have paper and pencil.', 'Visual Learner'),
            'b': ('Listen for familiar sounds or follow someone\'s directions.', 'Auditory Learner'),
            'c': ('Try different paths and remember your movements (like turning left at the big tree).',
                  'Kinesthetic Learner'),
            'd': ('Ask someone for help or discuss the situation with a friend.', 'Communicative Learner')
        }
    },
    {
        'id': 4,
        'question': "How do you best remember things you need to do?",
        'answers': {
            'a': ('Writing them down in a colorful to-do list.', 'Visual Learner'),
            'b': ('Setting an alarm or repeating things to yourself.', 'Auditory Learner'),
            'c': ('Tying a knot in a string or using physical reminders like putting your shoes by the door.',
                  'Kinesthetic Learner'),
            'd': ('Telling a friend or making a plan with them.', 'Communicative Learner')
        }
    },
    {
        'id': 5,
        'question': "Imagine you're learning a new language. What would help you most?",
        'answers': {
            'a': ('Watching videos of people speaking the language.', 'Visual Learner'),
            'b': ('Listening to music and audiobooks in the new language.', 'Auditory Learner'),
            'c': ('Practicing speaking with a friend or partner.', 'Kinesthetic Learner'),
            'd': ('Discussing the material with friends and explaining it to each other.', 'Communicative Learner')
        }
    }
]


def shuffle_questions_and_answers(questions):
    # Shuffle the questions
    shuffled_questions = random.sample(questions, len(questions))

    # Shuffle the answers for each question
    for question in shuffled_questions:
        items = list(question['answers'].items())
        random.shuffle(items)
        question['answers'] = dict(items)

    return shuffled_questions


def classify_learning_type(responses, shuffled_questions):
    # Initialize a dictionary to store points for each learning type
    learning_types = {
        'Visual Learner': 0,
        'Auditory Learner': 0,
        'Kinesthetic Learner': 0,
        'Communicative Learner': 0
    }

    # Iterate over the responses and assign points to the learning types
    for i, (question_id, answer) in enumerate(responses):
        question = next(q for q in shuffled_questions if q['id'] == question_id)
        learning_type = question['answers'].get(answer)[1]
        if learning_type:
            learning_types[learning_type] += 1

    # Determine the learning types with the highest points
    sorted_learning_types = sorted(learning_types.items(), key=lambda x: x[1], reverse=True)
    top_two_learning_types = sorted_learning_types[:2]

    # Check if the top two learning types have the same points
    if top_two_learning_types[0][1] == top_two_learning_types[1][1]:
        return top_two_learning_types, learning_types
    else:
        return [top_two_learning_types[0]], learning_types


# Shuffle the questions and their answers
shuffled_questions = shuffle_questions_and_answers(questions)

# Example usage:
# Assume the student responded to the shuffled questions with the following answers
responses = [(1, 'd'), (2, 'c'), (3, 'b'), (4, 'a'), (5, 'b')]  # Example responses with question IDs and chosen options

top_learning_types, points = classify_learning_type(responses, shuffled_questions)
print(f"The student's top learning type(s): {top_learning_types} with points: {points}")

# Shuffle the questions and their answers
shuffled_questions = shuffle_questions_and_answers(questions)

print(shuffled_questions)

# Example usage:
# Assume the student responded to the shuffled questions with the following answers
responses = [(1, 'a'), (2, 'c'), (3, 'b'), (4, 'a'), (5, 'a')]  # Example responses with question IDs and chosen options

learning_type, points = classify_learning_type(responses, shuffled_questions)
print(f"The student is classified as a {learning_type} with points: {points}")
