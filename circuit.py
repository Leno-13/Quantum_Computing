import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, partial_trace
from qiskit.visualization import plot_histogram, plot_bloch_vector
import matplotlib.pyplot as plt

q = QuantumRegister(3, "q")
c = ClassicalRegister(3, "c")
qc = QuantumCircuit(q, c)
qc.x(0)
qc.z(0)
qc.barrier()
qc.h(1)
qc.cx(1, 2)
qc.barrier()
qc.cx(0, 1)
qc.h(0)
qc.measure(0, 0)
qc.measure(1, 1)
qc.barrier()
qc.cx(1, 2)
qc.cz(0, 2)
qc.barrier()
qc.z(2)
qc.x(2)
qc.measure(2, 2)


qc.draw(output='mpl')

sim = AerSimulator()
job = sim.run(qc, shots=1024)
result = job.result()

counts = result.get_counts()
print("Counts:", counts)

fig = plot_histogram(counts)

#qc_no_measure = qc.remove_final_measurements(inplace=False)
#state = Statevector.from_instruction(qc_no_measure)
#bob_state = partial_trace(state, [0, 1])  # trace out q[0] and q[1]
#plot_bloch_vector([bob_state.data[0,0].real, bob_state.data[1,0].real, bob_state.data[0,1].real])

plt.show()
