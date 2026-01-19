from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram, plot_state_qsphere
import matplotlib.pyplot as plt

target = "10101"
n = len(target)
qc = QuantumCircuit(n, n)
qc.h(range(n))
qc.barrier()
target_rev = target[::-1]
for i, bit in enumerate(target_rev):
    if bit == "0":
        qc.x(i)
qc.barrier()
qc.h(n-1)
qc.mcx(list(range(n-1)), n-1)
qc.h(n-1)
qc.barrier()
for i, bit in enumerate(target_rev):
    if bit == "0":
        qc.x(i)
qc.barrier()
qc.h(range(n))
qc.x(range(n))
qc.barrier()
qc.h(n-1)
qc.mcx(list(range(n-1)), n-1)
qc.h(n-1)
qc.barrier()
qc.x(range(n))
qc.h(range(n))
qc.measure(range(n), range(n))
qc.draw(output="mpl")

sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
counts = result.get_counts()
print("Results:", counts)
plot_histogram(counts)
plt.show()
