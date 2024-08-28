import numpy as np
import matplotlib.pyplot as plt
import tkinter
import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition

# INITIALIZE TKINTER
root = tkinter.Tk()
root.title("Gate Visualizer")

# WINDOW AND FAVICON
root.geometry("590x625")
root.resizable(False, False)
root.iconbitmap(default="favicon.ico")

# COLORS AND FONTS
background = "#141414"
button_color = "#282828"
special_button_color = "#ff0000"
special_button_color_2 = "#f00fff"
button_font = ("Poppins", 18)
display_font = ("Poppins", 24)


# CREATE VECTOR FUNCTION
def create_vector(x, y, z, window):
    '''
    Create a vector from the given x, y, and z values.
    '''
    global vector
    vector = [x, y, z]
    print(vector)
    window.destroy()

# CREATE STATE FUNCTION
def create_state(alpha, beta, window):
    '''
    Create a vector from the given x, y, and z values.
    '''
    global state
    state = [alpha, beta]
    window.destroy()

# INITIALIZE CIRCUIT FUNTION
def initialize_circuit():
    '''
    Initialize the quantum circuit.
    '''
    global circuit
    circuit = QuantumCircuit(1)
    # circuit.initialize([1/np.sqrt(2), -1/np.sqrt(2)], qubits=circuit.qubits, normalize=True)

initialize_circuit()


# INITIALIZE STATE FUNCTION
def initialize_state():
    initialization = tkinter.Tk()
    initialization.title("Set Initial State")
    initialization.geometry("600x800")
    initialization.resizable(False, False)



    xyz_text = tkinter.Frame(initialization, bg=background, padx=10, pady=10)
    xyz_text.pack()
    xyz_input = tkinter.Frame(initialization, bg=background)
    xyz_input.pack(fill="both", expand=True)

    xyz = tkinter.Text(xyz_text, wrap="word", width=100, height=5, font=("Poppins", 12), bg=background, padx=10, pady=10, fg="white")
    xyz.pack()
    xyz_data = """Input the values x, y, and z, such that that the initial state is given by:
                                |psi> = (x, y, z)
The values of x, y, and z can be any real numbers."""
    xyz.insert("1.0", xyz_data)
    xyz.config(state="disabled")

    x_entry = tkinter.Entry(xyz_input, font=("Poppins", 14), width=10)
    x_entry.insert("end", "1")
    x_entry.pack(pady=10)

    y_entry = tkinter.Entry(xyz_input, font=("Poppins", 14), width=10)
    y_entry.insert("end", "0")
    y_entry.pack(pady=10)

    z_entry = tkinter.Entry(xyz_input, font=("Poppins", 14), width=10)
    z_entry.insert("end", "0")
    z_entry.pack(pady=10)

    xyz_save = tkinter.Button(xyz_input, text="Set (x, y, z) State", font=button_font, bg=special_button_color_2, fg="white", command=lambda: create_vector(float(x_entry.get()), float(y_entry.get()), float(z_entry.get()), initialization))
    xyz_save.pack()




    alphabeta_text = tkinter.Frame(initialization, bg=background, padx=10, pady=10)
    alphabeta_text.pack()
    alphabeta_input = tkinter.Frame(initialization, bg=background)
    alphabeta_input.pack(fill="both", expand=True)

    bloch = tkinter.Text(alphabeta_text, wrap="word", width=100, height=5, font=("Poppins", 12), bg=background, padx=10, pady=10, fg="white")
    bloch.pack()
    bloch_data = """Input the values alpha and beta such that the initial state is given by:
                                |psi> = alpha |0> + beta |1>
The values of alpha and beta must be either real numbers in the range [-1, 1] or complex numbers in the range [-i, i]."""
    bloch.insert("1.0", bloch_data)
    bloch.config(state="disabled")

    alpha_entry = tkinter.Entry(alphabeta_input, font=("Poppins", 14), width=10)
    alpha_entry.insert("end", "1")
    alpha_entry.pack(pady=10)

    beta_entry = tkinter.Entry(alphabeta_input, font=("Poppins", 14), width=10)
    beta_entry.insert("end", "0")
    beta_entry.pack(pady=10)

    alphabeta_save = tkinter.Button(alphabeta_input, text="Set State", font=button_font, bg=special_button_color_2, fg="white", command=lambda: create_state(float(alpha_entry.get()), float(beta_entry.get()), initialization))
    alphabeta_save.pack()

