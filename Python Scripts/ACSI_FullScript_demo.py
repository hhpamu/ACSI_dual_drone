import time
# import sklearn
import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm
from cflib.positioning.motion_commander import MotionCommander
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncLogger import SyncLogger
import os
# from sklearn.metrics import mean_absolute_error
# from sklearn.metrics import mean_absolute_percentage_error
import numpy as np
import matplotlib.pyplot as plt
from numpy import savetxt


def param_stab_est_callback(name, value):
    print('The crazyflie has parameter ' + name + ' set at number: ' + value)

# def simple_param_async(scf, groupstr, namestr):
#     cf = scf.cf
#     full_name = groupstr + '.' + namestr

#     cf.param.add_update_callback(group=groupstr, name=namestr,
#                                  cb=param_stab_est_callback)
#     time.sleep(1)

setpointLy = []
actualLy = []

setpointLx = []
actualLx = []


setpointRy = []
actualRy = []

setpointRx = []
actualRx = []

#For yaw:
# setpointL = []
# actualL = []

# setpointR = []
# actualR = []


pwm_list_L = []
pwm_list_R = []
def log_pwm_callback(uri, timestamp,data, logconf):
    if (uri=="radio://0/80/2M/E7E7E7E7E1"):
        avg = data['motor.m1'] + data['motor.m2'] + data['motor.m3'] + data['motor.m4']
        pwm_list_L.append(avg/4)
    else:
        avg = data['motor.m1'] + data['motor.m2'] + data['motor.m3'] + data['motor.m4']
        pwm_list_R.append(avg/4)

def log_vel_callback(uri, timestamp, data, logconf):

    actualx = float(data['kalman.statePX'])
    setpointx = float(data['ctrltarget.vx'])
    
    
    actualy = float(data['kalman.statePY'])
    setpointy = float(data['ctrltarget.vy'])
    
    
    # actual = float(data['stateEstimateZ.rateYaw'])
    # setpoint = float(data['ctrltarget.yaw'])
    
    if (uri=="radio://0/80/2M/E7E7E7E7E1"):
        
        # For yaw
        # actualL.append(actual)
        # setpointL.append(setpoint)
        
        # For other dirs
        actualLx.append(actualx)
        setpointLx.append(setpointx)
        actualLy.append(actualy)
        setpointLy.append(setpointy)
        
    else:
        
    #     # For yaw
    #     # actualR.append(actual)
    #     # setpointR.append(setpoint)
        
        actualRx.append(actualx)
        setpointRx.append(setpointx)
        actualRy.append(actualy)
        setpointRy.append(setpointy)

roll_Kp = 0
roll_Kd = 0
roll_Ki = 0
 
def update_params_callback(uri, name,value):
    print(name + "for " + uri + " set at: " + value)
    # print(name + " for " + str(uri) +" set at: " + value)


    
#define PID_ROLL_RATE_KP  250.0
#define PID_ROLL_RATE_KI  500.0
#define PID_ROLL_RATE_KD  2.5
#define PID_ROLL_RATE_KFF 0.0
#define PID_ROLL_RATE_INTEGRATION_LIMIT    33.3

#define PID_PITCH_RATE_KP  250.0
#define PID_PITCH_RATE_KI  500.0
#define PID_PITCH_RATE_KD  2.5
#define PID_PITCH_RATE_KFF 0.0
#define PID_PITCH_RATE_INTEGRATION_LIMIT   33.3

#define PID_YAW_RATE_KP  120.0
#define PID_YAW_RATE_KI  16.7
#define PID_YAW_RATE_KD  0.0
#define PID_YAW_RATE_KFF 0.0
#define PID_YAW_RATE_INTEGRATION_LIMIT     166.7
def set_params_async(scf, group):
    
    # roll_ratio = 3.75
    # pitch_ratio = 1.5
    cf = scf.cf
    
    cf.param.add_update_callback("pid_rate", "yaw_kp", lambda n, v: update_params_callback(cf.link_uri, n, v))
    cf.param.add_update_callback("pid_rate", "roll_kp", lambda n, v: update_params_callback(cf.link_uri, n, v))
    cf.param.add_update_callback("pid_rate", "pitch_kp", lambda n, v: update_params_callback(cf.link_uri, n, v))
    cf.param.add_update_callback("pid_rate", "roll_kd", lambda n, v: update_params_callback(cf.link_uri, n, v))
    cf.param.add_update_callback("pid_rate", "pitch_kd", lambda n, v: update_params_callback(cf.link_uri, n, v))
    
    time.sleep(1)
    #Actual Tuned Values
    # cf.param.set_value("pid_rate.yaw_kp", 150)
    # time.sleep(1)
    # cf.param.set_value("pid_rate.roll_kp", 1000) #250
    # time.sleep(1)
    # cf.param.set_value("pid_rate.roll_kd", 10) # 2.5
    # time.sleep(1)
    # cf.param.set_value("pid_rate.pitch_kp", 400)  
    # time.sleep(1)
    # cf.param.set_value("pid_rate.pitch_kd", 4)
    # time.sleep(1)
    
    
    cf.param.set_value("pid_rate.roll_kp", 600) # 250
    time.sleep(0.2)
    cf.param.set_value("pid_rate.roll_kd", 6) # 2.5
    # time.sleep(0.2)
    # cf.param.set_value("pid_rate.pitch_kp", 250+(pwm_ratio*2300)) # 250
    # time.sleep(0.2)
    # cf.param.set_value("pid_rate.pitch_kd", 2.5+(pwm_ratio*23)) # 2.5
    time.sleep(0.2)
    
