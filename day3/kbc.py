question = [
    "1.Who developed Python Programming Language?\n"
    "a) Wick van Rossum\n"
    " b) Rasmus Lerdorf\n"
    " c) Guido van Rossum\n"
    " d) Niene Stom\n",
    # question 2
    "2.Which type of Programming does Python support?\n"
    " a) object-oriented programming\n"
    " b) structured programming\n"
    "  c) functional programming\n"
    " d)all of the mentioned\n",
    # question 3
    "3. Is Python case sensitive when dealing with identifiers?\n"
    " a) no\n"
    " b) yes\n"
    " c) machine dependent\n"
    " d) none of the mentioned\n",
    # Question \n4
    "4. Which of the following is the correct extension of the Python file?\n\n"
    "a) .python\n\n"
    "b) .pl\n\n"
    "c) .py\n\n"
    "d) .p\n",
    # question 5
    "5. Is Python code compiled or interpreted?\n"
    "a) Python code is both compiled and interpreted\n"
    "b) Python code is neither compiled nor interpreted\n"
    "c) Python code is only compiled\n"
    "d) Python code is only interpreted\n",
    # question 6
    "6. All keywords in Python are in _________\n"
    "a) Capitalized\n"
    "b) lower case\n"
    "c) UPPER CASE\n"
    "d) None of the mentioned\n",
    # question no 7
    "8. Which of the following is used to define a block of code in Python language?\n"
    "a) Indentation\n"
    "b) Key\n"
    "c) Brackets\n"
    "d) All of the mentioned\n",
    # question no 9
    "9. Which keyword is used for function in Python language?\n"
    "a) Function\n"
    "b) def\n"
    "c) Fun\n"
    "d) Define\n",
    # question 10
    " 10. Which of the following character is used to give single-line comments in Python?\n"
    "a) //\n"
    "b) #\n"
    "c) !\n"
    "d) /*   \n",
]

answer = ["c", "d", "b", "c", "a", "d", "a", "b", "b"]
# questionLength = len(question)
print("Welcome to the Py KBC")

amount = 0
for i in range(len(question)):
    print(question[i])
    userInput = str(input("enter the answer: "))
    if userInput == answer[i] and question[i]:
        print("right Answer")
        amount = amount + 10000
        print("you won the amount",amount)
        print("\n")

    else:
        print("wrong answer")
        print("\n")
        break

print("you won the amount :", amount)