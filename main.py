Questions = []
Options = []
abc = "abcdefgh"


QuestionNumber = input("Enter The Question Number :   ")
OptionNumber = input("Enter The Option Number :   ")
for i in range(int(QuestionNumber)) :
    Question = input("Enter the question :   ")
    Questions.append(Question)
    for x in range(int(OptionNumber)) :
        Option = input("Enter the option :   ")
        Options.append(Option)


for i in range(int(QuestionNumber)) :
    TitleOfQuestion = str(i+1) + "- " +  Questions[i] + ("\n" * 2 )
    examfile = open("exam.txt","a")
    examfile.write(TitleOfQuestion)
    for x in range(int(OptionNumber)) :
        examfile.write(abc[x] + ") " + Options[x] + "\n")
    examfile.write("\n")
    examfile.close()





    