def set_params_async_load(scf, group, pwm_ratio):

    cf = scf.cf
    
    cf.param.add_update_callback("pid_rate", "roll_kp", lambda n, v: update_params_callback(cf.link_uri, n, v))
    cf.param.add_update_callback("pid_rate", "roll_kd", lambda n, v: update_params_callback(cf.link_uri, n, v))
    time.sleep(0.2)
    cf.param.set_value("pid_rate.roll_kp", 600 +(pwm_ratio*3500)) # 250
    time.sleep(0.2)
    cf.param.set_value("pid_rate.roll_kd", 6+(pwm_ratio*35)) # 2.5
    # time.sleep(0.2)
    # cf.param.set_value("pid_rate.pitch_kp", 250+(pwm_ratio*2300)) # 250
    # time.sleep(0.2)
    # cf.param.set_value("pid_rate.pitch_kd", 2.5+(pwm_ratio*23)) # 2.5
    time.sleep(0.2)


default_average = 0

def motion_command(scf):
    cflib.crtp.init_drivers()

    #Logging
    lg_stab = LogConfig(name='Velocity', period_in_ms=20)
    lg_pwm = LogConfig(name = 'pwm', period_in_ms = 20)
    
    lg_pwm.add_variable('motor.m1', 'float')
    lg_pwm.add_variable('motor.m2','float')
    lg_pwm.add_variable('motor.m3', 'float')
    lg_pwm.add_variable('motor.m4','float')
    

    
    # lg_stab.add_variable('motor.m1', 'float')
    # lg_stab.add_variable('motor.m2','float')
    # lg_stab.add_variable('motor.m3', 'float')
    # lg_stab.add_variable('motor.m4','float')
    
    
    lg_stab.add_variable('kalman.statePY', 'float')
    lg_stab.add_variable('ctrltarget.vy','float')
    lg_stab.add_variable('kalman.statePX', 'float')
    lg_stab.add_variable('ctrltarget.vx','float')
    
    
    # For yaw
    # lg_stab.add_variable('stateEstimateZ.rateYaw', 'float')
    # lg_stab.add_variable('ctrltarget.yaw','float')

    scf.cf.log.add_config(lg_pwm)
    scf.cf.log.add_config(lg_stab)
    
    lg_stab.data_received_cb.add_callback(lambda t, d, l: log_vel_callback(scf.cf.link_uri, t, d, l))
    lg_pwm.data_received_cb.add_callback(lambda t, d, l: log_pwm_callback(scf.cf.link_uri, t, d, l))
   
    mc = MotionCommander(scf,default_height = 0.3)
    group = 'pid_rate'
    
    # Set the default dual drone payload
    set_params_async(scf, group)
    mc.take_off(height = 0.3)
    time.sleep(1)
    lg_stab.start()
    mc.forward(1.5,0.3)
    time.sleep(1)
    mc.land()
    time.sleep(3)
    mc.take_off(height = 0.3)
    lg_pwm.start()
    while(len(pwm_list_L)<10):
        time.sleep(0.1)
        continue
    lg_pwm.stop()
    pwm_ratio = (sum(pwm_list_R + pwm_list_L)/(len(pwm_list_R)+len(pwm_list_L))/50000) - 1
    if(pwm_ratio > 0):
        print(pwm_ratio)
        #Adaptively Adjust PID for payload
        set_params_async_load(scf, group, pwm_ratio)
    # mc.land()
    # time.sleep(2)
    # mc.take_off(height = 0.3)
    time.sleep(1)
    mc.left(2,0.3)
    time.sleep(1)
    mc.right(2,0.3)
    time.sleep(1)
    mc.land()
    lg_stab.stop()
    


    
    
def calculate_mape(y_true, y_pred):
    sum = 0
    count = 0
    if (y_true[50] != 0):
        for i in range(len(y_true)):
            if (y_true[i]!= 0):
                sum+=np.abs((y_true[i] - y_pred[i]) / y_true[i])
                count += 1
            
        return sum*100/count
    else:
        return 0