# GATE FUNCTION
def display_gate(gate):
    '''
    Display the gate on the screen. The maximum number of gates is 10.
    '''
    display.insert("end", gate)

    input_gates = display.get()
    num_gates = len(input_gates)
    list_gates = list(input_gates)
    search = ["R", "D"]
    doubles = [list_gates.count(i) for i in search]
    num_gates -= sum(doubles)

    if (num_gates == 10):
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, hadamard_gate]
        for gate_i in gates:
            gate_i.config(state="disabled")

# INPUT ANGLE FUNCTION
def angle(angle, window, circuit, axis):
    '''
    Change the angle of the rotation gate.
    '''
    global theta
    theta = angle * np.pi

    if (axis == 'x'):
        circuit.rx(theta, 0)
        theta = 0

    elif (axis == 'y'):
        circuit.ry(theta, 0)
        theta = 0

    elif (axis == 'z'):
        circuit.rz(theta, 0)
        theta = 0

    window.destroy()

# ROTATION FUNCTION
def rotation(circuit, axis):
    '''
    Apply a rotation gate on the circuit. Takes a user-inputted value for a rotation angle for the parametrized rotation gates.
    '''
    rotation = tkinter.Tk()
    rotation.title("Rotation Angle")
    rotation.geometry("600x230")
    rotation.resizable(False, False)

    pi_4 = tkinter.Button(rotation, text="pi/4", height=2, width=10, font=button_font, bg=button_color, fg="white", command=lambda: angle(0.25, rotation, circuit, axis))
    pi_4.grid(row=0, column=0)

    pi_2 = tkinter.Button(rotation, text="pi/2", height=2, width=10, font=button_font, bg=button_color, fg="white", command=lambda: angle(0.5, rotation, circuit, axis))
    pi_2.grid(row=0, column=1)

    pi = tkinter.Button(rotation, text="pi", height=2, width=10, font=button_font, bg=button_color, fg="white", command=lambda: angle(1, rotation, circuit, axis))
    pi.grid(row=0, column=2)

    two_pi = tkinter.Button(rotation, text="2pi", height=2, width=10, font=button_font, bg=button_color, fg="white", command=lambda: angle(2, rotation, circuit, axis))
    two_pi.grid(row=0, column=3, sticky="w")

    mpi_4 = tkinter.Button(rotation, text="-pi/4", height=2, width=10, font=button_font, bg=button_color, fg="white", command=lambda: angle(-0.25, rotation, circuit, axis))
    mpi_4.grid(row=1, column=0)

    mpi_2 = tkinter.Button(rotation, text="-pi/2", height=2, width=10, font=button_font, bg=button_color, fg="white", command=lambda: angle(-0.5, rotation, circuit, axis))
    mpi_2.grid(row=1, column=1)

    mpi = tkinter.Button(rotation, text="-pi", height=2, width=10, font=button_font, bg=button_color, fg="white", command=lambda: angle(-1, rotation, circuit, axis))
    mpi.grid(row=1, column=2)

    mtwo_pi = tkinter.Button(rotation, text="-2pi", height=2, width=10, font=button_font, bg=button_color, fg="white", command=lambda: angle(-2, rotation, circuit, axis))
    mtwo_pi.grid(row=1, column=3, sticky="w")

# VISUALIZE FUNCTION
def visualize(circuit, state, window):
    '''
    Visualize the circuit on the Bloch Sphere.
    '''
    try:
        visualize_transition(circuit=circuit, initial_state=state)
    except qiskit.visualization.exceptions.VisualizationError:
        window.destroy()

# CLEAR FUNCTION
def clear():
    '''
    Clear the screen.
    '''
    display.delete(0, "end")
    circuit = initialize_circuit()

    if (x_gate["state"] == "disabled"):
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, hadamard_gate]
        for gate in gates:
            gate.config(state="normal")

# ABOUT FUNCTION
def about():
    '''
    Display information about the project.
    '''
    info = tkinter.Tk()
    info.title("About")
    info.geometry("600x400")
    info.resizable(False, False)

    text = tkinter.Text(info, wrap="word", font=("Poppins", 12), bg=background, fg="white")
    text.pack(fill="both", expand=True)

    label = tkinter.Label(info, text="About Gate Visualizer", font=("Poppins", 18), bg=background, fg="white")
    label.config(font=("Poppins", 18))
    label.pack()

    text_data = """
    Gate Visualizer is a visualization tool for single qubit gates applied on a Block sphere.
    It is created by Ralph Razzouk.
    """
    text.insert("1.0", text_data)

    info.mainloop()


