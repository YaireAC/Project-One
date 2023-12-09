
"""
#Question 1.
    #This is a class of albums to create album objects
    #An album consists of certain components: Photobook, CD, and Package
    #Within each of these components are then variables to detail them:
     #Photobook:
            -Pages = Number of pages
        #CD:
            -Songs = Number of songs in the CD
        #Package:
            -Name = Name of the album
            -Color = Color of the album
            -Fragile = Checking if the album is fragile or not
            -Price = How much the album costs
    #There are methods that would then be required throughout, such as:
        def photobook, def cd: Used for the user to set the characteristics of the album
        def packaging: Used to also set the physical aspect of the album and determine if the album will require extra packaging to set the price of the album
        def display: how to display the information of the album

    #Some tests that show that the file works is by being able to cet different numbers to the integer variables.
    Such as the number of pages, can handle any large number. Further can be displayed if desired when choosing the option to display. Also, the variables get changed if the data is updated before quiting.
    Which also exist gracefully when chosen.
"""
class Album:
    """Class to make an album"""
    def __init__(self):
        self._pages = 0
        self._songs = 0
        self._name = ""
        self._color = ""
        self._fragile = 0
        self._price = 0

    def photobook(self):
        print("how many pages are in the book?")
        self._pages = int(input())
        print("Your album has", self._pages, "pages !")

    def CD(self):
        print("how many songs are in the book?")
        self._songs = int(input())
        print("Your album has", self._songs, "songs !")

    def packaging(self):
        self._color = input("what is the color of the album? :")
        self._name = input("what is the name of the album? :")
        self._fragile = int(input("Is the album fragile or not (1-Yes 0-No): "))
        if self._fragile == 1:
            self._price = 155
        else:
            self._price = 130
        print("The price of the album is $", self._price)

    def display_info(self):
        print(f"Album Info: Name - {self._name}, Color - {self._color}, Pages - {self._pages}, Songs - {self._songs}")


def main():
    one_album = Album()

    while True:
        print("What section of the album would you like to work with?")
        print("1. Photobook")
        print("2. CD")
        print("3. Packaging")
        print("4. Display Album Info")
        print("5. Quit")

        print("Enter choice: ")
        choice = int(input())

        if choice == 1:
            one_album.photobook()
        elif choice == 2:
            one_album.CD()
        elif choice == 3:
            one_album.packaging()
        elif choice == 4:
            one_album.display_info()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("You put an invalid choice. Enter a number between 1 and 5.")
            print(" ")
if __name__ == "__main__":
        main()
