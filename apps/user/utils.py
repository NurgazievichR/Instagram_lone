from django.db.models import Q
from django.shortcuts import render

from apps.user.models import CustomUser


def transliterate(name):
   """
   Автор: LarsKort
   Дата: 16/07/2011; 1:05 GMT-4;
   Не претендую на "хорошесть" словарика. В моем случае и такой пойдет,
   вы всегда сможете добавить свои символы и даже слова. Только
   это нужно делать в обоих списках, иначе будет ошибка.
   """
   # Слоаврь с заменами
   slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
      'ц':'c','ч':'ch','ш':'sh','щ':'sch','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'u','я':'ya', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'YO',
      'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
      'Ц':'C','Ч':'CH','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
      'Ю':'U','Я':'YA',',':'','?':'',' ':'_','~':'','!':'','@':'','#':'',
      '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
      ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
      '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
      'Є':'e', '—':''}
        
   # Циклически заменяем все буквы в строке
   for key in slovar:
      name = name.replace(key, slovar[key])
   return name

def clean_username(request):
   me = CustomUser.objects.get(username=request.user.username)
   if len(request.POST['username'])<155 and not CustomUser.objects.filter(username=request.POST['username']):
      return True
   elif CustomUser.objects.filter(username=request.POST['username']) and request.POST['username'] == request.user.username:
      return True
   else:
      return False

def get_id_by_username(username):
   object = CustomUser.objects.get(username=username)
   return object.id


def paginate_posts(a:int, b:int):
    while True:
        yield a
        a+=b



