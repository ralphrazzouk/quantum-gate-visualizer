# Gate Visualizer

This program is a calculator-looking application that aims to help visualizing quantum gates on a Bloch sphere. It is a visualization tool for single qubit rotations on a Block sphere.

Unfortunately, The `visualize_transition()` function has been deprecated and will be removed in the 2.0.0 release. This function had a number of limitations which limited its utility to only very specific use cases and did not fit in with the rest of the Qiskit visualization module.

## Gates

The following lists all the single-qubit gates that are implemented.

-   $X$: flips the state of the qubit. `circuit.x()`
-   $Y$: rotates the state vector about the $y$-axis. `circuit.y()`
-   $Z$: flips the phase by $\pi$ radians along `circuit.z()`
-   $R_x$: performs a parametrized rotation about the $x$-axis. `circuit.rx()`
-   $R_y$: performs a parametrized rotation about the $y$-axis. `circuit.ry()`
-   $R_z$: performs a parametrized rotation about the $z$-axis. `circuit.rz()`
-   $S$: rotates the state vector about the $z$-axis by $\frac{\pi}{2}$ radians. `circuit.s()`
-   $T$: rotates the state vector about the $z$-axis by $\frac{\pi}{4}$ radians. `circuit.t()`
-   $S_d$: rotates the state vector about the $z$-axis by $-\frac{\pi}{2}$ radians. `circuit.sdg()`
-   $T_d$: rotates the state vector about the $z$-axis by $-\frac{\pi}{4}$ radians. `circuit.tdg()`
-   $H$: the Hadamard gate that creates the state of superposition. `circuit.h()`

For $R_x$, $R_y$, and $R_z$, the input angle $\theta$ of rotation is only allowed for the range of values $\theta \in [-2\pi, 2\pi]$.

At one instance, only ten operations can be visualized.

## Important Change

The function `qiskit.visualization.visualize_transition()` was not working well with `qiskit.QuantumCircuit.initalize()` and was treating it as a quantum gate itself that was to be animated. To solve this, we can modify the code of the function `qiskit.visualization.visualize_transition()`. Specifically, we can add an argument in the function that accounts for the starting position and feed it into the `starting_pos` variable.

The function initially is

```py
    def visualize_transition(circuit, trace=False, saveas=None, fpg=100, spg=2):
```

and then becomes

```py
    def visualize_transition(circuit, trace=False, saveas=None, fpg=100, spg=2, initial_state=[0, 0, 1]):
```

after adding the argument `initial_state=[0, 0, 1]` to the end.

Additionally, somewhere in that function is a definition for the variable `starting_pos`. Initially, the variable was defined as

```py
    starting_pos = _normalize(np.array([0, 0, 1]))
```

and then becomes

```py
    starting_pos = _normalize(np.array(initial_state))
```

which is fed as an argument to the function `visualize_transition()`.

This is a very easy solution but requires some local editing of the qiskit files.
