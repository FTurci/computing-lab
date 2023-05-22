#!/usr/bin/env python
# coding: utf-8

# # Coupled oscillators - the complete solution using initial conditions.
# 
# ## The Simple Harmonic Oscillator
# 
# Before we consider the complete solution for systems of coupled oscillators it is worth reminding ourselves of the solution for the simple harmonic oscillator problem. We remind ourselves that the simple harmonic oscillator equation is,
# 
# \begin{equation}
# m \ddot x = -k x
# \end{equation}
# where $m$ and $k$ are the mass and the spring constant respectively. We also note these are both $m$ and $k$ are real and positive. We also deduce that the frequency is $\omega= \sqrt{\frac{k}{m}}$.There are many and equivalent ways in which you might write the (trial) solution. 
# 
# ### Solutions expressed as trigonometric functions.
# 
# \begin{equation}
# x(t) = x_o \cos(\omega t +\delta) \space\space\space\space\space ...(1)
# \end{equation}
# or 
# \begin{equation}
# x(t) = x_o \sin(\omega t +\delta') \space\space\space\space\space ...(2)
# \end{equation}
# 
# we can see (1) and (2) are equivalent if $\delta' = \delta +\frac{\pi}{2}$.
# 
# We also note that these would also give 
# \begin{equation}
# \dot x(t)=-\omega x_o \sin(\omega t +\delta) \space\space\space\space\space ...(3)
# \end{equation}
# or 
# \begin{equation}
# \dot x(t)=\omega x_o \cos(\omega t +\delta') \space\space\space\space\space ...(4)
# \end{equation}
# 
# To obtain the full solution of our problem we need to determine the constants $x_o$ and $\delta$ from (1) and (3) or $x_o$ and $\delta'$ from (2) and (4). We can see that this is possible if we know the value of $x$ and $\dot x$ at a particular point in time. For example, if $x(0)=C$ and $\dot x(0) =0$ then from (1) and (3) $x_o= C$ and $\delta = 0 $ or from (2) and (4) we get $x_o=C$ and $\delta' = \frac{\pi}{2}$. The keypoint  is that we need to find two constants, the amplitude and phase (even if one of them, $\delta$ is zero).
# 
# We can also take equation (4) and use the 'double angle' trigonometric relationships to show we may also write the general solution as 
# 
# \begin{equation}
# x(t)=A \sin (\omega_0 t)+B \cos(\omega_0 t) \space\space\space\space\space ...(5)
# \end{equation}
# 
# where the amplitude and phase information are contained in the real constants $A$ and $B$.
# 
# ### Solutions expressed with complex numbers
# 
# We know that we can express the trigonometric functions with exponentials with complex arguments, i.e.
# 
# \begin{equation}
# \sin(\theta)=\frac{\exp(i\theta)-\exp(i\theta)}{2i} \space\space\text{and} \space\space \cos(\theta)=\frac{\exp(i\theta)+\exp(i\theta)}{2}
# \end{equation}
# 
# or alternatively, we can use De Moivre's theorem (or more strictly Euler's theorem which is the particular case of De Moivre's theorem when $n=1$), 
# 
# \begin{equation}
# \exp(i\theta)=cos(\theta)+i\sin(\theta)
# \end{equation}
# 
# Hence, we might expect and we do find that
# 
# \begin{equation}
# x(t)=X_0 \exp(i\omega t)
# \end{equation} 
# 
# is also a solution of the S.H.M. equation provided $\omega_0^2=\pm \frac{k}{m}$. Hence allowing for both roots we have the general solution,
# 
# \begin{equation}
# x(t)=A'\exp(i\omega_0 t)+B'\exp(-i\omega_0 t) \space\space\space\space\space ...(6)
# \end{equation}
# 
# Again, the constants $A'$ and $B'$ contain the amplitude and phase information and may be complex even though we know $x(t)$ is a real number. You should note that we can recover equation (5) if we apply De Moivre's theorem again and we recognise that $A=i(A'-B')$ and $B=A'+B'$, where now recognise that $B$ is be written as an imaginary number. 
# 
# Let's look at some examples of initial conidtions. If $x(0)=C$ and $\dot x(0)=0$ we find,
# 
# \begin{equation}
# C=A'+B' \\
# 0=-i\omega_0(A'-B')
# \end{equation}
# 
# so that we find,
# 
# \begin{equation}
# x(t)=C\cos(\omega_o t)
# \end{equation}
# 
# that corresponds to the case when the phase is $0$.
# 
# If we set $x(0)=0$ and $\dot x(0)=C'$ we find,
# 
# \begin{equation}
# 0=(A'+B') \\
# C'=-i\omega_0(A'-B')
# \end{equation}
# 
# so that we find
# 
# \begin{equation}
# x(t)=\frac{C'}{\omega_0}\sin(\omega_0 t)
# \end{equation}
# that is equivalent to
# \begin{equation}
# x(t)=C''\cos(\omega_o t-\frac{\pi}{2})
# \end{equation}
# where $C''=\frac{C'}{\omega_0}$ and we have a phase of $-\frac{\pi}{2}$.
# 
# 

# In[ ]:




