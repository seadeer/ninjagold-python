from django.shortcuts import render, redirect
import datetime
from random import randrange

def index(request):
    print id(request)
    try:
        request.session['total']
    except:
        request.session['total'] = 100
    try:
        request.session['messages']
    except:
        request.session['messages'] = []
    context = {
        "total": request.session['total'],
        "messages": request.session['messages']
    }
    print context
    return render(request, 'ninja.html', context)

def farm(request):
    # take a random number and add to session total
    result = process_gold(request, 'farm')
    return redirect('index')

def cave(request):
    result = process_gold(request, 'cave')
    return redirect('index')

def dojo(request):
    result = process_gold(request, 'dojo')
    return redirect('index')

def dice(request):
    result = process_gold(request, 'dice')
    return redirect('index')

def restart(request):
    request.session.clear()
    return redirect('index')

def process_gold(request, location):
        print id(request)
        timestamp = datetime.datetime.now().strftime('%b %d, %H:%M')
        if location == 'farm':
            earned = randrange(2,16)
            request.session['total'] += earned
            message = "You have worked hard on the farm all day, and the farmer generously paid you %s gold for your trouble." %earned
            request.session['messages'].insert(0,{'message': message, 'timestamp': timestamp})
        
        elif location == 'cave':
            randnum = randrange(0,2)
            print ("%")*60, randnum
            if randnum == 0:
                message = "You entered a cave and meditated all day until a monk came in and kicked you out of what turned out to be his dwelling. 0 gold earned."
                print message
                request.session['total']+= 0
            elif randnum == 1:
                earned = 500
                message = "You found a treasure! %s gold added to your purse." %earned
                request.session['total'] += earned
            print("&")*60
            request.session['messages'].insert(0,{'message': message, 'timestamp': timestamp})

        elif location == 'dojo':
            randnum = randrange(0,2)
            if randnum == 0:
                message = "Shogun saw you fight during the training and deemed you too dangerous. He took all of your gold and sent you off to a remote province."
                request.session['total'] = 0
            elif randnum == 1:
                earned = randrange(1, 6)
                message = "You were training hard but got defeated by the master again. As you were lying on the mat you spied a coin lying on the floor. %s gold added to your purse." %earned
                request.session['total'] += earned
            request.session['messages'].insert(0,{'message': message, 'timestamp': timestamp})

        elif location == 'dice':
            earned = randrange (-500,1000)
            if earned > 0:
                message= "You have gambled with Shogun all night and you were on your lucky strike! You will be buying Shogun's drinks all next week. %s gold won." %earned
            else:
                message="Luck was not with you tonight and Shogun will be making fun of you the entire week. %s gold lost" %abs(earned)
            request.session['total'] += earned
            request.session['messages'].insert(0,{'message': message, 'timestamp': timestamp})