uris = {
    'radio://0/80/2M/E7E7E7E7E1',
    'radio://0/80/2M/E7E7E7E7E7'
     # Add more URIs if you want more copters in the swarm
}


if __name__ == '__main__':
    cflib.crtp.init_drivers()
    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        print('Connected to  Crazyflies')
        swarm.reset_estimators()
        swarm.parallel_safe(motion_command)
        # swarm.parallel_adapt
        
        
        
    #Need to change this every time
    flightType = "Test 1"
    folder = "flightTracking/Final Submission Graphs/Adaptive Controller/" + flightType +"/"
    os.makedirs(folder, exist_ok=True)
    
    #for turning
    # factor = 0.0572958
    # dataL = np.column_stack((actualL, setpointL))
    # dataR = np.column_stack((actualR, setpointR))
    
    # dataL[:,0]*=factor  
    # dataR[:,0]*=factor
    
    # numRows = min(dataL.shape[0], dataR.shape[0])
    # dataAvg = np.zeros((numRows,2))
    # dataAvg[:,1] = dataL[:numRows,1]
    # dataAvg[:,0] = np.mean(np.stack((dataL[:numRows,0],dataR[:numRows,0])), axis = 0)
    
    # plt.plot(dataAvg[:,0], label = "actual data")
    # plt.plot(dataAvg[:,1], label = "setpoint")
    # plt.ylabel("Velocity (m/s)")
    # plt.xlabel("Flight of 2 Meters")
    # plt.title(flightType + " (2 Drone Average)")
    # plt.legend()
    # plt.savefig(folder + flightType + "Average.png")
    # plt.close()
    
    # mape = calculate_mape(dataAvg[25:500, 1], dataAvg[25:500, 0])
    # print("Mean Absolute Percentage Error (MAPE) yaw direction:", mape, "%")
    
    # print("left: ", sum(pwm_list_L)/len(pwm_list_L))
    # print("right: ", sum(pwm_list_R)/len(pwm_list_R))
    # for everything else
    dataL = np.column_stack((actualLx, setpointLx, actualLy, setpointLy))
    dataR = np.column_stack((actualRx, setpointRx, actualRy, setpointRy))
    # print(dataL.shape)
    # print(dataR.shape)
    numRows = min(dataL.shape[0], dataR.shape[0])
    dataAvg = np.zeros((numRows,4))
    dataAvg[:,1] = dataL[:numRows, 1]
    dataAvg[:,3] = dataL[:numRows, 3]
    dataAvg[:,0] = np.mean(np.stack((dataL[:numRows,0],dataR[:numRows,0])), axis = 0)
    dataAvg[:,2] = np.mean(np.stack((dataL[:numRows,2],dataR[:numRows,2])), axis = 0)
    
    
    plt.plot(dataAvg[:,0], label = "actual data x")
    plt.plot(dataAvg[:,1], label = "setpoint x")
    plt.plot(dataAvg[:,2], label = "actual data y")
    plt.plot(dataAvg[:,3], label = "setpoint y")
    
    plt.ylabel("Velocity (m/s)")
    plt.title("Full Demo")
    # plt.title(flightType + " (2 Drone Average)")
    plt.legend()
    plt.savefig(folder + flightType + "Average.png")
    plt.close()

    mape = calculate_mape(dataAvg[25:, 1], dataAvg[25:, 0])
    print("Mean Absolute Percentage Error (MAPE) X direction:", mape, "%")
    mape = calculate_mape(dataAvg[25:, 3], dataAvg[25:, 2])
    print("Mean Absolute Percentage Error (MAPE) Y direction:", mape, "%")

    # Calculate Absolute Error
    # abs_error = mean_absolute_error(dataAvg[:, 1], dataAvg[:, 0])
    # print("Absolute Error:", abs_error)
    # mape = mean_absolute_percentage_error(dataAvg[:, 1], dataAvg[:, 0])
    # print("Absolute Error:", mape)
    
    # plt.plot(dataL[:,0]*turnconv, label = "actual data")
    # plt.plot(dataL[:,1], label = "setpoint")
    # plt.ylabel("Velocity (m/s)")
    # plt.xlabel("Flight of 2 Meters")
    # plt.title(flightType + " (Left Done)")
    # plt.legend()
    # plt.savefig(folder + flightType + "Left.png")
    # plt.close()
    
    # plt.plot(dataR[:,0]*turnconv, label = "actual data")
    # plt.plot(dataR[:,1], label = "setpoint")
    # plt.ylabel("Velocity (m/s)")
    # plt.xlabel("Flight of 2 Meters")
    # plt.title(flightType + " (Right Drone)")
    # plt.legend()
    # plt.savefig(folder + flightType + "Right.png")
    # plt.close()
    
    savetxt(folder+flightType+'_L.csv', dataL, delimiter=',')
    savetxt(folder+flightType+'_R.csv', dataR, delimiter=',')


