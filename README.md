# COMP4900-TrafficSimulation

Python simulation used to test effectivness of transit signal priority system. Models each car as individual drivers with different attributes.

## Authors
- Callum MacLeod 
- Kyuri Jung


## Required Modules
- PySimpleGui
- PyGame

## Instructions to Run:
Create a results/ folder in main directory

To see visualization of simulation run Main.py

Change any constants that you wish or keep defaults and launch simulation

To perform large numbers of simulations refer to RunSimulation.py and modify variables as required for desired result.

It is **recommended** to run large simulations using PyPy3. PyPy3 is an alternative interpreter for python designed to speed up execution. It is able to run simulations at over 20x the speed. It cannot be used when the simulation is ran visually.

## Info

After each simulation the stats will be saved to the results folder. Results can then be analyzed further using the numerous harvest utilities. Ensure that the path provided to the utilities points to a folder that contains subfolders as it is designed to compare numerous simulations with similar parameters.