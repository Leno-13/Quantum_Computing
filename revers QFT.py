from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.visualization import plot_bloch_multivector, plot_histogram, plot_state_qsphere
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
from numpy import pi

#might be useful
#def qft(n):
#    qc = QuantumCircuit(n)
#    for j in range(n):
#        qc.h(j)
#        for k in range(j + 1, n):
#            qc.cp(pi / 2**(k - j), k, j)
#    for i in range(n // 2):
#        qc.swap(i, n - i - 1)
#    return qc

n = 3
qc = QuantumCircuit(n, n )
qc.x(1)
qc.x(2)
qc.barrier()

# Save state before measurement
qc_state = qc.copy()
qc.swap(0, 2)
qc.barrier()
qc.h(0)
qc.cp(-pi/2, 0, 1)
qc.h(1)
qc.cp(-pi/4, 0, 2)
qc.cp(-pi/2, 1, 2)
qc.h(2)
qc.measure_all()

qc.draw(output="mpl")
state = Statevector.from_instruction(qc_state)
plot_bloch_multivector(state)
plot_state_qsphere(state)
plt.show()