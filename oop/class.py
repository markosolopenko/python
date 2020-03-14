

# from oop.person import person

# print(person)

class Car:

    number_of_wheels = 4
    speed = 100

    def __init__(self, brand, year_produced):
        self.brand = brand
        self.year_produced = year_produced
        self.__unwanted = 'some_unwanted_field'

    def __unwanted_print(self):
        print(f'Hello {self.__unwanted}')

    def do_stuff(self):
        self.__unwanted_print()

    @classmethod
    def change_n_of_wheels(cls, new_number_of_wheels):
        cls.number_of_wheels = new_number_of_wheels

    @classmethod
    def from_string(cls, info_string):
        brand, year_produced = info_string.split(' ')

        cls.play_music('Love')
        return cls(brand, int(year_produced))

    # def __str__(self):
    #     return f'Car: {self.brand}, {self.year_produced}'

    def ride(self, distance):
        print(f'The car {self.brand} has ridden for {distance} miles')

    def repair(self):
        pass

    def crash(self):
        pass

    @staticmethod
    def play_music(song):
        print(f'Song {song} is playing')

    @classmethod
    def distance(cls, time):
        return time * cls.speed

    @property
    def full_name(self):
        return f'{self.brand} {self.year_produced}'

    def __eq__(self, other):
        if isinstance(other, Car):
            if self.brand == other.brand and self.year_produced == other.year_produced:
                return True
            return False
        return False

    def __dict__(self):
        return {
            'brand': self.brand,
            'year_produced': self.year_produced,
            'distance': self.number_of_wheels,
            'speed': self.speed
        }



if __name__ == "__main__":

    car_list = [
        Car('Toyota', 1997),
        Car('Mazda', 2000),
        Car('Volkswagen', 2005)
    ]

    # my_new_car = Car('Volkswagen', 2005)
    # my_new_car.ride(100)

    car_original = Car('Volvo', 1999)
    car_from_str = Car.from_string('Volvo 1999')

    another_reference = car_original


    print(car_original == car_from_str)
    print(car_original == another_reference)

    print(car_original)
    print(car_from_str)
    print(another_reference)


    # car_from_str.change_n_of_wheels(6)

    # print(car_from_str.number_of_wheels)
    # print(car_original.number_of_wheels)

    # print(car_original.full_name)



    print()

    # for x in car_list:
    #     print(x.number_of_wheels)
    #     # print(x.number_of_wheels)
    #     # print(x.number_of_wheels)
