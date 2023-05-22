#!/usr/bin/env python
# coding: utf-8

# # Coupled Oscillators - a worked example of the Eigenvalue and Eigenvector analysis.

# ## Introduction

# In mathematics part of PHYS10008 you have considered the case of coupled oscillators as an example of finding eigenvectors and eigenvalues. As you will have realised from the lectures, the full solution to these problems often entails tedious matrix calculations (finding determinants etc.) that are very prone to simple errors in calculation. In practise computers are very good at handling these linear algebra problems. The idea of this work book is that you should begin to appreciate the physics of the solutions to these problem and what they mean, without getting bogged down in calculation. This said, you should make sure that you are able to solve eigenvalue/eigenvector problems for simple 2 or 3 particle coupled systems.
# 
# Before we move on let's consider the general scheme for approaching these problems.
# 
# In 1 dimension a coupled oscillator system  we typically consider a series of masses that are connected together by springs. Two different types of end condition are considered: one where the masses at the end are free and one where they are connected to a rigid wall (infinite mass) with a final spring. We will consider both.  Note, questions will almost always state that you should consider small oscillations, in which case you can assume the potential will be parabolic (i.e. $\propto x^2$.)  You should be able to demonstrate this by considering a Taylor expansion for any sensible 'bowl' like potential. Typical examples of coupled oscillator systems include springs, coupled pendulums, coupled LCR circuits or even the interatomic potentials between atoms - in the end the maths is the same.  
# 
# For our typical mechanics questions it is the solution for the position of the masses as a function of time that we seek.(In coupled LCR circuits charge is the oscillating quantity and the inductance $L$ and capacitance $C$ take the place of the mass and spring respectively. $R$ gives rise to damping in the system). 
# 
# We will first concentrate on the steps needed to solve the problem using the example given the maths lectures.

# ## Step 1 - The formulation of the coupled oscillator equations

# In order to solve this problem we need to apply Newtons second law of motion to each of the masses in turn. We should remember that we will specify the coordinate of each mass $m_1$, $m_2$ in terms of their coordinates $x_1$ and $x_2$ that are defined as zero when the masses are in their equilibrium positions. Hence we should obtain,
# 
# \begin{equation}
# m_1 \ddot x_1 = -k_1x_1+k_2(x_2-x_1) \\
# m_2 \ddot x_2 = -k_3x_2+k_2(x_1 -x_2)
# \end{equation}
# 
# The trickiest part here is getting the signs correct. For the coupling terms (for example the term including $k_2$) setting either $x_1=0$ or $x_2 = 0$ is often sufficient to check the signs are correct. You should also note by Newton's third law that the force acting between the masses should be equal and opposite for each one. We can write these equations in matrix form as:
# 
# \begin{equation}
# \left [ \begin{array}{cc} m_1 & 0 \\ 0 & m_2 \end{array} \right ]
# \left [ \begin{array}{c} \ddot x_1 \\ \ddot x_2 \end{array} \right ]=
# \left [ \begin{array}{cc} -(k_1+k_2) & k_2 \\ k_2 & -(k_2 +k_3) \end{array} \right ]
# \left [ \begin{array}{c} x_1 \\ x_2 \end{array} \right ]
# \end{equation}
# 
# This is the equation we need to solve. 
# 
# At this stage, we will confine ourself to the case $m_1 = m_2= m $. We'll come back to what this means and how we deal with the case $m_1 \neq m_2$ later. In this case we get,
# 
# \begin{equation}
# \left [ \begin{array}{c} \ddot x_1 \\ \ddot x_2 \end{array} \right ]=\frac{1}{m}
# \left [ \begin{array}{cc} -(k_1+k_2) & k_2 \\ k_2 & -(k_2 +k_3) \end{array} \right ]
# \left [ \begin{array}{c} x_1 \\ x_2 \end{array} \right ]
# \end{equation}.
# 
# As an example let's choose $k_2 = 2k_1=2k_3=2k$ (you can change them later in this work sheet if you wish to experiment with different values). In this case we have the equation,
# 
# \begin{equation}
# \left [ \begin{array}{c} \ddot x_1 \\ \ddot x_2 \end{array} \right ]=-\frac{k}{m}
# \left [ \begin{array}{cc} 3 & -2 \\ -2 & 3 \end{array} \right ]
# \left [ \begin{array}{c} x_1 \\ x_2 \end{array} \right ] \space\space ... (1)
# \end{equation}.
# 
# Note that, provided all the masses are equal this matrix is real and symmetric. 

