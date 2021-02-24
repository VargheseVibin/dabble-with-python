fr_cities_visited = {
    "Paris" : 4  , 
    "Lille" : 1 , 
    "Nice" : 2 , 

}

travel_log = {
    "France" : fr_cities_visited , 
    "Germany" : ["Berlin" , "Munich"]
}

#print(travel_log)

def add_country_visited (country, cities_visited, visited_count):
    cy_dict = { "country" : country , 
                "cities_visited" : cities_visited , 
                "total_visits" : visited_count , 
    }
    travel_log_01.append(cy_dict)

travel_log_01 = [
    {
        "country" : "France" , 
        "citites_visited" : ["Paris" , "Lille", "Nice"] , 
        "total_visits" : 12 , 
    } , 
    {
        "country" : "Germany" , 
        "citites_visited" : ["Berlin" , "Munich", "Stuttgart"] , 
        "total_visits" : 20 , 
    }
]

a="Russia"
b=["Moscow", "Kaliningrad", "St.Petersburg"]
c=12

add_country_visited(a,b,c)

print(travel_log_01[0])
print(travel_log_01[1])
print(travel_log_01[2])


