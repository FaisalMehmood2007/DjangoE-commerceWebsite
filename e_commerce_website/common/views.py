from django.shortcuts import render

from e_commerce_website.jewelry.models import Category, CustomerGender, Metal, StoneType


def get_nav_bar_context():

    female_gender = CustomerGender.objects.filter(classification='F').get()
    male_gender = CustomerGender.objects.filter(classification='M').get()
    
    categories = Category.objects.all()
    categories_choices = [x[1] for x in Category.TitleChoices.choices]
    
    categories_by_choices = {}
    
    index = 0

    for category in categories:
        categories_by_choices[category] = categories_choices[index]
        index += 1
    
    metals = Metal.TitleChoices.choices
    
    stones = StoneType.TitleChoices.choices
    
    filtered_stones =  filter(lambda stone: stone[1] in ['Ruby', 'Pearl', 'Sapphire', 'Emerald', 'Diamond'], stones)
    
    
    context = {
        'female_gender': female_gender,
        'male_gender': male_gender,
        'categories_by_choices': categories_by_choices,
        'metals': metals,
        'stones': filtered_stones,
    }
    
    return context

def index_page(request):
    
    context = get_nav_bar_context()
    
    return render(request, 'common/index-page.html', context)

# from django import forms
# from django.shortcuts import render

# from e_commerce_website.jewelry.models import Category

# class IndexForm(forms.Form):
#     categories = Category.TitleChoices
    
#     category = forms.ChoiceField(
#         choices=categories,
#         required=False,
#         widget=forms.CheckboxSelectMultiple(),
#     )

# def index_page(request):
    
#     if request.method == 'get':
#         form = IndexForm()
        
#     else:
#         form = IndexForm(request.POST)
        
#     context = {
#         'form': form,
#     }
    
#     return render(request, 'common/index-page.html', context)