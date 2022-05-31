from django.http import HttpResponse
from django.shortcuts import render
from mysite1 import MODEL
import pandas as pd


def myRound(x):
    if x < 0.5:
        return 0
    else:
        return 1


def do_post(request, targetPage):
    age_text = request.POST.get('age', '0')
    age = float(age_text) / 100
    sex_text = request.POST.get('sex', '0')
    sex = 0
    if sex_text == 'male':
        sex = 0
    else:
        sex = 1
    composition_text = request.POST.get('composition', '0')
    composition = 0.0
    if composition_text == 'cystic':
        composition = 0.0
    elif composition_text == 'partially_cystic':
        composition = 0.5
    elif composition_text == 'solid':
        composition = 1.0
    margin_text = request.POST.get('margin', '0')
    margin = 0.0
    if margin_text == 'well_defined':
        margin = 0.0
    elif margin_text == 'ill_defined':
        margin = 0.5
    elif margin_text == 'spiculated':
        margin = 1.0
    echogenicity_hypoechogenicity = 0
    echogenicity_isoechogenicity = 0
    echogenicity_text = request.POST.get('echogenicity', '0')
    if echogenicity_text == 'hypoechogenicity':
        echogenicity_hypoechogenicity = 1
        echogenicity_isoechogenicity = 0
    elif echogenicity_text == 'isoechogenicity':
        echogenicity_hypoechogenicity = 0
        echogenicity_isoechogenicity = 1
    elif echogenicity_text == 'hyperechogenicity':
        echogenicity_hypoechogenicity = 0
        echogenicity_isoechogenicity = 0
    calcification_microcalcification = 0
    calcification_non = 0
    calcification_text = request.POST.get('calcification', '0')
    if calcification_text == 'microcalcification':
        calcification_microcalcification = 1
        calcification_non = 0
    elif calcification_text == 'non':
        calcification_microcalcification = 0
        calcification_non = 1
    elif calcification_text == 'macrocalcification':
        calcification_microcalcification = 0
        calcification_non = 0

    test_data = [[age, sex, composition, margin, echogenicity_hypoechogenicity, echogenicity_isoechogenicity,
                  calcification_microcalcification, calcification_non]]

    test_df = pd.DataFrame(test_data,
                           columns=['age', 'sex', 'composition', 'margin', 'echogenicity_hypoechogenicity',
                                    'echogenicity_isoechogenicity', 'calcification_microcalcification',
                                    'calcification_non'], dtype=float)
    print(test_df)
    predict_test = [myRound(x[0]) for x in MODEL.predict(test_df)]
    result = ''
    if predict_test[0] == 1:
        result += 'Positive'
    else:
        result += 'Negative'
    # return HttpResponse(result)
    return render(request, targetPage, locals())


def test_view(request):
    if request.method == 'GET':
        return render(request, 'test.html', locals())
    elif request.method == 'POST':
        return do_post(request, 'test.html')


def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html', locals())
    elif request.method == 'POST':
        return do_post(request, 'index.html')
