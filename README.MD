<p align="center" width="100%">
    <img width="19%" src="https://images2.imgbox.com/de/e7/zRZyBJBF_o.png">
</p>

## Important Note
#### This API is unofficial, fully open source and in Beta version. If you have any questions/troubles, you can use Issues to let me know.

## About
#### udemyAPI developed for udemy teachers. It helps you to monitor your course. You can monitor the questions in your course with this library.  
#### Mail:AzizKpln@protonmail.com
#### LinkedIn:https://www.linkedin.com/in/aziz-k-074604170/

## Importing The Modules
```
from udemyAPI.UdemyQuestionsAnswers import UdemyQuestionAnswers
from udemyAPI import apiConfigTeachingAssistant
from udemyAPI import apiConfigStandard
from udemyAPI.playwrightSetup import setupPlaywright
from udemyAPI.udemyLogin import login
from udemyAPI.teachingAssistant import teachingAssistantReports
```

### setting up playwright
```
pwPage=setupPlaywright()._page_()
```
### Logging in Udemy
```
login(pwPage,<email>,<password>)
```
>-    If you don't want your password to be seen in the script that you're writing,
>-    You can setup a virtual environment. You can search about it if you don't know how to.


## configuration of udemyAPI teaching assistant
```
apiConfig=apiConfigTeachingAssistant(pwPage,<course_link>,<language>,<teaching_assistant_name>)
```
> apiConfigTeachingAssistant returns;
>-    Links of questions that's answered by a spesific teaching assistant in a spesific time.
>-    Links of questions that's unanswered by a spesific teaching assistant in a spesific time.
>-    Comments that's been made by a spesific teaching assistant in a spesific time.

>first argument takes the playwright setup variable

>the second one takes the course link(the link in student panel)

>the third option is the language. EN and TR supported. It's the language of your udemy panel

>the last option takes the teaching assistant name.

## using the API for apiConfigTeachingAssistant
```
uAPI=teachingAssistantReports(apiConfig)
```
> teachingAssistantReports inherits the values that you've written in apiConfigTeachingAssistant.
> therefore you have to use the variable 'apiConfig' inside of teachingAssistantReports function.
```
uAPI._teachingAssistantReports_(5)
```
> To recieve the reports, use the function above and give a day. The code above returns the 5 days reports for teaching assistant "Aziz"
```
print("Comments By Assistant:",uAPI.commentsByTeachingAssistant)
```
> uAPI.commentsByTeachingAssistant used to receive the comments that's been made by the teaching assistant
```
print("Answered:",uAPI.getLinksAnswered)
```
> uAPI.getLinksAnswered used to receive the links that's been answered by the teaching assistant
```
print("UnAnswered:",uAPI.getLinksUnAnswered)
```
> uAPI.getLinksUnAnswered used to receive the links that's NOT been answered by the teaching assistant

```
print(len(uAPI.getLinksUnAnswered))
```
> you can also use the len() python function to recieve the length of answered/unanswered questions.


## configuration of udemyAPI Standard function
```
apiConfig=apiConfigStandard(pwPage,<course_link>,<language>)
```
> apiConfigStandard returns;
>-    Questions that's not been read by anyone.
>-    Questions that's not been answered by anyone.
>-    Questions that's not been answered by any teaching assistant
>- - -  (the difference is in here it looks for every teaching assistant in the course, but above, it looks for a spesific teaching assistant.)

>first argument takes the playwright setup variable

>the second one takes the course link(the link in teaching assistant panel)

>the last option is the language. EN and TR supported. It's the language of your udemy panel

## using the API for apiConfigStandard
```
uAPI=UdemyQuestionAnswers(apiConfig)
```
> UdemyQuestionAnswers inherits the values that you've written in apiConfigStandard.
> therefore you have to use the variable 'apiConfig' inside of UdemyQuestionAnswers function.
```
uAPI.courseID=3
```
<img width="45%" src="https://images2.imgbox.com/e7/d1/8WLJ5K86_o.png">

> courseID takes the ID number of course. For the courses above;

> 1 means all courses

> 2 means etik hacker olma kursu

> 3 means etik hacker olma kursu seviye 2
```
uAPI.unAnsweredQuestions(5)
```
> the code above is used to get unanswered questions in 5 days by anyone
```
uAPI.noAnswerByTeacingAssistants(5)
```
> the code above is used to get unanswered questions in 5 days by any teaching assistants
```
uAPI.unReadQuestions(5)
```
> the code above is used to get unread questions in 5 days by any teaching assistants
```
print(uAPI.getLinks)
```
> the code above used for getting links
```
print(len(uAPI.getLinks))
```
> you can use the len() function to see the number of links