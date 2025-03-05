from django.shortcuts import render
from django.http import HttpResponse

#create your views here
def index(request):
   my_context = {
      'user': 'Carlos',
      'message': 'Una saludo a la banda que la sigue cotorreando',
      'special_ofters' : [
         {
            'name' : 'Mascarilla hidratante de sabila',
            'cost' : 140.00,
            'image_url': 'static/sayonara/img/Aloeverawithicon_2048x2048.jpg',
         },
         {
            'name' : 'Consola de videojuegos portatil XE150',
            'cost' : 450.00,
            'image_url': 'static/sayonara/img/Consola.jpeg',
         },
         {
            'name' : 'Reloj de pulcera gotica de snoppy',
            'cost' : 160.00,
            'image_url': 'static/sayonara/img/reloj.jpeg',
         },
         {
            'name' : 'Camisa para caballero de algodon',
            'cost' : 200.00,
            'image_url': 'static/sayonara/img/camisa.jpeg',
         },
      ],
      'products': ['Mascarilla hidratante de sabila',
                  'Consola de videojuegos portatil XE150',
                  'Reloj de pulcera gotica de snoppy',
                  'Camisa para caballero de algodon',
                  ],
   }
   return render(request, 'sayonara/index.html', context=my_context)

