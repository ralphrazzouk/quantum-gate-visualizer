import numpy as np
import matplotlib.pyplot as plt
import customtkinter
import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition

# INITIALIZE TKINTER
root = customtkinter.CTk()
root.title("Gate Visualizer")

# WINDOW AND FAVICON
root.geometry("560x550")
root.resizable(False, False)
root.iconbitmap(default="favicon.ico")

# COLORS AND FONTS
global mode
mode = "dark"
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green") #green, dark-blue, sweetkind
main_font = customtkinter.CTkFont(family="Poppins", size=28, weight="bold")
text_font = customtkinter.CTkFont(family="Poppins", size=22)
gate_font = customtkinter.CTkFont(family="Roboto", size=22, weight="bold")


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

# INITIALIZE CIRCUIT FUNCTION
def initialize_circuit():
    '''
    Initialize the quantum circuit.
    '''
    global circuit
    circuit = QuantumCircuit(1)

initialize_circuit()

# INITIALIZE STATE FUNCTION
def initialize_state():
    initialization = customtkinter.CTk()
    initialization.title("Set Initial State")
    initialization.geometry("1000x800")
    initialization.resizable(False, False)



    xyz_text = customtkinter.CTkFrame(initialization)
    xyz_text.pack()
    xyz_input = customtkinter.CTkFrame(initialization)
    xyz_input.pack(fill="both", expand=True)

    xyz = customtkinter.CTkTextbox(xyz_text, width=1000, height=200, font=text_font)
    xyz.pack()
    xyz_data = """Input the values x, y, and z, such that that the initial state is given by:
                                |psi> = (x, y, z)
The values of x, y, and z can be any real numbers."""
    xyz.insert("1.0", xyz_data)
    xyz.configure(state="disabled")

    x_entry = customtkinter.CTkEntry(xyz_input, font=("Poppins", 14), width=100)
    x_entry.insert("end", "1")
    x_entry.pack(pady=10)

    y_entry = customtkinter.CTkEntry(xyz_input, font=("Poppins", 14), width=100)
    y_entry.insert("end", "0")
    y_entry.pack(pady=10)

    z_entry = customtkinter.CTkEntry(xyz_input, font=("Poppins", 14), width=100)
    z_entry.insert("end", "0")
    z_entry.pack(pady=10)

    xyz_save = customtkinter.CTkButton(xyz_input, text="Set (x, y, z) State", font=main_font, command=lambda: create_vector(float(x_entry.get()), float(y_entry.get()), float(z_entry.get()), initialization))
    xyz_save.pack()




    alphabeta_text = customtkinter.CTkFrame(initialization)
    alphabeta_text.pack()
    alphabeta_input = customtkinter.CTkFrame(initialization)
    alphabeta_input.pack(fill="both", expand=True)

    bloch = customtkinter.CTkTextbox(alphabeta_text, width=1000, height=200, font=text_font)
    bloch.pack()
    bloch_data = """Input the values alpha and beta such that the initial state is given by:
                                |psi> = alpha |0> + beta |1>
The values of alpha and beta must be either real numbers in the range [-1, 1] or complex numbers in the range [-i, i]."""
    bloch.insert("1.0", bloch_data)
    bloch.configure(state="disabled")

    alpha_entry = customtkinter.CTkEntry(alphabeta_input, font=("Poppins", 14), width=100)
    alpha_entry.insert("end", "1")
    alpha_entry.pack(pady=10)

    beta_entry = customtkinter.CTkEntry(alphabeta_input, font=("Poppins", 14), width=100)
    beta_entry.insert("end", "0")
    beta_entry.pack(pady=10)

    alphabeta_save = customtkinter.CTkButton(alphabeta_input, text="Set State", font=main_font, command=lambda: create_state(float(alpha_entry.get()), float(beta_entry.get()), initialization))
    alphabeta_save.pack()

    initialization.mainloop()

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
        for gate in gates:
            gate.configure(state="disabled")

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
    rotation = customtkinter.CTk()
    rotation.title("Rotation Angle")
    rotation.geometry("600x230")
    rotation.resizable(False, False)

    pi_4 = customtkinter.CTkButton(rotation, text="pi/4", height=2, width=10, command=lambda: angle(0.25, rotation, circuit, axis))
    pi_4.grid(row=0, column=0)

    pi_2 = customtkinter.CTkButton(rotation, text="pi/2", height=2, width=10, command=lambda: angle(0.5, rotation, circuit, axis))
    pi_2.grid(row=0, column=1)

    pi = customtkinter.CTkButton(rotation, text="pi", height=2, width=10, command=lambda: angle(1, rotation, circuit, axis))
    pi.grid(row=0, column=2)

    two_pi = customtkinter.CTkButton(rotation, text="2pi", height=2, width=10, command=lambda: angle(2, rotation, circuit, axis))
    two_pi.grid(row=0, column=3, sticky="w")

    mpi_4 = customtkinter.CTkButton(rotation, text="-pi/4", height=2, width=10, command=lambda: angle(-0.25, rotation, circuit, axis))
    mpi_4.grid(row=1, column=0)

    mpi_2 = customtkinter.CTkButton(rotation, text="-pi/2", height=2, width=10, command=lambda: angle(-0.5, rotation, circuit, axis))
    mpi_2.grid(row=1, column=1)

    mpi = customtkinter.CTkButton(rotation, text="-pi", height=2, width=10, command=lambda: angle(-1, rotation, circuit, axis))
    mpi.grid(row=1, column=2)

    mtwo_pi = customtkinter.CTkButton(rotation, text="-2pi", height=2, width=10, command=lambda: angle(-2, rotation, circuit, axis))
    mtwo_pi.grid(row=1, column=3, sticky="w")

