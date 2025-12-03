from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

shots_list = [1, 1000, 8000]

qc = QuantumCircuit(1)
qc.h(0)
qc_state = qc.copy()
qc.measure_all()
qc.draw(output='mpl')

state = Statevector.from_instruction(qc_state)
plot_bloch_multivector(state)
plt.show()

all_states = ['0','1']

for shots in shots_list:
    sim = AerSimulator()
    result = sim.run(qc, shots=shots).result()
    counts = result.get_counts()

    full_counts = {state: counts.get(state, 0) for state in all_states}
    plot_histogram(full_counts)
    plt.title(f"Histogram for {shots} shots")
    plt.show()
