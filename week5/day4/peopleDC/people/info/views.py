from django.shortcuts import render
from django.http import HttpResponse

name = 'Bob Smith'
age = 35
country = 'USA'


def display_person(request):
    info = f"{name}, {age}, {country}"
    return HttpResponse(info)


people = ['bob', 'martha', 'fabio', 'john']


def display_people(request):
    people.sort()
    result = ''
    for person in people:
        result += person.capitalize() + '\n'
    return HttpResponse(result)


all_people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def display_all_people(request):
    newlist = sorted(all_people, key=lambda d: d['age'])
    result = ''
    for person in newlist:
        result += f"{person['name']}, {person['age']}, {person['country']} |"
    return HttpResponse(result)
