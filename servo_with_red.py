from dronekit import connect,VehicleMode,mavutil
import cv2
import time
connection_string="/dev/serial/by-id/usb-Hex_ProfiCNC_CubeOrange_3E0040001151303437363830-if00"
iha=connect(connection_string,wait_ready=True,timeout=100,baud=115200)

def set_servo(vehicle,servo_number,pwm_value):
    pwm_value_int=int(pwm_value)
    msg=vehicle.message_factory.command_long_encode(
        0,0,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,
        servo_number,
        pwm_value_int,
        0,0,0,0,0
        )
    vehicle.send_mavlink(msg)
iha.mode=VehicleMode("MANUAL")
'''for i in [500,700,1250,1500]:
    time.sleep(1)
    set_servo(iha,13,i)'''
print(iha.location.global_relative_frame.lat)

