# Automatic Generation Control Using an Actor-Critic based Adaptive PID controller

This Repo contains an implementation of a Novel Actor-Critic based Adaptive PID controller for Automatic Generation Control on a Two area Power system.

Automatic Generation Control (AGC) is critical for providing quality electrical energy. In this paper, we present an Actor-Critic Reinforcement Learning (RL) based Adaptive Proportional-Integral-Derivative (PID) controller. The performance of model-based control methods relies on the accuracy of the available plant model. There is a need for adaptive controllers that, for the most part, work independently of the system configuration. The PID controller parameters are updated through an actor-critic policy in real-time. This actor-critic policy is implemented as a single RBF kernel implemented as a neural network. The input to the RBF kernel is the Area Control Error(ACE) after being passed through a state converter. The kernel outputs the updated parameters of the PID controller. We employ the gradient descent method based on the Temporal Difference (TD) error performance index to update the neural network’s weights. The neural network and the kernel are continually updated, making the controller robust and adaptive. Numerical simulations were performed, and the controller’s performance was recorded and compared to a traditional PID controller.

* To run the Python Implementation of the adaptive controller run ```twoarea_with_adaptive_pid.py```
* To run the Matlab Implementation of the adaptive controller run ``````
![main.m](https://github.com/NickNair/Adaptive-PID-controller/blob/master/matlab_implementation/main.m)
