from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from numpy import pi
import matplotlib.pyplot as plt

N = 21
a = 2
n_count = 4
qc = QuantumCircuit(n_count + 1, n_count)
for q in range(n_count):
    qc.h(q)
qc.x(n_count)
for q in range(n_count):
    qc.cx(q, n_count)
for j in range(n_count):
    qc.h(j)
    for k in range(j):
        qc.cp(-pi / 2**(j - k), k, j)
qc.measure(range(n_count), range(n_count))
qc.draw(output="mpl")
plt.show()

sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
counts = result.get_counts()
print("Counts:", counts)
