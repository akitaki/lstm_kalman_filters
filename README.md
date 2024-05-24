# LSTM Kalman Filters
PyTorch LSTMs for state estimation of dynamical systems. Test systems include 1) spring-mass-damper, 2) cantilever beam, 3) randomly generated LTI system. Also includes parallelized KF implementation for each system.
Data is for a simulated 10 degrees-of-freedom spring-mass-damper system, discretized using Zero-order hold. Higher order systems can be simulated by modifying the dof variable in the KF notebook.