# ## Step 2 - The trial solution
# 
# Formally we need to solve these coupled differential equations. However, the solutions are well known and closely related to the (uncoupled) simple harmonic oscillator equation where trial solutions of the form $x=C\exp(i\omega t)$ are used. In a similar way we will choose a trial solution for this problem of the form,
# 
# \begin{equation}
# \left[ \begin{array}{c} x_1 \\x_2 \end{array} \right] = \left[ \begin{array}{c} C_1 \\C_2 \end{array} \right] \exp(i\omega t) \space\space ... (2)
# \end{equation}
# 
# There are a few points to note. 
# 
# We are no longer imagining the individual masses as moving with simple harmonic motion but we asscociate the oscillatory motion with a vector $\vec x = \vec x_0 \exp(i\omega t) = (C_1\hat x_1+C_2 \hat x_2)\exp(i\omega t)$ where $\hat x_1$ and $\hat x_2$ are unit vectors in our vector space. The idea of the vector space can be a difficult concept to understand especially when you realise that for $N$ masses we have an $N$ dimensional vector space (and $N$ may be considerably larger than 3!).
# 
# We will also see that we are not looking for a single frequency but $N$ different frequencies (although they may be degenerate, i.e. two independent solutions have the same frequency.)
# 
# Hence, using the trial solution (2) and subsituting into (1) we find
# 
# \begin{equation}
# \omega^2 \left [ \begin{array}{c} C_1 \\ C_2 \end{array} \right ]=-\frac{k}{m}
# \left [ \begin{array}{cc} 3 & -2 \\ -2 & 3 \end{array} \right ]
# \left [ \begin{array}{c} C_1 \\ C_2 \end{array} \right ] \space\space ... (3)
# \end{equation}.
# 
# As we know $k$ and $m$ we need to solve this equation to find the values of $\omega$ and $\left [ \begin{array}{c} C_1 \\ C_2 \end{array} \right ]$. 
# 
# At this point we may also note that if we multiply both sides of this equation by an arbitary constant, we will not find unique values for $C_1$ or $C_2$ although the ratio between them must always be the same. Ultimately the value of these constants is determined when we substitute the initial conditions into our general solution. We can re-arrange (3) and introduce the unit matrix to show,
# 
# \begin{equation}
# \left (-\frac{k}{m}
# \left [ \begin{array}{cc} 3 & -2 \\ -2 & 3 \end{array} \right ]
# -\omega^2 \left[ \begin{array}{cc} 1 & 0 \\ 0 & 1 \end{array} \right]\right ) 
# \left [ \begin{array}{c} C_1 \\ C_2 \end{array} \right ] = 0\space\space ... (4)
# \end{equation}.
# 
# that we see is in the form 
# 
# \begin{equation}
# \left (A-\lambda I\right) \vec v=0
# \end{equation}
# 
# for which, you have seen from lectures, the solutions $\lambda$ and $\vec v$ are the eigenvalues and eigenvectors of this equation.
# 
# 
# 
# 

# ## Step 3  - Finding the Eigenvalues and Eigenvectors.
# 
# We may find, either the Eigenvalues in terms of $k$ and $m$ (or sometimes we might write $\sqrt \frac{k}{m} =\omega_0^2$) or we can enter their values. You should make sure that you can do this yourself for $2 \times 2$ matrices (where you will need to solve a quadratic equation to find the eigenvalues. It is also possible to find analytic (closed form) solutions for $3 \times 3$ and $4 \times 4$ problems but the solutions are difficult to remember and apply, so in this course you will only be asked to solve $2 \times 2$ problems or $3 \times 3$ problems 'by hand' where it is straightforward to determine the roots of the cubic equation you obtain. In general you cannot find analytic solutions for $N \ge 5$ although solutions do exist for special cases. 
# 
# In this sheet we will use Python and the Linear Algebra package available with it, to determine the eigenvalues and eigenvectors for this problem. You will then see how easy, in python, it is to extend the analysis for examples with $N$ considerably greater than 4.  For convenience I will set $\sqrt\frac{k}{m} = 1$ but you should be able to modify the python code to take into account different values of $k$ and $m$ if you wish
# 
# Hence, we now wish to find the eigenvalues and eigenvectors of the matrix,
# 
# \begin{equation}
# \left[ \begin{array}{cc} 3 & -2 \\ -2 & 3 \end{array} \right] 
# \end{equation}
# 
# Here is the code we need to do the calculation. By now you are familiar with how to set up (or read from file) numpy arrays in python. In this problem we could use the eigenvector/eigenvalue functions in numpy to do the calculation. However, these are more limited so I have used the functions from the scipy library that are more comprehensive (they can deal with generalised eigenvector problems). 

