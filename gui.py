# -*- coding: utf-8 -*-
"""gui.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1toD8X6GBINH9PQS1OtOvIGWpHJ6cA0VH
"""

time_online_student = float(input("How many hours a week does your student spend in online schooling? "))
total_posts_by_student = float(input("How many times does your student ask for help in a week ?"))
days_spent = float(input("If your student was given 14 days to complete an assignment, how long would they spend on it? "))
def reset_score(score):
  if score >= 100:
    score = 100
  return score
pred_score_time_online = 13.19 + 20.119 + 46.28 * time_online_student  - 12.16 * (time_online_student ** 2) + 1.32 * (time_online_student ** 3) - 0.05 * (time_online_student ** 4) 
pred_score_total_posts = 35.69 + 65.13 * total_posts_by_student
pred_score_procrastination = 13.97 * days_spent
pred_score_time_online = reset_score(pred_score_time_online)
pred_score_total_posts = reset_score(pred_score_total_posts)
pred_score_procrastination = reset_score(pred_score_procrastination)
pred_score = pred_score_time_online + pred_score_total_posts + pred_score_procrastination
pred_score /= 3
pred_score = reset_score(pred_score)
pred_score = round(pred_score, 2)
pred_grade = 'a'
if pred_score < 69.5:
  pred_grade = 'F'
elif pred_score > 69.5 and pred_score < 71.5:
  pred_grade = 'D-'
elif pred_score > 71.5 and pred_score < 73.5:
  pred_grade = 'D'
elif pred_score > 73.5 and pred_score < 75.5:
  pred_grade = 'D+'
elif pred_score > 75.5 and pred_score < 78.5:
  pred_grade = 'C-'
elif pred_score > 78.5 and pred_score < 81.5:
  pred_grade = 'C'
elif pred_score > 81.5 and pred_score < 84.5:
  pred_grade = 'C+'
elif pred_score > 84.5 and pred_score < 87.5:
  pred_grade = 'B-'
elif pred_score > 87.5 and pred_score < 90.5:
  pred_grade = 'B'
elif pred_score > 90.5 and pred_score < 92.5:
  pred_grade = 'B+'
elif pred_score > 92.5 and pred_score < 95.5: 
  pred_grade = 'A-'
elif pred_score > 95.5 and pred_score < 97.5:
  pred_grade = 'A'
elif pred_score > 97.5:
  pred_grade = 'A+'
else:
  pred_grade = 'u wot m8 thats impossible'
print("Your child's predicted score is: {}".format(pred_score))
print("Your child's predicted score (as a letter grade) is: {}".format(pred_grade))