
from django.contrib.auth.models import User

from dashboard.models import Course, Topic, Post, Membership, CourseSchedule

import datetime

admin = User.objects.create_user(username="admin", email="noreply@micbase.com", password="purpleTeam",
    first_name="admin", last_name="admin")
admin.save()

user_1 = User.objects.create_user(username="farquharson", email="farquharsonWWW@gmail.com", password="purpleTeam",
    first_name="Deborah", last_name="Farquharson")
user_1.save()


user_2 = User.objects.create_user(username="acramond", email="aCramond@sina.com", password="purpleTeam",
    first_name="Amee", last_name="Cramond")
user_2.save()


user_3 = User.objects.create_user(username="gtoroosian", email="gToroosian@u.northwestern.edu", password="purpleTeam",
    first_name="Greg", last_name="Toroosian")
user_3.save()


user_4 = User.objects.create_user(username="rydbeck", email="rRydbeck@fgcu.edu", password="purpleTeam",
    first_name="Rachael", last_name="Rydbeck")
user_4.save()

user_5 = User.objects.create_user(username="adulany", email="aDulany@gmail.com", password="purpleTeam",
    first_name="Andrew", last_name="Dulany")
user_5.save()


course_1 = Course(name="EECS 212 (formerly 310) Mathematical Foundations of Computer Science", professor_firstname="Hendrix", professor_lastname="William", manager=user_1)
course_1.save()

course_2 = Course(name="EECS 214 (formerly 311) Data Structures and Data Management", professor_firstname="Scheuermann", professor_lastname="Peter", manager=user_1)
course_2.save()

course_3 = Course(name="EECS  336 - Design & Analysis of Algorithms", professor_firstname="Hartline", professor_lastname="Jason", manager=user_1)
course_3.save()

course_4 = Course(name="EECS  339 - Introduction to Database Systems", professor_firstname="Peter", professor_lastname="Dinda", manager=user_1)
course_4.save()

course_5 = Course(name="EECS 394 - Software Project Management", professor_firstname="Riesbeck", professor_lastname="Chris", manager=user_1)
course_5.save()

topic_1=Topic(title="Today's class is awesome", content="I really enjoyed today's class. I learned a lot of things about graphs which i've been facinated with.", author=user_3, course=course_1)
topic_1.save()
topic_2=Topic(title="Did anyone get the question about Binary Search Tree?", content="I am so confused, what does the professor mean by O(logn)?", author=user_2, course=course_2)
topic_2.save()
topic_3=Topic(title="Does anyone want to study together for next week's exam?", content="Does anyone want to study together for next week's exam? I'll be in the MUDD library most of the time for the weekend, come on and join me.", author=user_4, course=course_2)
topic_3.save()
topic_4=Topic(title="I really like the on-time walker...", content="I'm not a member of that team, but I really like their idea. And i have a suggestion for them: make it look better!!", author=user_2, course=course_5)
topic_4.save()
topic_5=Topic(title="Last project was killing me!!!!", content="I just submitted the project, it spent me like 2 days. anyone has the same feeling?", author=user_5, course=course_4)
topic_5.save()
topic_6=Topic(title="Hartline looks so cool today!", content="He looks great in that purple suit.", author=user_3, course=course_3)
topic_6.save()


post_1=Post(content="Yeah, I like today's class too.", author=user_2, topic=topic_1)
post_1.save()

post_2=Post(content="I didn't get today's class at all, how could your guys like it?", author=user_1, topic=topic_1)
post_2.save()

post_3=Post(content="I hate this class!", author=user_4, topic=topic_1)
post_3.save()

post_4=Post(content="You can refer to the textbook form page 100 to 150, it explains the problem clearly", author=user_1, topic=topic_2)
post_4.save()

post_5=Post(content="I didn't get it neither...", author=user_3, topic=topic_2)
post_5.save()

post_5=Post(content="The book really helps, thank you Deborah.", author=user_4, topic=topic_2)
post_5.save()

post_6=Post(content="I will study the exam in the library too, let's do it together", author=user_2, topic=topic_3)
post_6.save()

post_7=Post(content="I don't have time... I will go to Florida....", author=user_3, topic=topic_3)
post_7.save()

post_8=Post(content="I didn't finish it yet. Can I email you a few problems I have?", author=user_2, topic=topic_5)
post_8.save()

post_9=Post(content="Yeah.. I like him so much!", author=user_4, topic=topic_6)
post_9.save()


membership_1 = Membership(member = user_1, course = course_1)
membership_1.save()

membership_2 = Membership(member = user_2, course = course_2)
membership_2.save()

membership_3 = Membership(member = user_3, course = course_5)
membership_3.save()

membership_4 = Membership(member = user_4, course = course_4)
membership_4.save()

membership_5 = Membership(member = user_5, course = course_3)
membership_5.save()

membership_6 = Membership(member = user_2, course = course_1)
membership_6.save()

membership_7 = Membership(member = user_4, course = course_1)
membership_7.save()

membership_8 = Membership(member = user_3, course = course_2)
membership_8.save()

membership_9 = Membership(member = user_4, course = course_2)
membership_9.save()

membership_10 = Membership(member = user_4, course = course_3)
membership_10.save()

membership_11 = Membership(member = user_2, course = course_4)
membership_11.save()


courseSchedule_1 = CourseSchedule(course = course_1, start_time = datetime.time(11, 00), end_time = datetime.time(12, 20), weekday = 2)
courseSchedule_1.save()

courseSchedule_2 = CourseSchedule(course = course_1, start_time = datetime.time(11, 00), end_time = datetime.time(12, 20), weekday = 4)
courseSchedule_2.save()

courseSchedule_3 = CourseSchedule(course = course_2, start_time = datetime.time(11, 00), end_time = datetime.time(12, 20), weekday = 1)
courseSchedule_3.save()

courseSchedule_4 = CourseSchedule(course = course_2, start_time = datetime.time(12, 00), end_time = datetime.time(12, 50), weekday = 3)
courseSchedule_4.save()

courseSchedule_5 = CourseSchedule(course = course_2, start_time = datetime.time(12, 00), end_time = datetime.time(12, 50), weekday = 5)
courseSchedule_5.save()

courseSchedule_6 = CourseSchedule(course = course_3, start_time = datetime.time(15, 30), end_time = datetime.time(16, 50), weekday = 2)
courseSchedule_6.save()

courseSchedule_7 = CourseSchedule(course = course_3, start_time = datetime.time(15, 30), end_time = datetime.time(16, 50), weekday = 4)
courseSchedule_7.save()

courseSchedule_8 = CourseSchedule(course = course_4, start_time = datetime.time(16, 00), end_time = datetime.time(16, 50), weekday = 1)
courseSchedule_8.save()

courseSchedule_9 = CourseSchedule(course = course_4, start_time = datetime.time(16, 00), end_time = datetime.time(16, 50), weekday = 3)
courseSchedule_9.save()

courseSchedule_10 = CourseSchedule(course = course_4, start_time = datetime.time(16, 00), end_time = datetime.time(16, 50), weekday = 5)
courseSchedule_10.save()

courseSchedule_11 = CourseSchedule(course = course_5, start_time = datetime.time(10, 00), end_time = datetime.time(10, 50), weekday = 1)
courseSchedule_11.save()

courseSchedule_12 = CourseSchedule(course = course_5, start_time = datetime.time(10, 00), end_time = datetime.time(10, 50), weekday = 3)
courseSchedule_12.save()

courseSchedule_13 = CourseSchedule(course = course_5, start_time = datetime.time(10, 00), end_time = datetime.time(10, 50), weekday = 5)
courseSchedule_13.save()

