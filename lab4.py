class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
    
    def search_by_city(self, city):
        result = [flight for flight in self.flights if flight.source == city or flight.destination == city]
        return result
    
    def search_from_city(self, city):
        result = [flight for flight in self.flights if flight.source == city]
        return result
    
    def search_between_cities(self, city1, city2):
        result = [flight for flight in self.flights if flight.source == city1 and flight.destination == city2]
        return result

def main():
    flight_table = FlightTable()
    
    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]
    
    for data in flight_data:
        flight = Flight(data[0], data[1], data[2], data[3])
        flight_table.add_flight(flight)
    
    while True:
        print("Menu:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            city = input("Enter the city: ")
            result = flight_table.search_by_city(city)
            print("Flights for", city)
            for flight in result:
                print(f"Flight ID: {flight.flight_id}, From: {flight.source}, To: {flight.destination}, Price: {flight.price}")
        
        elif choice == 2:
            city = input("Enter the city: ")
            result = flight_table.search_from_city(city)
            print("Flights from", city)
            for flight in result:
                print(f"Flight ID: {flight.flight_id}, To: {flight.destination}, Price: {flight.price}")
        
        elif choice == 3:
            city1 = input("Enter the source city: ")
            city2 = input("Enter the destination city: ")
            result = flight_table.search_between_cities(city1, city2)
            print(f"Flights from {city1} to {city2}")
            for flight in result:
                print(f"Flight ID: {flight.flight_id}, Price: {flight.price}")
        
        elif choice == 4:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