# VISUALIZE FUNCTION
def visualize(circuit, vector, window):
    '''
    Visualize the circuit on the Bloch Sphere.
    '''
    try:
        visualize_transition(circuit=circuit, initial_state=vector)
    except qiskit.visualization.exceptions.VisualizationError:
        window.destroy()

# CLEAR FUNCTION
def clear():
    '''
    Clear the screen.
    '''
    display.delete(0, "end")
    initialize_circuit()

    if (x_gate._state == "disabled"):
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, hadamard_gate]
        for gate in gates:
            gate.configure(state="normal")

# ABOUT FUNCTION
def about():
    '''
    Display information about the project.
    '''
    info = customtkinter.CTk()
    info.title("About")
    info.geometry("600x400")
    info.resizable(False, False)

    label = customtkinter.CTkLabel(info, text="About Gate Visualizer")
    label.pack()

    text = customtkinter.CTkTextbox(info, wrap="word")
    text.pack(fill="both", expand=True)

    text_data = """
    Gate Visualizer is a visualization tool for single qubit gates applied on a Block sphere.
    It is created by Ralph Razzouk.
    """
    text.insert("1.0", text_data)

    info.mainloop()

# THEME FUNCTION
def theme():
    if (mode == "dark"):
        customtkinter.set_appearance_mode("light")
        mode = "light"

    else:
        customtkinter.set_appearance_mode("dark")
        mode = "dark"


# LAYOUT
display_frame = customtkinter.CTkFrame(root)
display_frame.pack()
button_frame = customtkinter.CTkFrame(root)
button_frame.pack(fill="both", expand=True)

# SCREEN DISPLAY
display = customtkinter.CTkEntry(display_frame, justify="left", font=main_font) #, borderwidth=10, bg=background, fg="white"
display.pack(padx=3, pady=4)

# INITIALIZE
theta = 0
theta = 0
initial_state_button = customtkinter.CTkButton(button_frame, text="Set Initial State", font=main_font, command=lambda: initialize_state())
initial_state_button.grid(row=0, column=0, columnspan=3, ipady=10, sticky="ew", padx=3, pady=3)

