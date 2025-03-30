---
layout: page
title: about this course // syllabus
description: Syllabus for DSCI 345
---

See [the schedule](schedule.html) for a list of topics by week, with links to slides.


# Instructors:

- [Peter Ralph](https://kr-colab.github.io/people), instructor: plr@uoregon.edu
    * lecture: 11-11:50 MWF in ESL 105
    * office hours: TBD

- [Ben Young](https://pages.uoregon.edu/bjy/), instructor: bjy@uoregon.edu
    * lecture: 11-11:50 MWF in LA 230
    * office hours: TBD

# Course Description

This course covers a theoretical basis in probability and statistics
that is foundational for work in data science.
Randomness and uncertainty are fundamental at all stages of data science work,
from understanding strengths and limitations of data sources,
through modeling and inference,
to algorithmic aspects of learning and prediction
(e.g., random forests; stochastic gradient decent).
This course is aimed at students who have done some work looking at real data
and want to have a deeper (and more quantitative)
understanding of what we are doing when we make predictions using data.
The course covers
both tools for modeling randomness and calculating properties of those models,
and the process of estimating quantities from data.
An important thread throughout the course is on *simulating data*:
being able to construct and simulate from sophisticated models for random data generation.


# Course Objectives

Students will:

- become fluent in basic topics of probability: randomness, uncertainty, estimation, and prediction;
    probability and expectation, conditional probabilities, and random variables; mean, variance, expectation.
- be able to formulate and describe models of real world situations that incorporates realistic models of randomness, and
- be able to simulate from these models.
- learn how to pick realistic simulation parameters by fitting models to data.
    This includes: the central limit theorem, the method of moments fitting, minimum variance estimators,
    and discussions of outliers, overdispersion, goodness of fit.
- become familiar with the theoretical basis of classical statistics,
    including the central limit theorem,
    hypothesis testing, likelihood, and $p$-values.
- be able to use simulations to measure power, false positives, and false discovery rates.
- understand and apply principal component analysis,
    to numerical and textual data.
- learn to detect and correct for overfitting using regularization and cross-validation.

## Course Information

- *Websites:* besides [the page you are looking at](https://uodsci.github.io/dsci345/),
    assignments and announcements will be distributed
    on the [canvas page](https://canvas.uoregon.edu/)

## Prerequisites:

Students should be familiar with the basics of calculus and linear algebra,
have experience with python,
and have worked with describing/visualizing data.
UO course prerequisites:
Math 342 (linear algebra), CS 211 (computer science II), and
either DSCI 101/102 or some other exposure to data science/statistics.

# Assignments

There will be weekly assignments, each a Jupyter notebook;
download each one, complete it on your own, and submit your completed notebook on Canvas,
generally by *Monday at 11:59pm* (but see the Canvas assignment).

You are encouraged to work with other students (please say who you worked with)
and use whatever internet sources you like (please cite your sources).
However, the final work (both code and writing) should be your own:
for instance, if you use generative AI to suggest approaches to the problem,
you should not copy-paste the results in, but rather rewrite it in your own words.

# Quizzes

There will be 9 short quizzes, at start of class on Monday.
The purpose of the quizzes is:
- provide a grade-based motivation for students to keep up with the readings;
- assess whether students can do modelling *without assistance* (the difference between a B and C grade)
- help the instructor understand the state of knowledge of students in the class.

# Final

The final exam will be *in class*; see [the exam schedule](https://registrar.uoregon.edu/dates-deadlines/exams) to find the day and time.
The final will aim to cover the same topics as the homeworks,
but structured in such a way that it is do-able in class (i.e., without the computer).

Grade breakdown:

- 20% Quizzes  (lowest score dropped)
- 50% Assignments (lowest two scores dropped)
- 30% Final

## Textbooks

We will be assigning reading from these (freely available) books:

- [_Probability for Data Science_](http://prob140.org/textbook/content/README.html),
    by Ani Adhikari and Jim Pitman.

There is a list of other useful reading materials on [the page of references](https://uodsci.github.io/dsci345/pages/reference.html).

## Software:

Class demonstrations, exercises, and homeworks
will be done using [jupyter notebooks](https://jupyter.org/),
so you should have on your computer a working python installation
with

- [jupyter](https://jupyter.org/) (either jupyter lab or jupyter notebook),
- [numpy](https://numpy.org/),
- [scipy](https://scipy.org/),
- [matplotlib](https://matplotlib.org/), and
- [scikit-learn](https://scikit-learn.org/).

# Course Modality

This class is offered in person.
We aim to make class available remotely,
by broadcasting lectures on zoom and making the recordings available afterwards on Canvas;
however, at times there are technical issues, so we cannot guarantee this will be available for all lectures.
Moreover, for most students in-class participation is more engaging and results in better learning outcomes, so we strongly encourage in-person attendance.
However, we know that things happen in life that might make you unable to come - for instance, please do not come to class if you are sick.

# Course Policies

- **How will we communicate with you?**
    Our class will communicate through our Canvas site.
    Announcements and emails are archived there, automatically forwarded to your UO email, and can even reach you by text.
    Check and adjust your settings under Account > Notifications.
    We also get in touch with individual students when needed through email.
    Feedback on assignments will occur in Canvas.

- **How and why can you communicate with us?**
    Please reach out by email or by attending office hours!
    We can also take a few questions immediately after class.

We enjoy talking with students about the course material!
Are you confused or excited about something?
Wondering how what we're learning relates to current events, career choices, or other classes you can take UO?
Please be in touch!
Please also be in touch to tell us how you are doing in the course.
If you are having trouble with some aspect of it, we would like to strategize with you.
We believe every student can succeed in this course, and we care about your success.


# Classroom Community Expectations

All members of the class (both students and instructor) can expect to:

- *Participate and Contribute:*
    All students are expected to participate by sharing ideas and contributing to the learning environment.
    This entails preparing, following instructions, and engaging respectfully and thoughtfully with others.

- *Expect and Respect Diversity:*
    All classes at the University of Oregon welcome and respect diverse experiences, perspectives, and approaches.
    What is not welcome are behaviors or contributions that undermine, demean, or marginalize others
    (especially if this is based on race, ethnicity, gender, sex, age, sexual orientation, religion, ability, or socioeconomic status).
    We value differences and communicate disagreements with respect.

- *Help Everyone Learn:*
    Part of how we learn together is by learning from one another.
    To do this effectively, we need to be patient with each other, identify ways we can assist others,
    and be open-minded to receiving help and feedback from others.
    Don't hesitate to contact us to ask for assistance or offer suggestions that might help us learn better.

# Absences

Attendance is important because we will develop our knowledge in part through in-class activities that require your active engagement.
We'll have discussions, small-group activities, and do other work during class that will be richer for your presence,
and that you won't be able to benefit from if you are not there.
That said, if you are feeling ill, please stay home to heal and avoid infecting your classmates.
Please take absences only when necessary, so when they are necessary, your prior attendance will have positioned you for success.

We do not assign credit specifically for attendance, but will have quizzes in class on Mondays.
We drop the lowest quiz score, so if you will need to miss more than one Monday, please talk to us.

# Student Workload and Time Use

This is a 4-credit hour course,
so you should expect to complete 120 hours of work for the course: an average of about 12 hours each week (this includes time in-class).
An estimate for time usage for activities and assignments in an average week is below -
some weeks may have shorter or longer time commitments:

- In-class meetings: 3 hours
- Pre-class reading: 2 hours
- Assignments: 7 Hours


# Course Deadlines and Late Work

Assignments in this course are generally due once a week.
Although deadlines are firm, your lowest two assignment scores will be dropped.

# Grading Policies

**Grading scheme:** A = 85-100%, B = 75-84%, C = 65-74%, D = 55-64%, F = 0-55%.

Note that these grades translate directly and unambiguously to grades out of 10.

We have chosen these cutoffs based on our past experience and the following description
from the math department's [undergraduate grading standards](https://blogs.uoregon.edu/mathresources/files/2023/05/MathGradingStandards-1tli4lj.pdf)
for what the various letter grades should mean.
The relevant language, modified from that for "applied" courses, is:

- **A:**
    Consistently chooses appropriate models, uses correct techniques, and carries calculations through to a correct answer.
    Able to estimate error when appropriate,
    and to describe assumptions and limitations of models as appropriate.
- **B:**
    Usually chooses appropriate models and uses correct techniques, and makes few calculational errors.
    Able to estimate error
    and to describe assumptions and limitations of models when prompted.
- **C:**
    Makes calculations correctly or substantially correctly, but requires guidance on choosing models and technique.
    Generally able to estimate error and to describe assumptions and limitations of models when prompted, but often requires guidance.
- **D:**
    Makes calculations or develops models in some topics correctly or substantially correctly,
    but not consistently or in all topics.
- **F:**
    Can neither choose appropriate models, or techniques, nor carry through calculations.

Pluses and Minuses are given out by instructor discretion, generally only to scores at the very top or bottom scores of these ranges (so that an A+ really means truly exceptional work).

We anticipate *not adjusting the scores at all*: if you get 8 out of 10 on a problem, that means you did a B's worth of work on it.


# Generative Artificial Intelligence Use

Students can use generative AI ("GenAI") tools in this class to help with certain aspects of course work and assignments.
This includes brainstorming ideas, creating a paper outline, or summarizing research findings of articles.
However, you cannot use content such as text or graphics created by GenAI tools in your work;
rather, you must be the author/creator of your work submissions.
For example, you can use a GenAI tool to suggest a paper outline based on a draft you provide it,
but you cannot submit an assignment with text generated by GenAI as if the text is your own writing.

As we see it, there are a few good reasons for this:

- *You did not do the work.*
    A skill we do cover in class is how to effectively search for solutions to problems
    (e.g., what are good keywords? what are good/reliable sources?),
    a skill that overlaps with effective querying of GenAI.
    However, if you were to find an exact solution to a given problem on the web somewhere,
    you should not paste that answer into your homework,
    because (a) the point of the class is for you to learn, and learning requires working;
    and (b) plagiarism.

- To assign you a letter grade, *we need to assess whether *you* can do mathematical modelling and whether *you* can assess the errors in your models* -
    getting a GenAI model to produce plausible work is *not* the same thing as being able to do it yourself
    (the latter requires deeper understanding).

In accordance with UO policy, if we believe you've handed in work created whole or in part by GenAI tools,
we may submit a report of suspected academic misconduct
to the Office of Student Conduct and Community Standards for that office to make a determination of responsibility
and, if warranted, assess a grade penalty.
So, if you are in doubt or have questions about your usage of a particular tool, check in with us.
