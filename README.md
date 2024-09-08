

**1.Single Pendulum:**

We first start with a signle pendulum where i wrote two differential equations: one for a signle pendulum without friction ( pendulum_wo_friction()) and the other one with friction (pendulum_w_friction()).
We are using scipy.integrate.odeint to solve the differential equations in this repository so don't forget to pip install scipy and also matplotlib to see the plots.
The first plot is our parameters with respect to time.We can verify here that when the angle is at its extremum, the angle velocity is null.
![paramaters with respect to time](https://github.com/user-attachments/assets/a4e069bb-ffc7-40e8-b5f0-299b77b3b7c0)


For the initial conditions, you can change the vector u0 where the first component is the initial angle the second is the intial angular velocity.
These initial conditions play an important role in the nature of the trajectory of the pendulum .We can see this change in the Phase portrait.
We have three different types of trajectory:

**a.Harmonic oscillator:** 

this is when the intial angle is small enough to linearise the differential equation.


![paramaters with respect to time](https://github.com/user-attachments/assets/9ffbc440-d269-4567-9784-89eac6487702)  
     
    
  The Phase portrait is an ellipse in this case.

![harmonic oscillator](https://github.com/user-attachments/assets/f2b4a319-e941-4f55-9733-10fe95fb4d8b)

**b.Anharmonic oscillator:**

this is when the initial angle is not small enough to linearise the ode but also not big enough for the pendulum to reach the next type of trajectory ( with the help of the initial angular velocity).
![anharmonic trajectory](https://github.com/user-attachments/assets/4968d834-4786-40fa-8f4a-68f18f11ae78)                                                                                       

 
 
 The Phase portrait is a deformed ellipse.

 
![anharmonic oscillator](https://github.com/user-attachments/assets/651ee474-e95a-4406-971d-1824658096c0)

**c.Free trajectory:**

this is when the initial parameters are big enough for the pendulum to be doing full circles nonstop.


![free trajectory](https://github.com/user-attachments/assets/5546586e-f1b1-4899-b00b-a395a22ab6ef)                                             ![free phase portrait](https://github.com/user-attachments/assets/dacd7948-d8dd-477c-ade3-a52da548f048)



You can also change the constants ( g:gravity potential,l:length of the cord,alpha:viscosity constant) but this will only change the period of the oscillation.


In the end, we animate the pendulum's oscillation.

![pendulum](https://github.com/user-attachments/assets/6644f3b5-a9bb-4809-b88d-28e0de119713)

**2.Double Pendulum :**


To establish the equation of motion for the double pendulum, I chose to write the lagrangian of the system and use the Euler_Lagrange equation for the two angles ( theta1 and theta2).

We use odeint just like with the single pendulum except here the initial vector u0 has 4 coordinates (angle and angular velcoity for each pendulum).
Changing the initial conditions change greatly the trajectory of the pendulums which show the chaotic nature of the system.




![double_pendulum](https://github.com/user-attachments/assets/d6cac13b-45e8-4534-bc42-1816770882e9)



**P.S**  Don't forget to import the libraries matplotlib, numpy and scipy.integrate








