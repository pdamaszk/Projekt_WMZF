def double_pen_ani_wyk(L1, th1, M1, L2, th2, M2):
    from numpy import sin, cos

    import matplotlib.pyplot as plt
    import scipy.integrate as integrate
    import matplotlib.animation as animation

    G = 9.8         # [m/s^2]       przyspieszenie ziemskie

    # L1 = 0.3        # [m]           dlugosc pierwszego wahadla
    # th1 = 90.0      # [stopnie]     kąt nachylenia pierwszego wahadla
    # M1 = 100.0      # [kg]          masa pierwszego wahadla
    #
    # L2 = 1.0        # [m]           dlugosc drugiego wahadla
    # th2 = -90.0     # [stopnie]     kąt nachylenia drugiego wahadla
    # M2 = 2.0        # [kg]          masa drugiego wahadla

    w1 = 0.0        # [m/s]         prędkość poczatkowa pierwszego wahadla
    w2 = 0.0        # [m/s]         prędkość poczatkowa drugiego wahadla

    dt = 0.05       # [s]           delta - dokładność obliczeń
    t = np.arange(0, 60, dt)



    def pochodna(state, t):

        dydx = np.zeros_like(state)
        dydx[0] = state[1]

        delta = state[2] - state[0]
        den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
        dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                    + M2 * G * sin(state[2]) * cos(delta)
                    + M2 * L2 * state[3] * state[3] * sin(delta)
                    - (M1+M2) * G * sin(state[0]))
                   / den1)

        dydx[2] = state[3]

        den2 = (L2/L1) * den1
        dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                    + (M1+M2) * G * sin(state[0]) * cos(delta)
                    - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                    - (M1+M2) * G * sin(state[2]))
                   / den2)

        return dydx



    # initial state
    state = np.radians([th1, w1, th2, w2])

    # integrate your ODE using scipy.integrate.
    global y
    y = integrate.odeint(pochodna, state, t)

    x1 = L1*sin(y[:, 0])
    y1 = -L1*cos(y[:, 0])

    x2 = L2*sin(y[:, 2]) + x1
    y2 = -L2*cos(y[:, 2]) + y1

    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1.1*(L1+L2), 1.1*(L1+L2)), ylim=(-1.1*(L1+L2), L1+0.5*L2))
    # ax.set_ylim([-1.1*(L1+L2), 1.1*L1])
    # ax.set_xlim([-1.1*(L1 + L2), 1.1*(L1+L2)])
    # print(np.size(y))
    ax.set_aspect('equal')
    ax.grid()

    line, = ax.plot([], [], 'o-', lw=2)
    time_template = 'time = %.2fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


    def init():
        line.set_data([], [])
        time_text.set_text('')
        return line, time_text


    def animate(i):
        thisx = [0, x1[i], x2[i]]
        thisy = [0, y1[i], y2[i]]

        line.set_data(thisx, thisy)
        time_text.set_text(time_template % (i*dt))
        return line, time_text


    ani = animation.FuncAnimation(fig, animate, range(1, len(y)),
                                  interval=dt*1000, blit=True, init_func=init)
    plt.show()