# LAYOUT
display_frame = tkinter.LabelFrame(root, bg=background)
display_frame.pack()
button_frame = tkinter.LabelFrame(root, bg=background)
button_frame.pack(fill="both", expand=True)

# SCREEN DISPLAY
display = tkinter.Entry(display_frame, width=120, font=display_font, borderwidth=10, bg=background, fg="white", justify="left")
display.pack(padx=3, pady=4)

# INITIALIZE
theta = 0
initial_state_button = tkinter.Button(button_frame, text="Set Initial State", font=button_font, bg=special_button_color_2, fg="white", command=lambda: initialize_state())
initial_state_button.grid(row=0, column=0, columnspan=3, sticky="ew", pady=1)

# BUTTONS
x_gate = tkinter.Button(button_frame, text="X", font=button_font, bg=button_color, fg="white", command=lambda: [display_gate('X'), circuit.x(0)])
y_gate = tkinter.Button(button_frame, text="Y", font=button_font, bg=button_color, fg="white", command=lambda: [display_gate('Y'), circuit.y(0)])
z_gate = tkinter.Button(button_frame, text="Z", font=button_font, bg=button_color, fg="white", command=lambda: [display_gate('Z'), circuit.z(0)])
x_gate.grid(row=1, column=0, ipadx=80, pady=1)
y_gate.grid(row=1, column=1, ipadx=80, pady=1)
z_gate.grid(row=1, column=2, ipadx=80, pady=1)

Rx_gate = tkinter.Button(button_frame, text="Rx", font=button_font, bg=button_color, fg="white", command=lambda: [display_gate('Rx'), rotation(circuit, 'x')])
Ry_gate = tkinter.Button(button_frame, text="Ry", font=button_font, bg=button_color, fg="white", command=lambda: [display_gate('Ry'), rotation(circuit, 'y')])
Rz_gate = tkinter.Button(button_frame, text="Rz", font=button_font, bg=button_color, fg="white", command=lambda: [display_gate('Rz'), rotation(circuit, 'z')])
Rx_gate.grid(row=2, column=0, columnspan=1, sticky="ew", pady=1)
Ry_gate.grid(row=2, column=1, columnspan=1, sticky="ew", pady=1)
Rz_gate.grid(row=2, column=2, columnspan=1, sticky="ew", pady=1)

s_gate = tkinter.Button(button_frame, text="S", font=button_font, bg=button_color, fg="white", command=lambda: [display_gate('S'), circuit.s(0)])
sd_gate = tkinter.Button(button_frame, text="Sd", font=button_font, bg=button_color, fg="white", command=lambda: [display_gate('Sd'), circuit.sdg(0)])
t_gate = tkinter.Button(button_frame, text="T", font=button_font, bg=button_color, fg="white", command=lambda: [display_gate('T'), circuit.t(0)])
td_gate = tkinter.Button(button_frame, text="Td", font=button_font, bg=button_color, fg="white", command=lambda: [display_gate('Td'), circuit.tdg(0)])
s_gate.grid(row=3, column=0, columnspan=1, sticky="ew", pady=1)
sd_gate.grid(row=3, column=1, columnspan=1, sticky="ew", pady=1)
t_gate.grid(row=4, column=0, columnspan=1, sticky="ew", pady=1)
td_gate.grid(row=4, column=1, columnspan=1, sticky="ew", pady=1)

hadamard_gate = tkinter.Button(button_frame, text="H", font=button_font, bg=button_color, fg="white", command=lambda: [display_gate('H'), circuit.h(0)])
hadamard_gate.grid(row=3, column=2, columnspan=1, rowspan=2, sticky="ewns", pady=1)

visualize_button = tkinter.Button(button_frame, text="Visualize", font=button_font, bg=special_button_color, fg="white", command=lambda: visualize(circuit, vector, root))
visualize_button.grid(row=5, column=0, columnspan=3, sticky="ew", pady=1)

clear_button = tkinter.Button(button_frame, text="Clear", font=button_font, bg=special_button_color, fg="white", command=clear)
about_button = tkinter.Button(button_frame, text="About", font=button_font, bg=special_button_color, fg="white", command=about)
exit_button = tkinter.Button(button_frame, text="Exit", font=button_font, bg=special_button_color, fg="white", command=root.destroy)
clear_button.grid(row=6, column=0, columnspan=1, sticky="ew", pady=1)
about_button.grid(row=6, column=1, columnspan=1, sticky="ew", pady=1)
exit_button.grid(row=6, column=2, columnspan=1, sticky="ew", pady=1)



# RUN
root.mainloop()