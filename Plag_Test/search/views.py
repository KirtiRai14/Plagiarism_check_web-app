from django.shortcuts import render
from .plagiarism_check import pc_check
from .plagiarism_check import answers
from .models import result_insert

# Create your views here.
def home(request):
    if request.method == "POST":
        if 's-query' in request.POST:
            term = request.POST['s-query']
            opt_1 = request.POST['opt1']
            opt_2 = request.POST['opt2']
            answers.append(term)
            answers.append(opt_1)
            answers.append(opt_2)
            """lookups = Q(Question__icontains=term)
            d = result_insert.objects.filter(lookups).distinct()
            #print(d)"""
            total_db_results_count=result_insert.objects.all().count()
            if request.POST['opt5'] != "":
                opt_3, opt_4, opt_5 = request.POST['opt3'], request.POST['opt4'], request.POST['opt5']
                n, display_title, display_snippet, display_link = pc_check(term, opt_1, opt_2, opt_3, opt_4, opt_5)
                answers.append(opt_3)
                answers.append(opt_4)
                answers.append(opt_5)
                db_results = result_insert.objects.filter(Question=term, Option_1=opt_1, Option_2=opt_2, Option_3=opt_3, Option_4=opt_4, Option_5=opt_5).values('Question','Option_1','Option_2','Option_3','Option_4','Option_5')
                db_results_count = result_insert.objects.filter(Question=term, Option_1=opt_1, Option_2=opt_2, Option_3=opt_3, Option_4=opt_4, Option_5=opt_5).count()
            elif request.POST['opt5'] == "" and request.POST['opt4'] != "":
                opt_3, opt_4 = request.POST['opt3'], request.POST['opt4']
                n, display_title, display_snippet, display_link = pc_check(term, opt_1, opt_2, opt_3, opt_4)
                answers.append(opt_3)
                answers.append(opt_4)
                db_results = result_insert.objects.filter(Question=term, Option_1=opt_1, Option_2=opt_2, Option_3=opt_3, Option_4=opt_4).values('Question','Option_1','Option_2','Option_3','Option_4')
                db_results_count = result_insert.objects.filter(Question=term, Option_1=opt_1, Option_2=opt_2, Option_3=opt_3, Option_4=opt_4).count()
            elif request.POST['opt4'] == "" and request.POST['opt3'] != "":
                opt_3 = request.POST['opt3']
                n, display_title, display_snippet, display_link = pc_check(term, opt_1, opt_2, opt_3)
                answers.append(opt_3)
                db_results = result_insert.objects.filter(Question=term, Option_1=opt_1, Option_2=opt_2, Option_3=opt_3).values('Question','Option_1','Option_2','Option_3')
                db_results_count = result_insert.objects.filter(Question=term, Option_1=opt_1, Option_2=opt_2, Option_3=opt_3).count()
            else:
                n, display_title, display_snippet, display_link = pc_check(term, opt_1, opt_2)
                db_results = result_insert.objects.filter(Question=term, Option_1=opt_1, Option_2=opt_2).values('Question','Option_1','Option_2')
                db_results_count = result_insert.objects.filter(Question=term, Option_1=opt_1, Option_2=opt_2).count()
            print(db_results)
            print(db_results_count)
            db_result_percentage = float((db_results_count / total_db_results_count) * 100)
            # print(db_result_percentage)
            display_array = zip(display_title, display_snippet, display_link)
            return render(request, 'display.html', {'result': n, 'array': display_array, 'database_results': db_results, 'db_result_percent': db_result_percentage})
        elif 'sub_1' in request.POST:
            #print("Accept is WORKING")
            query = result_insert()
            query.Question = answers[0]
            query.Option_1 = answers[1]
            query.Option_2 = answers[2]
            # print("Length of answers array is",len(answers))
            if len(answers) == 6:
                query.Option_3, query.Option_4, query.Option_5 = answers[3], answers[4], answers[5]
                # print("5 Options are working")
            elif len(answers) == 5:
                query.Option_3, query.Option_4 = answers[3], answers[4]
                # print("4 Options are working")
            elif len(answers) == 4:
                query.Option_3 = answers[3]
                # print("3 Options are working")
            if request.POST['reason']:
                query.Reason_if_match_percent_greater_than_50 = request.POST['reason']
                query.save()
            else:
                query.save()
            for i in range(0, len(answers)):
                answers.pop()
            #accept(request)
            return render(request, 'accept.html')
        elif 'sub_2' in request.POST:
            for i in range(0, len(answers)):
                answers.pop()
            #print("reject is working")
            #reject(request)
            return render(request, 'reject.html')
        elif 'sub_3' in request.POST:
            for i in range(0, len(answers)):
                answers.pop()
            #print("change_the_question is working")
            #change_the_question(request)
            return render(request, 'home.html')
        elif 'sub_4' in request.POST:
            return render(request, 'thank_you.html')
    return render(request, 'home.html')


def display(request):
    return render(request, 'display.html')


def accept(request):
    print("accept is WORKING")
    return render(request, 'accept.html')


def reject(request):
    print("reject is WORKING")
    return render(request, 'reject.html')


def change_the_question(request):
    print("change_the_question is WORKING")
    return render(request, 'home.html')
