import badger2040
import rand_string.rand_string as rand


badger = badger2040.Badger2040()

badger.pen(0)

a = rand.RandString("alphanumerical", 100) + "\n"
print(a)

badger.text("UUID creator", 20, 20)

badger.update()




# Check that there is a uuid.txt, if not preload
try:
    text = open("qrcodes/01_uuid.txt", "r")
    print ("UUID exists")
    badger.text("UUID already created", 20,60,scale=0.5)
    badger.update()

except OSError:
    with open("qrcodes/01_uuid.txt", "w") as f:
        f.write(a)
        f.write("Device UUID")
        badger.text("UUID created", 20,60,scale=0.5)
        badger.update()
    
badger.text("Returning to OS", 20,80,scale=0.5)
badger.update()
badger.clear()


