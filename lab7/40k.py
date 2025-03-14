import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

df_40k_chargeexp = pd.read_csv("40kohm-charge.csv")
df_40k_dischargeexp = pd.read_csv("40kohm-discharge.csv")

#40k charge
theoretical_dict = {"Time (s)": [], "Voltage (V)": []}
for x in df_40k_chargeexp["Time (s)"]:
    time = float(x)
    r = float(40000)
    c = float(100*10**(-6))
    e = float(20)
    alpha = float(2)
    v = float(e/alpha)*(1-math.exp(-(alpha*time)/(r*c)))
    theoretical_dict["Time (s)"].append(time)
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

print(f"R^2 for Charging, 40 kOhms: {r2_score(df_40k_chargeexp['Voltage (V)'], df_40k_chargetheo['Voltage (V)'])}")
print(f"R^2 for Discharging, 40 kOhms: {r2_score(df_40k_dischargeexp['Voltage (V)'], df_40k_dischargetheo['Voltage (V)'])}")
print(df_40k_chargeexp)
print(df_40k_chargetheo)
plt.show()

#print(df["Time (s)"])