from django.shortcuts import render

def index_page(request):
    goods = [
        {
            "section": "technologies",
            "label": "VLSU-ISPI",
            "type": "computer",
            "price": 30000,
            "img": "https://adm-verhotury.ru/media/resized/9fzAzZbUr6GKsgrRZ04AzP-IO2q3T_B3MhrM7j7WX9g/rs:fit:1024:768/aHR0cHM6Ly9hZG0t/dmVyaG90dXJ5LnJ1/L21lZGlhL3Byb2pl/Y3RfbW9fOTkvYWIv/ZDYvYjQvN2YvZjkv/N2Mva29tcHl1dGVy/LmpwZw.jpg",
            "count": 15,
            "reviews": ["Отличный компьютер", "Очень понравился", "10 из 10!"],
        },
        {
            "section": "electronics",
            "label": "iPhone 15 Pro",
            "type": "smartphone",
            "price": 120000,
            "img": "https://frankfurt.apollo.olxcdn.com/v1/files/x5oavnajkjp71-KZ/image",
            "count": 25,
            "reviews": ["Быстрый, мощный", "Лучшая камера!", "Очень доволен покупкой"],
        },
        {
            "section": "audio",
            "label": "Sony WH-1000XM5",
            "type": "headphones",
            "price": 35000,
            "img": "https://avatars.mds.yandex.net/get-mpic/11620615/2a0000018e6ad4458dc001070a6528af5371/900x1200",
            "count": 10,
            "reviews": ["Шумоподавление на высоте", "Звук потрясающий!", "Лучшие наушники, что у меня были"],
        }
    ]

    context = {
        "goods": goods,
    }
    return render(request, "index.html", context)
