import googlemaps
import populartimes
import config

gmaps = googlemaps.Client(key=config.api_key)

def create_card(name, addr, site, rate, color):
    return '<div class="row"><div class="col s12 m7"><div class="card ' + color+ '"><div class="card-image"><span class="card-title"></span></div><div class="card-content"><p>' + name + ' - ' + addr + '</p></div><div class="card-action"><a href="' + site +'">' + 'Site - ' + rate+'</a></div></div></div></div>'


def look_for(location, query):
    places = gmaps.places_nearby(location,radius=500,keyword=query)['results']
    total_places = ''
    colors = ['red accent-4', 'yellow accent-2', 'light-green accent-3']
    for place in places:
        pop = ""
        website = ""
        try:
            more_info = populartimes.get_id(config.api_key, place['place_id'])
            pop = more_info['current_popularity']
            rate = more_info['rating']
            if(pop >= 75):
                color = colors[0]
            elif(pop <= 30):
                color = colors[2]
            else:
                color = colors[1]
                
            website = gmaps.place(place['place_id'])['result']['website']
            total_places += create_card(place['name'], place['vicinity'], website, str(rate), color)
        except:
            pass
        
    return total_places