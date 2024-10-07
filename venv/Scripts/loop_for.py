student_scores=[153,12,32,121,111,144,122,125]
#print(max(student_scores))
max_score=0
for score in student_scores:
    if score >max_score:
        max_score = score
print(max_score)
