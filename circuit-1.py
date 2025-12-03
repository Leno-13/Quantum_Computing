import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

qc.x(1)
qc.barrier()
qc.h(0)
qc.cx(0, 1)
qc.measure(q,c)
qc.barrier()
qc.draw(output='mpl')


sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
counts = result.get_counts()

print("Counts:", counts)
fig = plot_histogram(counts)

plt.show()