# BUTTONS
x_gate = customtkinter.CTkButton(button_frame, text="X", font=gate_font, command=lambda: [display_gate('X'), circuit.x(0)])
y_gate = customtkinter.CTkButton(button_frame, text="Y", font=gate_font, command=lambda: [display_gate('Y'), circuit.y(0)])
z_gate = customtkinter.CTkButton(button_frame, text="Z", font=gate_font, command=lambda: [display_gate('Z'), circuit.z(0)])
x_gate.grid(row=1, column=0, ipadx=20, ipady=10, padx=3, pady=3)
y_gate.grid(row=1, column=1, ipadx=20, ipady=10, padx=3, pady=3)
z_gate.grid(row=1, column=2, ipadx=20, ipady=10, padx=3, pady=3)

Rx_gate = customtkinter.CTkButton(button_frame, text="Rx", font=gate_font, command=lambda: [display_gate('Rx'), rotation(circuit, 'x')])
Ry_gate = customtkinter.CTkButton(button_frame, text="Ry", font=gate_font, command=lambda: [display_gate('Ry'), rotation(circuit, 'y')])
Rz_gate = customtkinter.CTkButton(button_frame, text="Rz", font=gate_font, command=lambda: [display_gate('Rz'), rotation(circuit, 'z')])
Rx_gate.grid(row=2, column=0, columnspan=1, ipady=10, sticky="ew", padx=3, pady=3)
Ry_gate.grid(row=2, column=1, columnspan=1, ipady=10, sticky="ew", padx=3, pady=3)
Rz_gate.grid(row=2, column=2, columnspan=1, ipady=10, sticky="ew", padx=3, pady=3)

s_gate = customtkinter.CTkButton(button_frame, text="S", font=gate_font, command=lambda: [display_gate('S'), circuit.s(0)])
sd_gate = customtkinter.CTkButton(button_frame, text="Sd", font=gate_font, command=lambda: [display_gate('Sd'), circuit.sdg(0)])
t_gate = customtkinter.CTkButton(button_frame, text="T", font=gate_font, command=lambda: [display_gate('T'), circuit.t(0)])
td_gate = customtkinter.CTkButton(button_frame, text="Td", font=gate_font, command=lambda: [display_gate('Td'), circuit.tdg(0)])
s_gate.grid(row=3, column=0, columnspan=1, ipady=10, sticky="ew", padx=3, pady=3)
sd_gate.grid(row=3, column=1, columnspan=1, ipady=10, sticky="ew", padx=3, pady=3)
t_gate.grid(row=4, column=0, columnspan=1, ipady=10, sticky="ew", padx=3, pady=3)
td_gate.grid(row=4, column=1, columnspan=1, ipady=10, sticky="ew", padx=3, pady=3)

hadamard_gate = customtkinter.CTkButton(button_frame, text="H", font=gate_font, command=lambda: [display_gate('H'), circuit.h(0)])
hadamard_gate.grid(row=3, column=2, columnspan=1, ipady=10, rowspan=2, sticky="ewns", padx=3, pady=3)

visualize_button = customtkinter.CTkButton(button_frame, text="Visualize", font=text_font, command=lambda: visualize(circuit, vector, root))
visualize_button.grid(row=5, column=0, columnspan=3, ipady=10, sticky="ew", padx=3, pady=3)

clear_button = customtkinter.CTkButton(button_frame, text="Clear", font=text_font, command=clear)
about_button = customtkinter.CTkButton(button_frame, text="About", font=text_font, command=about)
exit_button = customtkinter.CTkButton(button_frame, text="Exit", font=text_font, command=root.destroy)
clear_button.grid(row=6, column=0, columnspan=1, ipady=10, sticky="ew", padx=3, pady=3)
about_button.grid(row=6, column=1, columnspan=1, ipady=10, sticky="ew", padx=3, pady=3)
exit_button.grid(row=6, column=2, columnspan=1, ipady=10, sticky="ew", padx=3, pady=3)



# RUN
root.mainloop()