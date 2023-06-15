#The functions of all possible suvat equation conbanations
def No_AT(S, U, V):
    A = round((V**2 - U**2) / (2*S), 5)
    T = round(2*S / (U + V), 5)
    return A, T

def No_VT(S, U, A):
    V = [round((U**2 + 2*A*S)**(1/2), 5), round(-(U**2 + 2*A*S)**(1/2), 5)]
    T = [round(((2*A*S + U**2)**(1/2) - U) / A, 5), round((-(2*A*S + U**2)**(1/2) - U) / A, 5)
    ]
    return V, T

def No_VA(S, U, T):
    V = round((2*S/T) - U, 5)
    A = round((2*(S - U*T)) / (T**2), 5)
    return V, A

def No_UT(S, V, A):
    U = round((V**2 - 2*A*S)**(1/2), 5)
    T = round((V - (V**2 - 2*A*S)**(1/2)) / A, 5)
    return U, T

def No_UA(S, V, T):
    U = round((2*S / T) - V, 5)
    A = round((2*(V*T - S)) / (T**2), 5)
    return U, A

def No_UV(S, A, T):
    U = round((2*S - A*T**2) / (2*T), 5)
    V = round((2*S + A*T**2) / (2*T), 5)
    return U, V

def No_ST(U, V, A):
    S = round((V**2 - U**2) / (2*A), 5)
    T = round((V - U) / A, 5)
    return S, T

def No_SA(U, V, T):
    S = round((T/2)*(U + V), 5)
    A = round((V - U) / T, 5)
    return S, A

def No_SV(U, A, T):
    S = round((U*T) + (0.5*A*T**2), 5)
    V = round(U + A*T, 5)
    return S, V
    
def No_SU(V, A, T):
    S = round(V*T - 0.5*A*(T**2), 5)
    U = round(V - A*T, 5)
    return S, U
    