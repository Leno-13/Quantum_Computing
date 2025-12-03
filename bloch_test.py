from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

qc = QuantumCircuit(1)
qc.x(0)
qc.h(0)

state = Statevector.from_instruction(qc)
plot_bloch_multivector(state)

plt.show()
