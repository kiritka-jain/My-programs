if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    average_marks = 0
    sum = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for names in student_marks:
        if names == query_name:
            marks_list = student_marks.get(names)
            for elem in marks_list:
                sum = sum + elem
            average_marks = sum / len(marks_list)
            print("%.2f"%average_marks)



