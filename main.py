import numpy as np

pi = np.pi


def main():

    # parametri di progetto
    # -------------------------------------------------------------------------------------------------------------------

    p00 = 101325 # [Pa]
    T00 = 293.15 # [K]
    R = 8314 / (0.21*32 + 0.79*28) #[J/kgK]
    d00 = p00 / (R * T00)

    g = 1.4
    cp = g * R / (g - 1)

    m = 3

    betaTT = 2
    l_isoS = cp * T00 * (betaTT**((g - 1)/g) - 1)

    D2 = 400
    R2 = D2 / 2

    n = 25000
    omega = 2 * pi * n / 60

    # determinazione hub radius
    #-------------------------------------------------------------------------------------------------------------------
    # verifica resistenza a snervamento (Ry = 350 [Mpa]) trasmettendo una coppia corrispondente a
    # efficienzaTT  = 80  [%]
    # safety factor = 1.5 [-]
    #
    # Dmin = 15.2 [mm]

    D1hub = 35
    R1hub = D1hub / 2

    # impeller outlet section design




    return None

if __name__ == "__main__":
    main()