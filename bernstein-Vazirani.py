from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

ssh = "11010"
n = len(ssh)
qc = QuantumCircuit(n + 1, n)
for i in range(n):
    qc.h(i)
qc.x(n)
qc.h(n)
qc.barrier()
print("Secret before reverse:", ssh)
ssh = ssh[::-1]
print("Secret after reverse: ", ssh)
for i, bit in enumerate(ssh):
    if bit == "1":
        qc.cx(i, n)
qc.barrier()
for i in range(n):
    qc.h(i)
qc.barrier()
qc.measure(range(n), range(n))
qc.draw(output="mpl")

sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
counts = result.get_counts()
print("Measurement results:", counts)
plot_histogram(counts, title="Bernstein–Vazirani Algorithm")
plt.show()
