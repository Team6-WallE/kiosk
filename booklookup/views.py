from django.shortcuts import render
import itertools
from django.core.mail import send_mail
# Create your views here.

def home(request):    
    return render(request, 'home.html', {})

def fac_loc(request):
    return render(request, 'fac_loc.html', {})

def req_lib(request):
    import json
    import requests
    
    if request.method == 'POST':
        user_mail = request.POST.get('UserMail')
        subject = request.POST.get('Subject')
        body = request.POST.get('Body')
        help_options = request.POST.get('HelpOptions')
        
        if str(user_mail) == "" or str(subject) == "":
            status = True
        else:
            if str(help_options) == 'HSS':
                send_mail(
                    'I would like to request for extra help by ' + subject, # subject
                    body, # message
                    user_mail, # from email
                    ['saharshini2002@gmail.com'], #to email
                )
                status = False
            elif str(help_options) == 'ENG':
                send_mail(
                    subject, # subject
                    body, # message
                    user_mail, # from email
                    ['dillys00th@gmail.com'], #to email
                )
                status = False
            elif str(help_options) == 'ICT':
                send_mail(
                    subject, # subject
                    body, # message
                    user_mail, # from email
                    ['kenneth2433@gmail.com'], #to email
                )
                status = False
            else:
                send_mail(
                    subject, # subject
                    body, # message
                    user_mail, # from email
                    ['harshini180502@gmail.com'], #to email
                )
                status = False
        
        return render(request, 'req_lib.html', {'status': status, 'name': subject})
        
    else:
        return render(request, 'req_lib.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def book_fac(request):
    return render(request, 'book_fac.html', {})

def search_results(request):
    import json
    import requests
    book_output = None
        
    if request.method == "POST":
        keyword_to_search = str(request.POST['searchkey']).lower()
        api_books = requests.get("https://kiosk-p64o4ozeh-team6-walle.vercel.app/Books/?book_name=", keyword_to_search.strip())
        api_borrows = requests.get("https://kiosk-p64o4ozeh-team6-walle.vercel.app/Borrow/", keyword_to_search.strip())
        
        try:
            api_book = json.loads(api_books.content)
            api_borrow = json.loads(api_borrows.content)
            book_output = list()
                        
            for item_book, item_borrow in itertools.zip_longest(api_book, api_borrow):
                if not keyword_to_search:
                    if str(item_book['book_id']) in str(item_borrow['book_id']):
                        item_book.update({'status' : item_borrow['status']})
                        book_output.append(item_book)
                elif str(item_book['book_name']).lower().startswith(keyword_to_search[0:4]):
                    if str(item_book['book_id']) in str(item_borrow['book_id']):
                        item_book.update({'status' : item_borrow['status']})
                        book_output.append(item_book)

        except Exception as e:
            api_book =  "Error requesting api book"

        return render(request, 'search_results.html', {'api_book': book_output,
                                                    'result': keyword_to_search})
        
# def send_email(request):
#     print("hello")
#     send_mail(
#         'Request for help', # subject
#         'I would like to request additional help', # message
#         'harshini180502@gmail.com', # from email
#         ['ammu.meenatchi@gmail.com'], #to email
#     )
#     return render(request, 'req_lib.html', {})
