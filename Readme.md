# Automatic Generation Control Using an Actor-Critic Based Adaptive PID Controller

This repository contains an implementation of a novel Actor-Critic based Adaptive PID controller for Automatic Generation Control (AGC) on a two-area power system.

AGC is critical for maintaining the quality and reliability of electrical energy. In this work, we present an Actor-Critic Reinforcement Learning (RL) based Adaptive Proportional-Integral-Derivative (PID) controller. Traditional model-based control methods depend heavily on the accuracy of the plant model. In contrast, this approach aims to develop an adaptive controller that operates largely independently of the system configuration.

The PID controller parameters are updated in real-time using an Actor-Critic policy. This policy is implemented through a single Radial Basis Function (RBF) kernel modeled as a neural network. The input to the RBF kernel is the Area Control Error (ACE), processed through a state converter. The kernel outputs the updated PID parameters.

Weight updates for the neural network are performed using the gradient descent method, guided by a Temporal Difference (TD) error performance index. This continuous update mechanism ensures the controller remains both robust and adaptive.

Numerical simulations were conducted, and the proposed controller's performance was compared against a traditional PID controller.

---

## Run the Implementations

- **Python Implementation**:  
  [twoarea_with_adaptive_pid.py](https://github.com/NickNair/Adaptive-PID-controller/blob/master/python_implementation/twoarea_with_adaptive_pid.py)

- **MATLAB Implementation**:  
  [main.m](https://github.com/NickNair/Adaptive-PID-controller/blob/master/matlab_implementation/main.m)

---

## Project Report

You can find the detailed report [here](https://github.com/NickNair/Adaptive-PID-controller/blob/master/Report%20-%20Adaptive%20PID%20Controller.pdf).

## Publications

- R. Muduli, N. Nair, S. Kulkarni, M. Singhal, D. Jena, and T. Moger,  
  "**Load Frequency Control of Two-Area Power System Using an Actor-Critic Reinforcement Learning Method-Based Adaptive PID Controller**,"  
  *2023 IEEE 3rd International Conference on Sustainable Energy and Future Electric Transportation (SEFET)*,  
  Bhubaneswar, India, 2023, pp. 1–6.  
  [DOI: 10.1109/SeFeT57834.2023.10245225](https://doi.org/10.1109/SeFeT57834.2023.10245225)
