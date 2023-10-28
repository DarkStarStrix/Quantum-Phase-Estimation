# use quantum phase estimation to find the number of PI digits and print them out

import numpy as np
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram


# make a quantum class to do the quantum phase estimation
class QuantumPhaseEstimation:
    def __init__(self, unitary, eigenstate, num_qubits):
        self.unitary = unitary
        self.eigenstate = eigenstate
        self.num_qubits = num_qubits
        self.qc = QuantumCircuit(num_qubits * 2, num_qubits)

    def build_circuit(self):
        # initialize the first register to the eigenstate
        for i in range(self.num_qubits):
            if self.eigenstate[i] == '1':
                self.qc.x(i)
        # apply the hadamard gate to the second register
        for i in range(self.num_qubits, self.num_qubits * 2):
            self.qc.h(i)
        # apply the controlled unitary gate
        for i in range(self.num_qubits):
            for j in range(2 ** i):
                self.qc
        # apply the inverse quantum fourier transform
        for i in range(self.num_qubits):
            for j in range(i):
                self
            self.qc.h(i)
        # measure the first register
        for i in range(self.num_qubits):
            self.qc.measure(i, i)

    def run(self):
        # run the circuit
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.qc, backend, shots=1000)
        result = job.result()
        counts = result.get_counts(self.qc)
        # print the result
        print(counts)
        plot_histogram(counts).show()


# define the unitary matrix
unitary = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, np.pi / 2, 0, 0, 0, 0, 0, 0],
           [0, 0, np.pi / 4, 0, 0, 0, 0, 0],
           [0, 0, 0, np.pi / 8, 0, 0, 0, 0],
           [0, 0, 0, 0, np.pi / 16, 0, 0, 0],
           [0, 0, 0, 0, 0, np.pi / 32, 0, 0],
           [0, 0, 0, 0, 0, 0, np.pi / 64, 0],
           [0, 0, 0, 0, 0, 0, 0, np.pi / 128]]

# define the eigenstate
eigenstate = '00000000'

# define the number of qubits
num_qubits = 8

# create a quantum phase estimation object
qpe = QuantumPhaseEstimation(unitary, eigenstate, num_qubits)

# build the circuit
qpe.build_circuit()

# run the circuit
qpe.run()

# print the result
print('The number of PI digits is: ', qpe.num_qubits)