# In[1]:


### The first part imports the linear algebra library so it recognises the function needed to calculate the eigenvalues and vectors
import numpy as NP
from scipy import linalg as LA
###
### Now we'll enter the array (you could read this from a file if you wish)
###
A = NP.array([[3,-2],[-2,3]])
print (A)
e_vals,e_vecs = LA.eig(A)
print ("Eigenvalues")
print(e_vals)
print ("Eigenvectors")
print(e_vecs)


# As you have seen, the python language is not the easiest language to use when creating and manipluating matrices but hopefully you can see how this works. Also note that the eigenvalues are returned as complex numbers with the imaginary part as zero as we expect.
# 
# From the result we see from this case  we have two eigenvalues. $\omega^2 =5$ and $\omega^2 =1$. You may wish to increase or decrease the strength of the spring in the middle to see the effect on the eigenvalues. 
# 
# The eigenvectors are returned as a matrix of normalised column vectors so the first eigenvector is $\left [\begin{array}{c} \frac{1}{\sqrt{2}} \\-\frac{1}{\sqrt{2}} \end{array}\right ]$ and the second eigenvector is $\left [\begin{array}{c} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{array}\right ]$. 
# 
# Hence, we'd expect our general solution to be a linear cominbation of these two modes i.e.
# 
# \begin{equation}
# \left[ \begin{array}{c} \ddot x_1 \\ \ddot x_2 \end{array}\right]=
# A\left [\begin{array}{c} \frac{1}{\sqrt{2}} \\-\frac{1}{\sqrt{2}} \end{array}\right ]\exp(i(5t))+
# B\left [\begin{array}{c} \frac{1}{\sqrt{2}} \\\frac{1}{\sqrt{2}} \end{array}\right ]\exp(i(1t))
# \end{equation}
# 
# where $A$ and $B$ are constants to be determined from the initial conditions.
# 

# ## Exercise
# 
# The python code from the example above is copied below. Go back to Step 1 above and find the matrix when you enter different values of $k_1$, $k_2$ and $k_3$. Use the code to calculate the eigenvalues and eigenvectors and try to understand how the nature of the coupled oscillations has changed. Look in particular when $k_1 \neq k_2 \neq k_3$ for example, $k_1 = 1, k_2=2, k_3 =3$. Try to interpret physically what is going on. 

# In[2]:


### The first part imports the linear algebra library so it recognises the function needed to calculate the eigenvalues and vectors
import numpy as NP
from scipy import linalg as LA
###
### Enter values into the array below for the equations of motion you have determined.
###
A = NP.array([[3,-2],[-2,5]])
print (A)
e_vals,e_vecs = LA.eig(A)
print ("Eigenvalues")
print(e_vals)
print ("Eigenvectors")
print(e_vecs)


# ## Beyond 2 x 2 problems
# 
# Beyond $2 \times 2$ matrices it becomes timeconsuming and tedious to calculate eigenvalues and eigenvectors. However, the techniques for calculating them using computers are well established using 'Linear Algebra' packages such as those available in numpy and scipy. The code above using python is one example but you can also find libraries for e.g. fortran, C/C++, for computational software packages such as Matlab, Scilab and symbolic algebra packages such as Maple, Mathematica (Wolfram Alpha) and macsyma. Here we give an example of a more complex problem using python.
# 
# A note of caution. These programmes do not always return what you expect. I have found this an issue especially, in symbolic algebra systems such as Maple or Mathematica, for the case where we have degenerate eigenvalues (two eigenvalues that have the same value) and their associated eigenvectors.
# 
# Let's extend our code to image a coupled spring system consistenting of 11 equal masses $m$ and 12 springs, all with spring constant $k$. Demonstrate that you can obtain the equation
# 
# \begin{equation}
# \left [ \begin{array}{c} \ddot x_1 \\ \ddot x_2 \\ \ddot x_3 \\ \ddot x_4 \\ \ddot x_5 \\ \ddot x_6 
# \\ \ddot x_7 \\ \ddot x_8 \\ \ddot x_9 \\ \ddot x_{10} \\ \ddot x_{11} \end{array} \right ] =\frac{k}{m} \left [ \begin{array}{ccccccccccc} 
# 2 & -1 & 0 & 0 & 0 & 0 & 0 & 0 & 0& 0 & 0\\
# -1 & 2 & -1 & 0 & 0 & 0 & 0 & 0 & 0& 0 & 0\\
# 0 & -1  & -2  & -1 & 0 & 0 & 0 & 0 & 0& 0 & 0\\
# 0 & 0 & -1 & 2 & -1 & 0 & 0 & 0 & 0& 0 & 0\\
# 0 & 0 & 0 & -1 & 2 & -1 & 0 & 0 & 0& 0 & 0\\
# 0 & 0 & 0 & 0 & -1  & 2 & -1 & 0 & 0& 0 & 0\\
# 0 & 0 & 0 & 0 & 0 & -1 & 2 & -1 & 0& 0 & 0\\
# 0 & 0 & 0 & 0 & 0 & 0 & -1 & 2 & -1& 0 & 0\\
# 0 & 0 & 0 & 0 & 0 & 0 & 0 & -1 & 2& -1 & 0\\
# 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & -1 & 2 & -1\\
# 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & -1 & 2 & -1\\
# \end{array} \right ]
# \left [ \begin{array}{c} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \\ x_6 
# \\ x_7 \\ x_8 \\  x_9 \\ x_{10} \\ x_{11} \end{array} \right ]
# \end{equation} and use the code below to find the eigenvalues and eigenvectors.
# 
# You can also find the eigenvectors for this equation analytically (you can find an example in the set problems). It is an example of a sparse matrix (contains lots of zeros). Note that the eigenvectors are returned as the columns in an $11 \times 11$ matrix. You should extract these and plot them out ($x_i$ vs $i$). You may like to use this code and decrease or increase $N$ to explore how the solutions change.  
# 
# 

