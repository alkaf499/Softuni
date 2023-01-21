class Smartphone():
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False


    def power(self):
        self.is_on = True

        
    def install(self, app, app_memory):
        if self.memory - app_memory >= 0 and self.is_on == True:
            self.memory -= app_memory
            self.apps.append(app)
            return f"Installing {app}"

        elif self.memory - app_memory >= 0 and self.is_on == False:
            return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
      
///
import unittest

class Tests(unittest.TestCase):
    def test_init(self):
        phone = Smartphone(50)
        self.assertEqual(phone.apps, [])
        self.assertEqual(phone.memory, 50)
        self.assertEqual(phone.is_on, False)
        
    def test_power(self):
        phone = Smartphone(50)
        self.assertEqual(phone.is_on, False)
        phone.power()
        self.assertEqual(phone.is_on, True)
        
    def test_install_successfull(self):
        phone = Smartphone(25)
        phone.power()
        res = phone.install("Spotify", 10)
        self.assertEqual(res, "Installing Spotify")
        
    def test_install_unsuccessfull_not_on(self):
        phone = Smartphone(25)
        res = phone.install("Word", 10)
        self.assertEqual(res, "Turn on your phone to install Word")
        
    def test_install_unsuccessfull_no_memory(self):
        phone = Smartphone(25)
        phone.power()
        res = phone.install("Excel", 30)
        self.assertEqual(res, "Not enough memory to install Excel")
        
    def test_status(self):
        phone = Smartphone(200)
        phone.power()
        phone.install("Powerpoint", 40)
        res = phone.status()
        self.assertEqual(res, "Total apps: 1. Memory left: 160")
        

if __name__ == "__main__":
   unittest.main()
