"""
================
Lorenz Attractor
================
"""
import numpy as np
import matplotlib.pyplot as plt

def lorenz(x, y, z, s=10, r=28, b=8/3):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

dt = 0.01
num_steps = 10000

# Need one more for the initial values
x1 = np.empty(num_steps + 1)
y1 = np.empty(num_steps + 1)
z1 = np.empty(num_steps + 1)

x2 = np.empty(num_steps + 1)
y2 = np.empty(num_steps + 1)
z2 = np.empty(num_steps + 1)

x3 = np.empty(num_steps + 1)
y3 = np.empty(num_steps + 1)
z3 = np.empty(num_steps + 1)

x4 = np.empty(num_steps + 1)
y4 = np.empty(num_steps + 1)
z4 = np.empty(num_steps + 1)

x5 = np.empty(num_steps + 1)
y5 = np.empty(num_steps + 1)
z5 = np.empty(num_steps + 1)


cnt = 250
q = 15.1
while(q < 27):
    print(cnt)
    # Set initial values
    x1[0], y1[0], z1[0] = (0., 1., 1.)
    x2[0], y2[0], z2[0] = (1., 1., 0.)
    x3[0], y3[0], z3[0] = (-1., 0., -1.)
    x4[0], y4[0], z4[0] = (-1., -1., -1.)
    x5[0], y5[0], z5[0] = (0.5, 0.5, 0.5)
    # Step through "time", calculating the partial derivatives at the current point
    # and using them to estimate the next point
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(x1[i], y1[i], z1[i], r=q)
        x1[i + 1] = x1[i] + (x_dot * dt)
        y1[i + 1] = y1[i] + (y_dot * dt)
        z1[i + 1] = z1[i] + (z_dot * dt)

        x_dot, y_dot, z_dot = lorenz(x2[i], y2[i], z2[i], r=q)
        x2[i + 1] = x2[i] + (x_dot * dt)
        y2[i + 1] = y2[i] + (y_dot * dt)
        z2[i + 1] = z2[i] + (z_dot * dt)

        x_dot, y_dot, z_dot = lorenz(x3[i], y3[i], z3[i], r=q)
        x3[i + 1] = x3[i] + (x_dot * dt)
        y3[i + 1] = y3[i] + (y_dot * dt)
        z3[i + 1] = z3[i] + (z_dot * dt)

        x_dot, y_dot, z_dot = lorenz(x4[i], y4[i], z4[i], r=q)
        x4[i + 1] = x4[i] + (x_dot * dt)
        y4[i + 1] = y4[i] + (y_dot * dt)
        z4[i + 1] = z4[i] + (z_dot * dt)

        x_dot, y_dot, z_dot = lorenz(x5[i], y5[i], z5[i], r=q)
        x5[i + 1] = x5[i] + (x_dot * dt)
        y5[i + 1] = y5[i] + (y_dot * dt)
        z5[i + 1] = z5[i] + (z_dot * dt)

    # Plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot(x1, y1, z1, 'b', lw=0.5)
    ax.plot(x2, y2, z2, 'r', lw=0.5)
    ax.plot(x3, y3, z3, 'g', lw=0.5)
    ax.plot(x4, y4, z4, 'm', lw=0.5)
    ax.plot(x5, y5, z5, 'k', lw=0.5)
    
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor "+str(q))
    
    plt.savefig('Lorenz Attractor'+str(cnt)+'.png', dpi=200)
    
    plt.show()

    q += 0.1
    cnt += 1
