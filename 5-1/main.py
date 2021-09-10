NONE = 0
SUCCESS = 10

def cheese_machine(s,a):
    global s2
    if a==0: # Press button 1
        s2 = 1-s # Toggle bulb state
        reward = NONE 
    else: # Press button 2
        if s==1: # Bulb is ON
            s2 = s # Bulb maintains current state 
            reward= SUCCESS # Cheese gained
        else:
            s2 = s # Bulb maintains current state 
            reward = NONE # No cheese because power is OFF 
    return reward

s_a_s2s = [(0,0,0),(1,0,0),(0,1,0),(1,1,0)]
for s_a_s2 in s_a_s2s:
    s = s_a_s2[0]
    a = s_a_s2[1]
    s2 = s_a_s2[2]
    reward = cheese_machine(s,a)
    print("s=",s,"s2=",s2,"a=",a,"reward=",reward)
