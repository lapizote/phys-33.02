import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

series_circuit_exp = pd.read_csv("series.csv")
parallel_circuit_exp = pd.read_csv("parallel.csv")

#constants
r = 100
r_internal = 37.6
l = 0.263
v = float(5)
c = 2.2/1000000
pi = 3.1415926
twopi = 2*pi

#Series Circuit
series_exp_resonant = [0.0, 0.0]
theoretical_dict = {"Frequency (Hz)": [], "Current RMS (mA)": []}
for x in series_circuit_exp["Frequency (Hz)"]:
    freq = float(x)
    z = ( math.sqrt( ( (r+r_internal)**2 + ( freq*twopi*l - (1/(freq*twopi*c)) )**2 ) ) )
    a = ( (v/z) * 1000 ) / math.sqrt(2)
    if a > series_exp_resonant[1]:
        series_exp_resonant[0] = freq
        series_exp_resonant[1] = a
    theoretical_dict["Frequency (Hz)"].append(freq)
    theoretical_dict["Current RMS (mA)"].append(a)
series_circuit_theo = pd.DataFrame(data=theoretical_dict)

#Parallel Circuit
parallel_exp_resonant = [0.0, 0.0]
theoretical_dict = {"Frequency (Hz)": [], "Voltage RMS (V)": []}
for x in parallel_circuit_exp["Frequency (Hz)"]:
    freq = float(x)
    x_l = freq*twopi*l
    x_c = 1/(freq*twopi*c)
    phase_diff = math.atan(-x_l/r_internal)

    sin_phi = math.sin(phase_diff)
    cos_phi = math.cos(phase_diff)

    sqrt_l = math.sqrt(r_internal**2+x_l**2)

    y = [1/r + cos_phi/sqrt_l, (sin_phi/sqrt_l) + 1/x_c]
    y[0] = y[0]*r
    y[1] = y[1]*r
    y[0] = y[0] + 1
    y_mag = math.sqrt(y[0]**2 + y[1]**2)
    v_m = (v/y_mag)/math.sqrt(2)

    if v_m > parallel_exp_resonant[1]:
        parallel_exp_resonant[0] = freq
        parallel_exp_resonant[1] = v_m

    theoretical_dict["Frequency (Hz)"].append(freq)
    theoretical_dict["Voltage RMS (V)"].append(v_m)
parallel_circuit_theo = pd.DataFrame(data=theoretical_dict)
print(parallel_circuit_theo)

fig1 = plt.figure()
fig1.canvas.manager.set_window_title("Series Circuit")
ax = plt.subplot(111)
series_circuit_theo.plot(kind = 'line', x = 'Frequency (Hz)', y = 'Current RMS (mA)', ax=ax, c="red", label="Theoretical")
series_circuit_exp.plot(kind = 'scatter', x = 'Frequency (Hz)', y = 'Current RMS (mA)', ax=ax, c="blue", label="Experimental")

fig2 = plt.figure()
fig2.canvas.manager.set_window_title("Parallel Circuit")
ax = plt.subplot(111)
parallel_circuit_theo.plot(kind = 'line', x = 'Frequency (Hz)', y = 'Voltage RMS (V)', ax=ax, c="red", label="Theoretical")
parallel_circuit_exp.plot(kind = 'scatter', x = 'Frequency (Hz)', y = 'Voltage RMS (V)', ax=ax, c="blue", label="Experimental")

print(f"R^2 for Series: {r2_score(series_circuit_exp['Current RMS (mA)'], series_circuit_theo['Current RMS (mA)'])}")
print(f"R^2 for Parallel: {r2_score(parallel_circuit_exp['Voltage RMS (V)'], parallel_circuit_theo['Voltage RMS (V)'])}")
print(f"Series resonance freq: {series_exp_resonant[0]}")
print(f"Parallel resonance freq: {parallel_exp_resonant[0]}")

plt.show()