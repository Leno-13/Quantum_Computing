import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, partial_trace
from qiskit.visualization import plot_histogram, plot_bloch_vector
import matplotlib.pyplot as plt

# State 1: |+>
state1 = QuantumCircuit(2)
# Initialize input to |0,0>
state1.barrier()
# Prepare the Bell state
state1.h(0)
state1.cx(0,1)
state1.measure_all()
state1.draw(output='mpl')

state2 = QuantumCircuit(2)
# Initialize input state to |1,0>
state2.x(1)
state2.barrier()
# Prepare the Bell state
state2.h(0)
state2.cx(0,1)
state2.measure_all()
state2.draw(output='mpl')

sim = AerSimulator()
job1 = sim.run(state1, shots=1024)
job2 = sim.run(state2, shots=1024)
result1 = job1.result()
result2 = job2.result()

counts1 = result1.get_counts()
counts2 = result2.get_counts()
fig1 = plot_histogram(counts1, title="Bell State |Φ+> from |00>")
fig2 = plot_histogram(counts2, title="Bell State |Ψ+> from |10>")
plt.show()