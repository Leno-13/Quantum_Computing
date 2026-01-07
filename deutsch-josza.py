from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

n = 4
qc = QuantumCircuit(n + 1, n)
for i in range(n):
    qc.h(i)
qc.x(n)
qc.h(n)
qc.barrier()
for i in range(n):
    qc.cx(i, n)
qc.barrier()
for i in range(n):
    qc.h(i)
qc.barrier()
qc.measure(range(n), range(n))
qc.draw(output='mpl')

sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
counts = result.get_counts()
print("counts:", counts)
plot_histogram(counts, title="Deutsch–Jozsa Algorithm")
plt.show()
