__author__ = 'paul'

SIZE = 'Size'
OCCUPIED = 'Occupied'
PRICE = 'Price'
MUSIC = 'Music'
LOCATION = 'Location'
VIP = 'VIP'
BEER = 'Favorite Beer'
ENJOY = 'Enjoy'

class Row:
    def __init__(self, size, occupied, price, music, location, vip, beer, enjoyed):
        self.attr = {
            SIZE: size,
            OCCUPIED: occupied,
            PRICE: price,
            MUSIC: music,
            LOCATION: location,
            VIP: vip,
            BEER: beer,
            ENJOY: enjoyed
        }
        return

    def printRow(self):
        print(self.attr)

attributes = {
    SIZE: ['Large', 'Medium', 'Small'],
    OCCUPIED: ['High', 'Moderate', 'Low'],
    PRICE: ['Expensive', 'Normal', 'Cheap'],
    MUSIC: ['Loud', 'Quiet'],
    LOCATION: ['Talpiot', 'City-Center', 'Mahane-Yehuda', 'Ein-Karem', 'German-Colony'],
    VIP: ['Yes', 'No'],
    BEER: ['Yes', 'No'],
    ENJOY: ['Yes', 'No']
}

allnontargetattributes = [SIZE, OCCUPIED, PRICE, MUSIC, LOCATION, VIP, BEER]

ordinal = {
    SIZE: 0,
    OCCUPIED: 1,
    PRICE: 2,
    MUSIC: 3,
    LOCATION: 4,
    VIP: 5,
    BEER: 6,
    ENJOY: 7
}

