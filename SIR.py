#simple SIR modeling based on tweet from Jeremy Howard with implementation in streamlit
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

day_sim = st.sidebar.slider('Days in timeframe', 1, 160, 160, 5)
recovered_time = st.sidebar.slider('Days to recovery', 1, 14, 10, 1)
beta = st.sidebar.slider('Beta', 0.01, 0.99, 0.2, 0.1)
gamma = st.sidebar.slider('Gamma', 1, 10, 1, 1) / recovered_time
N = st.sidebar.slider('Number of infections', 100, 100000, 1000, 100)
I = st.sidebar.slider('Infections', 0, 10, 1)
R = st.sidebar.slider('Recovered', 1, 10, 0)

S = N - I - R

res = []
for i in range(day_sim):
    diff_I = beta * S * I / N
    S -= diff_I
    diff_R = gamma*I
    R += diff_R
    I += diff_I - diff_R
    res.append ((S, I, R))
    
Ss, Is, Rs = map(np.array, zip(*res))

fig, ax = plt.subplots()
ax.plot(Ss/1000, 'b', label='Susceptibility')
ax.plot(Is/1000, 'y', label='Infected')
ax.plot(Rs/1000, 'g', label='Recovered')
ax.legend()

st.write(fig)
