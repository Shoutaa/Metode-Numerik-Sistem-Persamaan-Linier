def x_(y, z):
    return (5 - y + z) / 3

def y_(x, z):
    return (20 - 4*x + 3*z) / 7

def z_(x, y):
    return (10 - 2*x + 2*y) / 5

def main():
    e = 0.0001 * 100
    x_sebelum, y_sebelum, z_sebelum = 0, 0, 0
    i = 2
    
    print ("| {:10} | {:10} | {:10} | {:10} | {:10} | {:10} | {:10} |".format("Iterasi", "X", "Y", "Z", "eX(%)", "eY(%)", "eZ(%)"))
    print ("| {:10} | {:10.5f} | {:10.5f} | {:10.5f} | {:10} | {:10} | {:10} |".format(1, 0, 0, 0, "-", "-", "-"))
    x, y, z = x_(y_sebelum, z_sebelum), y_(x_sebelum, z_sebelum), z_(x_sebelum, y_sebelum)
    print ("| {:10} | {:10.5f} | {:10.5f} | {:10.5f} | {:10} | {:10} | {:10} |".format(i, x, y, z, 100, 100, 100))

    while True:
        x_baru = x_(y, z)
        y_baru = y_(x, z)
        z_baru = z_(x, y)
        
        eX = abs((x_baru - x) / x_baru) * 100
        eY = abs((y_baru - y) / y_baru) * 100
        eZ = abs((z_baru - z) / z_baru) * 100

        print ("| {:10} | {:10.5f} | {:10.5f} | {:10.5f} | {:10.2f} | {:10.2f} | {:10.2f} |".format(i+1, x_baru, y_baru, z_baru, eX, eY, eZ))
        
        if eX <= e and eY <= e and eZ <= e:
            break

        x, y, z = x_baru, y_baru, z_baru
        i += 1

if __name__ == "__main__":
    main()
