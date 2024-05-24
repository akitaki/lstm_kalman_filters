import sys
import numpy as np
import scipy.signal
import pickle

def main(arg1,arg2):
    dof = int(arg1)
    dt = float(arg2)

    rng = np.random.default_rng()

    # Continuous-time model
    # Parameters
    m = rng.integers(1,101,size=dof)
    '''for i in range(dof):
        m[i] = rng.integers(1,101,size=dof)
    m = 100*m
    '''

    k = rng.integers(500,3000,size=dof)
    # k = 2500*k

    d = rng.integers(2,20,size=dof)
    # d = 6*d

    # State-space
    A_c = np.zeros((2*dof,2*dof))

    offset = 0
    for i in range(2*dof):
        if i % 2 == 0:
            A_c[i,i+1] = 1

        if i % 2 == 1:
            if i != 2*dof-1:
                A_c[i,i-1] = -(k[i-1-offset]+k[i-offset])/m[i-1-offset]
                A_c[i,i] = -(d[i-1-offset]+d[i-offset])/m[i-1-offset]
                A_c[i,i+1] = k[i-offset]/m[i-1-offset]
                A_c[i,i+2] = d[i-offset]/m[i-1-offset]
            else:
                A_c[i,i-1] = -k[i-dof]/m[i-dof]
                A_c[i,i] = -d[i-dof]/m[i-dof]

            if i != 1:
                A_c[i,i-3] = k[i-1-offset]/m[i-1-offset]
                A_c[i,i-2] = d[i-1-offset]/m[i-1-offset]
        
            offset += 1

    B_c = np.zeros((2*dof,dof))
    offset = 0
    for i in range(2*dof):
        if i % 2 == 1:
            B_c[i,offset] = 1/m[i-1-offset]
            offset +=1

    H_c = np.zeros((dof,2*dof))
    offset = 0
    for i in range(dof):
        H_c[i,i+offset] = 1

        offset += 1

    D_c = np.array([[0.]])
    
    d_system = scipy.signal.cont2discrete((A_c, B_c, H_c, D_c),dt)
    with open('d_system.pickle', 'wb') as f:
        pickle.dump(d_system,f)

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])


