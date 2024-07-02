import matplotlib.pyplot as plt
import numpy as np
from control import matlab as pyctrl
import csv

# set parameters
zeta = 1.0047
omega_n = 10803

# create figure
fig = plt.figure(figsize=(6, 5))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# plot bode plot
P = pyctrl.tf([omega_n**2],[1, 2*zeta*omega_n, omega_n**2])
gain, phase, w = pyctrl.bode(P, pyctrl.logspace(1,8), plot=False)

# calculate frequency ratio
frequency_ratio = w / omega_n

# plot bode plot
# set your own coordinates
ax1.plot(w/(2*np.pi), 20*np.log10(gain), label='$\omega_n$=%.3f' % omega_n)
ax1.text(10**6.3, -20, '$\zeta$=%.4f' % zeta, fontsize=10)
ax2.plot(w/(2*np.pi), phase*180/np.pi, label='$\omega_n$=%.3f' % omega_n)
ax2.text(10**6.3, -50, '$\zeta$=%.4f' % zeta, fontsize=10)

# set properties of the x-axis and y-axis
ax1.set_ylim(-90, 10); ax1.set_yticks([-80, -40, 0])
ax2.set_ylim(-190, 10); ax2.set_yticks([-180, -90, 0])

# set labels
ax1.legend(); ax1.grid(); ax1.set_xscale('log')
ax1.set_ylabel('Magnitude [dB]')
ax2.legend(); ax2.grid(); ax2.set_xscale('log')
ax2.set_xlabel('[Hz]')
ax2.set_ylabel('Phase [deg]')
fig.tight_layout()

# save as png
fig.savefig('src/openloop-2ndOrder_bodePlot.png')
print('openloop-2ndOrder_bodePlot.png is saved in src folder.')

# Save data to CSV files
# Data for ax1 (Magnitude)
with open('src/ax1_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Frequency (Hz)', 'Frequency Ratio', 'Magnitude (dB)'])
    for freq, ratio, mag in zip(w/(2*np.pi), frequency_ratio, 20*np.log10(gain)):
        writer.writerow([freq, ratio, mag])

    print('ax1_data.csv is saved in src folder.')

# Data for ax2 (Phase)
with open('src/ax2_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Frequency (Hz)', 'Frequency Ratio', 'Phase (degrees)'])
    for freq, ratio, ph in zip(w/(2*np.pi), frequency_ratio, phase*180/np.pi):
        writer.writerow([freq, ratio, ph])

    print('ax2_data.csv is saved in src folder.')