# In[3]:


### The first part imports the linear algebra library so it recognises the function needed to calculate the eigenvalues and vectors
import numpy as NP
from scipy import linalg as LA
A = NP.array([
              [2,-1,0,0,0,0,0,0,0,0,0],
              [-1,2,-1,0,0,0,0,0,0,0,0],
              [0,-1,2,-1,0,0,0,0,0,0,0],
              [0,0,-1,2,-1,0,0,0,0,0,0],
              [0,0,0,-1,2,-1,0,0,0,0,0],
              [0,0,0,0,-1,2,-1,0,0,0,0],
              [0,0,0,0,0,-1,2,-1,0,0,0],
              [0,0,0,0,0,0,-1,2,-1,0,0],
              [0,0,0,0,0,0,0,-1,2,-1,0],
              [0,0,0,0,0,0,0,0,-1,2,-1],
              [0,0,0,0,0,0,0,0,0,-1,2],
             ])
print (A)
e_vals,e_vecs = LA.eig(A)
print ("Eigenvalues")
print(e_vals)
print ("Eigenvectors")
print(e_vecs)


# ##  What happens when we remove the walls?
# 
# In the previous examples the masses were attached to fixed walls by springs (Dirichlet boundary conditions). Modify the code above (reproduced below) to consider the case when the masses at the ends are not connected to a wall but are allowed to float freely. To do this you need to redetermine the equations of motion for the two masses at the end of the chain and modify the first and last rows of the matrix accordingly. Again plot out the eigenvectors. One of the eigenvectors is distinct from the others. Can you explain why it has this form?

# In[4]:


### The first part imports the linear algebra library so it recognises the function needed to calculate the eigenvalues and vectors
import numpy as NP
from scipy import linalg as LA
A = NP.array([
              [2,-1,0,0,0,0,0,0,0,0,0],
              [-1,2,-1,0,0,0,0,0,0,0,0],
              [0,-1,2,-1,0,0,0,0,0,0,0],
              [0,0,-1,2,-1,0,0,0,0,0,0],
              [0,0,0,-1,2,-1,0,0,0,0,0],
              [0,0,0,0,-1,2,-1,0,0,0,0],
              [0,0,0,0,0,-1,2,-1,0,0,0],
              [0,0,0,0,0,0,-1,2,-1,0,0],
              [0,0,0,0,0,0,0,-1,2,-1,0],
              [0,0,0,0,0,0,0,0,-1,2,-1],
              [0,0,0,0,0,0,0,0,0,-1,2],
             ])
print (A)
e_vals,e_vecs = LA.eig(A)
print ("Eigenvalues")
print(e_vals)
print ("Eigenvectors")
print(e_vecs)


# ## Conclusion for this notebook
# 
# In this notebook we have explored the two mass coupled oscillator system covered in lectures and extended the solution to cases where the spring constants are unequal. The case where the masses are different is covered in a different notebook. We have shown how we can treat this as an eigenvalue/eigenvector problem and shown how the soluitions can be calculated using python. We have extended the analysis to chains with $N>>2$ and shown how the solutions may still be calculated with simple function calls in python. 
