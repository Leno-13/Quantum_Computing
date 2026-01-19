from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.visualization import plot_bloch_multivector, plot_histogram, plot_state_qsphere
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
from numpy import pi

s = "10110"
n = len(s)
qc = QuantumCircuit(n)
s = s[::-1]
for i in range(n):
    if s[i] == "1":
        qc.x(i)
qc.barrier()
qc.h(4)
qc.cp(pi / 2, 1, 4)
qc.cp(pi / 4, 0, 4)
qc.cp(pi / 8, 1, 4)
qc.cp(pi / 16, 0, 4)
qc.barrier()
qc.h(3)
qc.cp(pi / 2, 1, 3)
qc.cp(pi / 4, 0, 3)
qc.cp(pi / 8, 0, 3)
qc.barrier()
qc.h(2)
qc.cp(pi / 2, 1, 2)
qc.cp(pi / 4, 0, 2)
qc.barrier()
qc.h(1)
qc.cp(pi / 2, 0, 1)
qc.barrier()
qc.h(0)
qc.barrier()
def add_swap_gates(circuit, num_qubits):
    for i in range(num_qubits // 2):
        circuit.swap(i, num_qubits - i - 1)
    return circuit
qft_circuit = add_swap_gates(qc, n)

qft_circuit.draw(output="mpl")
state = Statevector.from_instruction(qft_circuit)
plot_bloch_multivector(state)
plot_state_qsphere(state)
plt.show()