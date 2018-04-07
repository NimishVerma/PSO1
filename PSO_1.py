# ---------------------------------------------------------------------------------------------
# 																							
# 							CODE BY :																	
#									Nimish Verma
# 										(github.com/bigpythonimish)
# 							Made from implementing Swarm particle optimisation on a very basic level
# 
# 
# 
# 
# #############################################################################################

# Position of Particle in next iteration = Current position + Velocity for all three coordinates
# w = intertia weight val
# c1,c2 cognitive and social param
# r1,r2 random {0,1}
# velocity= w*velocity +c1*r1*(best individual posi -  current posi) + c2*r2*(global best posi - current posi)
# -----------------------|__________________________________________|---|______________________________________|
# -----------------------------COGNITIVE(PERSONAL EXP) TERM---------------------------------SOCIAL TERM---------


import random
import math
#function to optimize
def sphere_func(x):
	sum=0
	for i in range(len(x)):
		sum+=x[i]**2
	return sum

#particle class, argument: posi array
class Particle:
	def __init__(self,posarr):
		self.position_i=[]          # position
		self.velocity_i=[]          # velocity
		self.err_i=-1               # current individual error
		self.pos_best_i=[]          # best individual posi
		self.err_best_i=-1          # best individual error
       
		for i in range(0,num_dimensions):
			self.velocity_i.append(random.uniform(-1,1)) #assign random values from a uniform distribution
			self.position_i.append(posarr[i]) #takes the input array and assigns value of posi

	def findError(self,costFunc):
		self.err_i = costFunc(self.position_i) #find current error
		#if this error is less than the local error of individual we replace it
		if self.err_i < self.err_best_i or self.err_best_i==-1:
			self.pos_best_i=self.position_i
			self.err_best_i=self.err_i

	def update_params(self,global_best,bounds): #update position acc to bounds and velocity acc to weights and intertia
		w = 1 #constant intertia 
		c1 = 3 # individual cognition
		c2 = 5 #social constant slightly higher for exploration
		for i in range(0,num_dimensions):
			#UPDATE VELOCITIES FIRST
			r1=random.random()
			r2=random.random()

			cognitive_term=c1*r1*(self.pos_best_i[i]-self.position_i[i])
			social_term=c2*r2*(global_best[i]-self.position_i[i])
			self.velocity_i[i]=w*self.velocity_i[i]+cognitive_term+social_term

			#UPDATE POSITIONS NEXT
			self.position_i[i]=self.position_i[i]+self.velocity_i[i]

			# adjust maximum position if necessary
			if self.position_i[i]>bounds[i][1]:
				self.position_i[i]=bounds[i][1]

			# adjust minimum position if neseccary
			if self.position_i[i] < bounds[i][0]:
				self.position_i[i]=bounds[i][0]

class PSO():
	def __init__(self,costFunc,posiarr,bounds,num_particles,epochs):
		global num_dimensions

		num_dimensions=len(posiarr)
		global_err=-1                   # best error globally
		global_best=[]                   # best posi globally

        # establish the swarm (array of particles objects)
		swarm=[]
		for i in range(0,num_particles):
			swarm.append(Particle(posiarr))
		print (swarm)

        # begin optimization 
		i=0
		while i < epochs:
           
            
			for j in range(0,num_particles):
				swarm[j].findError(costFunc)#find cost of each particles

				# if the current particle has global min
				if swarm[j].err_i < global_err or global_err == -1:
					global_best=list(swarm[j].position_i)
					global_err=float(swarm[j].err_i)
			#  update parameters of particles
			for j in range(0,num_particles):
				swarm[j].update_params(global_best, bounds)
				i+=1
		print  ('RESULT:')
		print  (global_best)
		print (global_err)

if __name__ == "__PSO__":
    main()


initial=[5,5]               # initial starting posi
bounds=[(-10,10),(-10,10)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
PSO(sphere_func,initial,bounds,num_particles=15,epochs=40)



