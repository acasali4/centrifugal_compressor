#----------------------------------------------------------------------------------------------------------------------
#                                 SOLUZIONE IMPLICITA BILANCIO DI MASSA FLUSSO COMPRIMIBILE
#----------------------------------------------------------------------------------------------------------------------
#
# test script che implementa i metodi iterativi :
#
#   1) Regula Falsi
#   2) bisezione
#
# per la soluzione del problema implicito di chiusura del bilancio di massa sulla sezione di ingresso di un compressore
# centrifugo.
#
# La funzione obiettivo f_obj è costruita partendo dalla adimensionalizzazione della portata massica sulla sezione di efflusso
# e trattando il numero di Mach come unica variabile.
#
# la chiusura del bilancio di massa si riduce quindi alla ricerca di una radice della funzione
#
#           y = f_obj(M)
#

def main():

    import numpy as np
    import matplotlib.pyplot as plt

    pi = np.pi

    m = 3                           # portata massica,          [kg/s]
    Rh = 35e-3                      # raggio di mozzo,          [m]
    Rt = 87.5e-3                    # raggio di apice,          [m]

    p0 = 101325                     # pressione totale inlet,   [Pa]
    T0 = 293.15                     # temperatura totale inlet, [K]
    g = 1.4

    R = 8314 / (0.21*32 + 0.79*28)  # costante del gas,         [J/kmolK]

    S = pi * (Rt**2 - Rh**2)        # area di efflusso          [m^2]

    #------------------------------------------------------------------------------------------------------------------
    #                             *** PLOT FUNZIONE OBIETTIVO DA ANNULLARE ***
    # ------------------------------------------------------------------------------------------------------------------

    def f_obj(M):
        # funzione obiettivo la cui radice corrisponde alle condizioni statiche che smaltiscono la portata massica
        f_Mach = 1 + 1/2 * (g - 1) * M**2
        y = m - p0 * S / np.sqrt(R * T0) * np.sqrt(g) * M * f_Mach**((1 + g)/(2 - 2*g))
        return y

    MachVect = np.linspace(0,1,10000)

    plt.figure()
    plt.plot(MachVect, f_obj(MachVect))
    plt.plot(MachVect, 0*MachVect, linestyle='-.', color='red')
    plt.grid()
    plt.xlabel("Mach No. [-]", fontsize=25)
    plt.ylabel("objective function", fontsize=25)
    plt.title("root of implicit problem", fontsize=25)
    plt.show()

    # ------------------------------------------------------------------------------------------------------------------
    #                       *** APPROSSIMAZIONE DELLA RADICE DELLA FUNZIONE OBIETTIVO ***
    # ------------------------------------------------------------------------------------------------------------------

    # --> metodo di REGULA FALSI
    x_LOW = 0                                       # lower bound for root approximation
    x_UP = 1                                        # upper bound for root approximation
    res, toll, Niter, maxiter = 1, 1e-12, 0, 100    # initialisation of iterative parameters
    while res>toll and Niter<maxiter :

        x_GUESS = x_UP - (x_UP - x_LOW) / (f_obj(x_UP) - f_obj(x_LOW)) * f_obj(x_UP)

        if f_obj(x_GUESS) < 0:
            x_UP = x_GUESS
        else:
            x_LOW = x_GUESS

        res = np.abs(f_obj(x_GUESS))
        Niter = Niter + 1

    print("\n metodo Regula Falsi converge in : ",Niter," iterazioni, con residuo pari a : ",res,
          "\n\t soluzione approssimata Ma = ", x_GUESS)

    # --> metodo di BISEZIONE
    x_LOW = 0                                       # lower bound for root approximation
    x_UP = 1                                        # upper bound for root approximation
    res, toll, Niter, maxiter = 1, 1e-12, 0, 100    # initialisation of iterative parameters
    while res>toll and Niter<maxiter :

        x_GUESS = 0.5 * (x_UP + x_LOW)

        if f_obj(x_GUESS) < 0:
            x_UP = x_GUESS
        else:
            x_LOW = x_GUESS

        res = np.abs(f_obj(x_GUESS))
        Niter = Niter + 1

    print("\n metodo bisezione converge in : ",Niter," iterazioni, con residuo pari a : ",res,
          "\n\t soluzione approssimata Ma = ", x_GUESS)

    return None

########################################################################################################################
if __name__ == "__main__":
    main()
########################################################################################################################
