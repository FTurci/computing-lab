#!/usr/bin/env python
# coding: utf-8

# # Normal modes, coordinates, eigenvalues and eigenvectors
# 
# In the previous sheets we have seen how we can apply the mathematical technqiue of finding eigenvalues and eigenvectors to solve coupled oscilator problems. A key point to remember is we needed to find the eigenvalues and eigenvectors of a real and symmetric matrix. This was easy in the 'equal mass' case but needed a little more care for the 'unequal mass' case. 
# 
# The normal frequencies of the oscillators are determined from the eigenvalues. The relative motion of the the masses in the system were found from the eigenvectors and these are what we needed to find the motion of the individual masses.
# 
# In the lectures we introduced the idea of normal (or generalised coordinates). In this notebook we will elaborate on what we mean by normal coordinates and why they may be useful.
# 
# 

# ## The eigenvector matrix
# 
# There is a general result from Linear Algebra that says,
# 
# "For any matrix $\bf{A}$ that has well defined eigenvalues and eigenvectors we can form a matrix $\bf{P}$ from the eigenvectors as columns."
# 
# If you inspect the python code in the previous examples you can see that this is indeed the way in which the eigenvectors are returned from the python "LA.eig(A)" library call. A further result from Linear Algebra is,
# 
# \begin{equation}
# \bf{P}^{-1}\bf{A}\bf{P}= \bf{D}
# \end{equation}
# 
# The example of the two mass system was demonstrated in lectures so let's look at the more complicated example of the Carbon Dioxide molecule covered in previous sheet. We had
# \begin{equation}
# \omega^2 \left [ \begin{array}{c} C_{O1}' \\ C_C' \\ C_{O2}' \end{array} \right ]=
# k \left [ \begin{array}{ccc} \frac{1}{m_{O1}} & -\frac{1}{\sqrt{m_{O1}m_C}} & 0 \\
#                             -\frac{1}{\sqrt{m_{O1}m_C}} & \frac{2}{m_C} & -\frac{1}{\sqrt{m_C m_{O2}}} \\
#                              0 & -\frac{1}{\sqrt{m_C m_{O2}}} & \frac{1}{m_{O2}}  \end{array} \right ]
# \left [ \begin{array}{c} C_{O1}' \\ C_C' \\ C_{O2}' \end{array} \right ]
# \end{equation}
# 
# 
# an we took $k=1$ and let $m_C=12$ and $m_{O1} = m_{O2} = 16$. The eigenvalues and vectors for these values were generated using the python code below.
# 

# In[1]:


### The first part imports the linear algebra library so it recognises the function needed to calculate the eigenvalues and vectors
import numpy as NP
from scipy import linalg as LA
m_O1=16
m_C=12
m_O2=16
A = NP.array([[1/m_O1,-1/NP.sqrt(m_O1*m_C),0],
              [-1/NP.sqrt(m_O1*m_C),2/m_C,-1/NP.sqrt(m_O2*m_C)],
              [0, -1/NP.sqrt(m_O2*m_C), 1/m_O2]
             ])
print (A)
e_vals,e_vecs = LA.eig(A)
print ("Eigenvalues")
print(e_vals)
print ("Eigenvectors")
print(e_vecs)


# We will now modify the python code above to find the diagonal matrix. See if you can follow the code.

# In[2]:


### The first part imports the linear algebra library so it recognises the function needed to calculate the eigenvalues and vectors
import numpy as NP
from scipy import linalg as LA
m_O1=16
m_C=12
m_O2=16
A = NP.array([[1/m_O1,-1/NP.sqrt(m_O1*m_C),0],
              [-1/NP.sqrt(m_O1*m_C),2/m_C,-1/NP.sqrt(m_O2*m_C)],
              [0, -1/NP.sqrt(m_O2*m_C), 1/m_O2]
             ])
print ("A = ",A)
e_vals,P = LA.eig(A)
invP = LA.inv(P)
print (" ")
print ("eigenvalues are ", e_vals)
print(" ")
print("P    =", P)
print(" ")
print ("P^-1 = ",invP)
print (" ")
D=NP.matmul(invP,NP.matmul(A,P))
print ("D  =  ",D)
       


