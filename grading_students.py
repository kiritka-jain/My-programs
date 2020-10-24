def get_rounded_marks(score):
   if (score < 38) or (score % 5) < 3:
        return score
   return (score+(5-score%5))




no_of_stud = int(input())
for _ in range(no_of_stud):
    student_marks = int(input())
    print(get_rounded_marks(student_marks))

