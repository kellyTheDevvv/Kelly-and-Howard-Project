from module import Question

question_prompts = [
    "What colors are bananas?\n(a)Yellow\n(b)Red\n(c)Blue\n\n",
    "What color is the sky?\n(a)Yellow\n(b)Blue\n(c)White\n\n",
    "How long is River Nile?\n(a)200km\n(b)250km\n(c)350km"
]

questions =[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"b"),
    Question(question_prompts[2],"c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    return "You scored "+ str(score) + "/" + str(len(questions))    

print(run_test(questions))   