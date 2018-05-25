from django.shortcuts import render,HttpResponse
from django.template import loader
from .models import Question
from .models import Exam
from .models import Course
from .models import Chapter

# Create your views here.
def index(request):
    course_list=Course.objects.all()
    return render(request, 'exams/index.html',{'courses':course_list})

def create(request):
    question_arr=[]
    test=request.GET.get("course")
    ch=request.GET.get("numq")
    diff=request.GET.get("diff")
    simple=request.GET.get("simple")
    remin=request.GET.get("remin")
    understand=request.GET.get("understand")
    creativity=request.GET.get("creativity")
    c=Course.objects.get(course_name=test)
    ch=Chapter.objects.get(course=c)
    chapterList=Question.objects.filter(chapter=ch )
    ch_count=chapterList.count()
    question_list=Question.objects.filter(course=c)
    q_count=question_list.count()
    total_exam_questions=1/ch_count
    q_count_ch=q_count/total_exam_questions
   # population(q_count ,question_list)
    numberOfQuestionPerSimpleLevel=float(simple)/total_exam_questions
    numberOfQuestionPerDiffLevel=float(diff)/total_exam_questions
    numberOfQuestionPerReminLevel=float(remin)/total_exam_questions
    numberOfQuestionPerUnderstandingLevel=float(understand)/total_exam_questions
    numberOfQuestionPercreativityLevel=float(creativity)/total_exam_questions
    qlistcreativity=Question.objects.filter(q_obj="3")
    qlistreminding=Question.objects.filter(q_obj="2")
    qlistunderstanding=Question.objects.filter(q_obj="1")
    qlistsimple=Question.objects.filter(q_obj="1")
    qlistdifficult=Question.objects.filter(q_obj="2")
    pool=[]
    if(qlistcreativity.count() !=0 | qlistdifficult.count() != 0 | qlistreminding.count() !=0 | qlistunderstanding.count() != 0 | qlistsimple.count() !=0): 
        j=1
        if(j<numberOfQuestionPercreativityLevel):
            pool.append(qlistcreativity)
        j+=1
        jj=1
        if(jj<numberOfQuestionPerUnderstandingLevel):
            pool.append(qlistunderstanding[0])
        jj+=1  
        jjj=1
        if(jjj<numberOfQuestionPerReminLevel):
            pool.append(qlistreminding)
        jjj+=1      
        d=1
        if(d<numberOfQuestionPerDiffLevel):
            pool.append(qlistdifficult)
        d+=1  
        dd=1
        if(dd<numberOfQuestionPerSimpleLevel):
            pool.append(qlistdifficult)
        dd+=1  
    else:
        pass    

    #population(test,ch)
    return render(request, 'exams/create.html',{'s':pool})
#    return render(request, 'exams/index.html',{'courses':course_list})    

# def exam(request):
#     # return HttpResponse("create new exam .")
#     #return HttpResponse(template.render(context, request))
#     question_list=Question.objects.all()
#     print(question_list)
#     return render(request, 'exams/exam.html',{'questions':question_list})


# def population(q_count,question_list):
#     populat=[]
#     print(question_list[1])


# #def sample(numOfChapter,q)        