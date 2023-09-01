# Action_Potential_Simulation
I wrote this script to demonstrate and simulate The Hodgkin-Huxley model for a group of students.You can use any IDE to run the code, but I recommend Jupyter Lab. Make sure you install the dependencies. Remy Cohan, July 2023.
This repository contains a Python script (`action_potential_simulation.py`) that simulates the phases of an action potential. Using the power of numpy, matplotlib, and scipy, it generates an animation of the action potential waveform.

## Neurophysiology of Action Potentials

Action potentials are fundamental units of information transfer in the nervous system. Here's a brief overview of their phases:

1. **Resting Potential**: The membrane potential at which a neuron rests, usually around -70 mV.

2. **Depolarization**: A rapid increase in membrane potential driven primarily by the influx of sodium ions (Na+) into the cell.

3. **Repolarization**: Following depolarization, the membrane potential rapidly returns to the resting state. This is achieved by the outflow of potassium ions (K+) from the cell.

4. **Hyperpolarization**: The membrane potential temporarily becomes more negative than the resting potential, driven by continued outflow of K+. The neuron is less likely to fire another action potential during this phase.

## Code Breakdown

### Dependencies

**import numpy as np**
**import matplotlib.pyplot as plt**
**from matplotlib.animation import FuncAnimation**
**from scipy.interpolate import interp1d**


# Defining the Action Potential Phases
The script uses a Gaussian function to simulate the rapid rise (depolarization) and fall (repolarization) of the action potential, as well as the subsequent hyperpolarization.

- **Resting Potential**: A constant value of -70 mV.

- **Depolarization**: Modeled with a Gaussian function centered at 2.5 ms with an amplitude of 110 mV.

- **Hyperpolarization**: Modeled with another Gaussian function centered at 3.5 ms, reaching a potential of -90 mV.

### Plotting
Using `matplotlib`, the script plots the voltage changes over time to visually represent the action potential.

### Animation
The script animates the action potential using `FuncAnimation` from `matplotlib`, dynamically updating the voltage changes over the time course of the action potential.

## Usage

Run the script to generate an animation of the action potential. The generated GIF will be saved as `action_potential_Remy_Cohan.gif`.

