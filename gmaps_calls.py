import googlemaps
import populartimes
from multiprocessing.dummy import Pool as ThreadPool
import config

gmaps = googlemaps.Client(key=config.api_key)

def create_card(name, addr, site, rate, color):
    return '<div class="row"><div class="col s12 m7"><div class="card ' + color + '"><div class="card-image"><span class="card-title"></span></div><div class="card-content"><p>' + name + ' - ' + addr + '</p></div><div class="card-action"><a href="' + site +'">' + 'Site - ' + rate+'</a></div></div></div></div>'

def thread_search(place):
    global total_places
    colors = ['red', 'yellow accent-2', 'light-green accent-3', 'blue darken-1']
    pop = ""
    website = ""
    rate = str(place['rating'])
    try:
        print('Requesting popular times.')
        more_info = populartimes.get_id(config.api_key, place['place_id'])
        pop = more_info['current_popularity']
        if(pop >= 75):
            color = colors[0]
        elif(pop <= 30):
            color = colors[2]
        else:
            color = colors[1]
        print('Requesting website.')
        website = gmaps.place(place['place_id'])['result']['website']
        total_places += create_card(place['name'], place['vicinity'], website, rate, color)
    except:
        try:
            print('Requesting website.')
            website = gmaps.place(place['place_id'])['result']['website']
        except:
            pass
        total_places += create_card(place['name'], place['vicinity'], website, rate, colors[3])

def look_for(location, query='food', distance=500, price=4):
    print('Requesting places.')
    places = gmaps.places_nearby(location, radius=distance, keyword=query, max_price=price)['results']
    global total_places
    total_places = ''
    if not len(places):
        return total_places
    
    pool = ThreadPool(len(places))
    pool.map(thread_search, places)
    
    
    pool.close()
    pool.join()
    
    return total_places
