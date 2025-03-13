import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

df_20k_chargeexp = pd.read_csv("20kohm-charge.csv")
df_20k_dischargeexp = pd.read_csv("20kohm-discharge.csv")
df_40k_chargeexp = pd.read_csv("40kohm-charge.csv")
df_40k_dischargeexp = pd.read_csv("40kohm-discharge.csv")

#20k charge
theoretical_dict = {"Time (s)": [], "Voltage (V)": []}
for x in df_20k_chargeexp["Time (s)"]:
    time = float(x)
    r = float(20000)
    c = float(100*10**(-6))
    e = float(10)
    v = float(e)*(1-math.exp(-time/(r*c)))
    theoretical_dict["Time (s)"].append(time)
    theoretical_dict["Voltage (V)"].append(v)
df_20k_chargetheo = pd.DataFrame(data=theoretical_dict)
print("Done theoretical 20k charge!")

#20k discharge
theoretical_dict = {"Time (s)": [], "Voltage (V)": []}
for x in df_20k_dischargeexp["Time (s)"]:
    time = float(x)
    r = float(20000)
    c = float(100*10**(-6))
    e = float(10)
    v = float(e)*(math.exp(-time/(r*c)))
    theoretical_dict["Time (s)"].append(time)
    theoretical_dict["Voltage (V)"].append(v)
df_20k_dischargetheo = pd.DataFrame(data=theoretical_dict)
print("Done theoretical 20k discharge!")

#40k charge
theoretical_dict = {"Time (s)": [], "Voltage (V)": []}
for x in df_40k_chargeexp["Time (s)"]:
    time = float(x)
    r = float(40000)
    c = float(100*10**(-6))
    e = float(10)
    v = float(e)*(1-math.exp(-time/(r*c)))
    theoretical_dict["Time (s)"].append(time-3)
    theoretical_dict["Voltage (V)"].append(v)
df_40k_chargetheo = pd.DataFrame(data=theoretical_dict)
print("Done theoretical 40k charge!")

#40k discharge
theoretical_dict = {"Time (s)": [], "Voltage (V)": []}
for x in df_40k_dischargeexp["Time (s)"]:
    time = float(x)
    r = float(40000)
    c = float(100*10**(-6))
    e = float(10)
    v = float(e)*(math.exp(-time/(r*c)))
    theoretical_dict["Time (s)"].append(time)
    theoretical_dict["Voltage (V)"].append(v)
df_40k_dischargetheo = pd.DataFrame(data=theoretical_dict)
print("Done theoretical 40k discharge!")

fig1 = plt.figure()
fig1.canvas.manager.set_window_title("Charging, 20kOhms")
ax = plt.subplot(111)
df_20k_chargetheo.plot(kind = 'line', x = 'Time (s)', y = 'Voltage (V)', ax=ax, c="red", label="Theoretical")
df_20k_chargeexp.plot(kind = 'scatter', x = 'Time (s)', y = 'Voltage (V)', ax=ax, c="blue", label="Experimental")

fig2 = plt.figure()
fig2.canvas.manager.set_window_title("Discharging, 20kOhms")
ax = plt.subplot(111)
df_20k_dischargetheo.plot(kind = 'line', x = 'Time (s)', y = 'Voltage (V)', ax=ax, c="red", label="Theoretical")
df_20k_dischargeexp.plot(kind = 'scatter', x = 'Time (s)', y = 'Voltage (V)', ax=ax, c="blue", label="Experimental")

fig3 = plt.figure()
fig3.canvas.manager.set_window_title("Charging, 40kOhms")
ax = plt.subplot(111)
df_40k_chargetheo.plot(kind = 'line', x = 'Time (s)', y = 'Voltage (V)', ax=ax, c="red", label="Theoretical")
df_40k_chargeexp.plot(kind = 'scatter', x = 'Time (s)', y = 'Voltage (V)', ax=ax, c="blue", label="Experimental")

fig4 = plt.figure()
fig4.canvas.manager.set_window_title("Discharging, 40kOhms")
ax = plt.subplot(111)
df_40k_dischargetheo.plot(kind = 'line', x = 'Time (s)', y = 'Voltage (V)', ax=ax, c="red", label="Theoretical")
df_40k_dischargeexp.plot(kind = 'scatter', x = 'Time (s)', y = 'Voltage (V)', ax=ax, c="blue", label="Experimental")

print(f"R^2 for Charging, 20 kOhms: {r2_score(df_20k_chargeexp["Voltage (V)"], df_20k_chargetheo["Voltage (V)"])}")
print(f"R^2 for Discharging, 20 kOhms: {r2_score(df_20k_dischargeexp["Voltage (V)"], df_20k_dischargetheo["Voltage (V)"])}")

print(f"R^2 for Charging, 40 kOhms: {r2_score(df_40k_chargeexp["Voltage (V)"], df_40k_chargetheo["Voltage (V)"])}")
print(f"R^2 for Discharging, 40 kOhms: {r2_score(df_40k_dischargeexp["Voltage (V)"], df_40k_dischargetheo["Voltage (V)"])}")

plt.show()

#print(df["Time (s)"])