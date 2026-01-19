from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

shh = "011"
n = len(shh)
total_qubits = 2 * n
qc = QuantumCircuit(total_qubits, total_qubits)
qc.h(range(n))
qc.barrier()
for idx in range(n):
    if shh[idx] == "1":
        for j in range(n):
            qc.cx(idx, n + j)

qc.barrier()
qc.h(range(n))
qc.barrier()
qc.measure(range(total_qubits), range(total_qubits))
qc.draw(output="mpl")

sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
counts = result.get_counts()
print("Counts:", counts)
plot_histogram(counts, title="Simon Circuit Output")
plt.show()
sub_results = {}

for bitstring, count_value in counts.items():
    bitstring = bitstring[::-1]
    input_bits = bitstring[:n]
    if input_bits in sub_results:
        sub_results[input_bits] += count_value
    else:
        sub_results[input_bits] = count_value
print("Sub results: ", sub_results)
plot_histogram(sub_results, title="Sub results")
plt.show()