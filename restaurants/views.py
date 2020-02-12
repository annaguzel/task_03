from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list":[
        {"restaurant_name":"Chappati","food_type":"Indian"},
        {"restaurant_name":"Ocean","food_type":"SeaFood"},
        {"restaurant_name":"MADO","food_type":"Turkish Food"},
    ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":{
    "restaurant_name":"Alia",
    "food_type":"Arabic",
    },

    }
    return render(request, 'detail.html', context)
