from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 1)
qc.x(1)
qc.barrier()
qc.h(0)
qc.h(1)
qc.barrier()
#qc.cx(0, 1)
qc.barrier()
qc.h(0)
qc.barrier()
qc.measure(0, 0)
qc.draw(output='mpl')

sim = AerSimulator()
job = sim.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()
print("Counts:", counts)

plot_histogram(counts, title='Deutsch Algorithm – Constant Function')
plt.show()
