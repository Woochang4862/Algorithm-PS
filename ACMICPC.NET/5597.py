student_ids = {i for i in range(1,31)}
for _ in range(28):
    student_ids -= {int(input())}
print(' '.join(map(str,sorted(list(student_ids)))))
