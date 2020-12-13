import pymysql.connections
import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(15,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(18,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(23,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(24,GPIO.OUT,initial=GPIO.HIGH)

PIN_STAT_14=1
PIN_STAT_15=1
PIN_STAT_18=1
PIN_STAT_23=1
PIN_STAT_24=1
while True:
    db2 = pymysql.connections.Connection(
        host="localhost",
        user="pi",
        passwd="pi",
        database="concrete_factory"
    )
    print("connect successful!!")
    with db2.cursor() as cursor:
        sql = "select pn_Status from operation_mode order by pn_No"
        cursor.execute(sql)
        db2.commit()
        result = cursor.fetchall()
      
        if (not result[7][0]) != PIN_STAT_14:  
            PIN_STAT_14=not result[7][0]
            GPIO.output(14,PIN_STAT_14)
        if (not result[8][0]) != PIN_STAT_15:  
            PIN_STAT_15=not result[8][0]
            GPIO.output(15,PIN_STAT_15)
        if (not result[10][0]) != PIN_STAT_18: 
            PIN_STAT_18=not result[10][0]
            GPIO.output(18,PIN_STAT_18)
        if (not result[13][0]) != PIN_STAT_23:
            PIN_STAT_23=not result[13][0]
            GPIO.output(23,PIN_STAT_23)
        if ( result[14][0]) == GPIO.HIGH:  
            GPIO.output(24,GPIO.LOW)
            time.sleep(5)
            sql = "UPDATE operation_mode SET pn_Status = 0 WHERE pn_No = 24"
            cursor.execute(sql)
            db2.commit()
            GPIO.output(24,GPIO.HIGH)
