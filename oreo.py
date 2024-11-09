class Distance:
    def __init__(self):
        self.distances = {
            "moon": 384400000,    
            "mercury": 77000000000,
            "venus": 41400000000,
            "mars": 78340000000,
            "jupiter": 628730000000,
            "saturn": 1275000000000,
            "uranus": 2723950000000,
            "neptune": 4351400000000
        }

    def choose_planet(self):
        planet_name = input("Enter body name: Moon/ Mercury/ Venus/ Mars/ Jupiter/ Saturn/ Uranus/ Neptune: ").lower()
        if planet_name in self.distances:
            return planet_name
        else:
            print("Please enter a valid planet.")
            return self.choose_planet() 


class Oreo:
    def __init__(self):
        self.oreo_thickness = {
            "classic oreo": 8.3,      
            "double stuf oreo": 12.5,
            "mega stuf oreo": 14.3,
            "oreo thins": 7.1
        }

    def choose_oreo(self):
        oreo_name = input("Enter Oreo name: Classic Oreo/ Double Stuf Oreo/ Mega Stuf Oreo/ Oreo Thins: ").lower()
        if oreo_name in self.oreo_thickness:
            return oreo_name
        else:
            print("Please choose a valid Oreo.")
            return self.choose_oreo()  

    def calculate_oreos_to_planet(self, planet, oreo_name, distance_class):
        oreo_thickness_m = self.oreo_thickness[oreo_name] / 1000  
        distance_to_planet = distance_class.distances[planet]
        number_of_oreos = distance_to_planet / oreo_thickness_m
        print(f"It would take {number_of_oreos:,.2f} {oreo_name}s to reach {planet.capitalize()}.")



def main():
    oreo_instance = Oreo()
    distance_instance = Distance()

    selected_oreo = oreo_instance.choose_oreo()

    selected_planet = distance_instance.choose_planet()

    oreo_instance.calculate_oreos_to_planet(selected_planet, selected_oreo, distance_instance)

main()



