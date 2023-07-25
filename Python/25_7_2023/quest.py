"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:
fs = open("questions.txt","r")
question_bank = fs.readlines()
fs.close()
question_bank = [q.strip() for q in question_bank]
question_bank = [q.split("=") for q in question_bank]
result = []
n=0
for question in question_bank:
    print(f"{question[0]} = ")
    inp= input()
    if inp == question[1]:
        n+=1
    result.append(inp)
m = len(question_bank)

fs = open("result.txt","w")
fs.write(f"Your final score is {n}/{m}.")