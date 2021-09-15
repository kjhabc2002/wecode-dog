import json

from django.http     import JsonResponse
from django.views    import View

from .models import Owner, Dog
# Create your views here.

class OwnerListView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
        
            Owner.objects.create(
                name=data['name'],
                email=data['email'],
                age=data['age']
            )
        except KeyError:
            return JsonResponse({'MESSAGE':'CREATED'}, status=400)
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)


    def get(self, request):
        owners = Owner.objects.all()
        result=[]

        for owner in owners:
            dogs = owner.dog_set.all()
            dog_list=[]

            for dog in dogs:
                dogs = owner.dog_set.all()
                dog_info = (
                    {
                        'name' : dog.name,
                        'age' : dog.age
                    }   
                )
                dog_list.append(dog_info)
            result.append(
                {
                    'name' : owner.name,
                    'age' : owner.age,
                    'email' : owner.email,
                    'my_dog' : dog_list
                }
            )
        return JsonResponse({'result' : result}, status=200)


class DogListView(View):
    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(
            name=data['name'],
            age=data['age'],
            owner=Owner.objects.get(id=data['owner_id'])
        )
        result=[]

        return JsonResponse({'result' : result}, status=200)
    def get(self, request):
        dogs = Dog.objects.all()

        result = []
        for dog in dogs:
            result.append(
                {
                    'name' : dog.name,
                    'age' : dog.age,
                    'owner' : dog.owner.name    
                }
                
            )
        return JsonResponse({'MESSAGE' : result}, status=200)