# You should see that the $\bf{D}$ matrix is diagonal (within the numerical errors) and the diagonal elements of $\bf{D}$ are the eigenvalues of the matrix $\bf{A}$ that were calculated in the 'LA.eig' function. In the case of our real and symmetric matrices a result from linear algebra says $\bf{A}$ and $\bf{D}$ are $\textit{similar}$ matrices such that, 
# 
# \begin{equation}
# \textbf{A}\vec{x}-\lambda \vec{x}  = 0 \space\space\space\space ....(1)     
# \end{equation}
# and
# \begin{equation}
# \textbf{D}\vec{q}-\lambda \vec{q} = 0 \space\space\space\space ....(2)
# \end{equation} 
# 
# and that they share the common eigenvalues $\lambda_i$. As $\textbf{D}$ is diagonal we write,
# 
# \begin{equation}
# \left [ \begin{array}{cccc} D_1 & 0 & 0 & ... \\
#                     0 & D_2 & 0 & ... \\
#                     0 & 0 & D_3 & ... \\
#                     ... & ... & ... & ... \end{array} \right ]
#                     \left [ \begin{array}{c} q_1 \\ q_2 \\ q_3 \\ ... \end{array} \right ] =
# \left [ \begin{array}{cccc} \lambda_1 & 0 & 0 & ... \\
#                     0 & \lambda_2 & 0 & ... \\
#                     0 & 0 & \lambda_3 & ... \\
#                     ... & ... & ... & ... \end{array} \right ]
#                     \left [ \begin{array}{c} q_1 \\ q_2 \\ q_3 \\ ... \end{array} \right ]                   
# \end{equation}
# 
# that gives uncoupled equations $D_i q_i = \lambda_i q_i$. Each of these equations corresponds to a normal mode of the system and we note that they act as independent oscillators in $\vec{q}$ space. In otherwords if the system is oscillating in the coordinate $q_i$ then no energy will be transfered to the other modes (as the equations are uncoupled). Another way of saying this is we have transformed the problem from being defined in a vector space $\vec{x}$ to a vector space $\vec{q}$. You may ask why this might be interesting. It is possible to consider both the kinetic and potential energy in the $\vec{q}$ coordinates, for example the kinetic energy of each mode may be written as $\frac{1}{2}M_i q_i^2$ where $M_i$ corresponds to a 'mass' in $\vec{q}$-space. It is easy to see how the energy might be partitioned in a system when we use these coordinates. Expressing the kinetic and potential energy in normal coordinates is particular useful if we wish to formulate a problem using the Lagrangian approach to mechanics. Unfortunately, we cannot cover Lagrangian mechanics and generalised (normal) coordinates here but the method will appear in more advanced courses.
# 
# Given the utility of the normal coordinates we now wish to see how we can transform between the two vector spaces. We will do some simple matrix manipulation. From (2) we have
# 
# \begin{equation}
# \textbf{D}\vec{q}=\lambda \vec{q}\\
# \textbf{P}^{-1}\textbf{A}\textbf{P}\vec{q}=\lambda \vec{q}
# \end{equation}
# 
# Multiplying the LHS and RHS by $\textbf{P}$ we find
# 
# \begin{equation}
# \textbf{A}\textbf{P}\vec{q}=\textbf{P}\lambda \vec{q}
# \end{equation}
# 
# or re-arranging
# 
# \begin{equation}
# \textbf{A} ( \textbf{P} \vec{q} ) = \lambda ( \textbf{P} \vec{q})
# \end{equation}
# 
# If we compare this to equation (1) we find the result
# 
# \begin{equation}
# \vec{x}=\textbf{P} \vec{q}   \space\space\space\space ... (3)
# \end{equation}
# 
# or
# 
# \begin{equation}
# \textbf{P}^{-1}.\vec{x}=\vec{q}   \space\space\space\space ... (4)
# \end{equation} 
# 
# that is the result we quoted in lectures. It is important to remember here that we have sued some standard results from Linear Algebra theory that is valid for the real and symmetric matrices we have been using but are not generally true for all matrices.
# 
# Let's take a look at the results for our Carbon Dioxide molecule calculated above. For the masses in the example we find the result 
# \begin{equation}
# \textbf{P}   = \left [ \begin{array}{ccc} -0.369 & -0.707 & 0.603 \\
#   0.853 & 0 &   0.522 \\
#  -0.369 &  0.707 &  0.603 \end{array} \right]
# \end{equation}
# and 
# \begin{equation}
# \textbf{P}^{-1} = \left [ \begin{array}{ccc}
# -0.369  & 0.853 & -0.369 \\
#  -0.707 &  0 &  0.707 \\
#   0.603 &  0.522 &  0.603
#  \end{array} \right]
# \end{equation}
# 
# As you can see from this example $\textbf{P}^{-1}$ is just the transpose of $\textbf{P}$, $\textbf{P}^T$ so the relationship between the eigenvectors and the normal coordinates is straight forward to determine.

# In[ ]:




