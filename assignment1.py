initial_vel = 0
time_spent =  input ('Input time: ')
acceleration = input ('Input acceleration: ')
distance = input ('Input distance: ')
max_speed = 60
i = 0 

p_speed = int(acceleration)*int(time_spent)
p_distance = int(time_spent)*(p_speed)/2

if p_speed > max_speed:
    print ('The person went over the speed limit.' + '(Max speed was',p_speed,'m/s)')
else:
    print ('The person did not go over the speed limit.' +'(Max speed was',p_speed,'m/s)')

if p_distance > int(distance):
    print ('The person reached the destination.' + '(Reached',p_distance,'m)')
else:
    print ('The person did not reach the destination.' + '(Reached',p_distance,'m)')

##for i in range (0,int(time_spent)):
#    i = 'Duration'
#    number = 
#    print (i+':',time_spent, 'Distance: ','*'*int(p_distance/10))
    
while i < int(time_spent) + 1:
    print('Duration: ',i, 'Distance: ','*'*int(p_distance1))
    i = i + 1
    
