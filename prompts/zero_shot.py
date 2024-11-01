ZERO_SHOT_PROMPT = """
Given the following topic {input}, generate a quiz with 5 questions.
Each question should be a multiple choice question with 4 options. Provide one correct answer and three incorrect answers.
Ensure the questions cover different aspects of the topic.
Format the output as a JSON object with the following structure:
{{
    "questions": [
        {{
            "question": "Question text",
            "choices": [
                {{"key": "A", "value": "Option 1"}},
                {{"key": "B", "value": "Option 2"}},
                {{"key": "C", "value": "Option 3"}},
                {{"key": "D", "value": "Option 4"}}
            ],
            "answer": "A"
        }},
        ...
    ]
}}
"""
