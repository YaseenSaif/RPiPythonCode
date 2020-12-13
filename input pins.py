import pymysql.connections
import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(9,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(0,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    db = pymysql.connections.Connection(
        host="localhost",
        user="pi",
        passwd="pi",
        database="concrete_factory"
    )
    print("connect successful!!")
    with db.cursor() as cursor:
        sql = "select pn_Status from operation_mode order by pn_No"
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        PIN_STAT_0=GPIO.input(0)
        PIN_STAT_4=GPIO.input(4)
        PIN_STAT_5=GPIO.input(5)
        PIN_STAT_9=GPIO.input(9)
        PIN_STAT_10=GPIO.input(10)
        PIN_STAT_11=GPIO.input(11)
        PIN_STAT_13=GPIO.input(13)
        PIN_STAT_17=GPIO.input(17)
        PIN_STAT_22=GPIO.input(22)
        PIN_STAT_19=GPIO.input(19)
        time.sleep(0.100)
        
        if result[0][0] != PIN_STAT_0: 
            sql = "update operation_mode set pn_Status=%s  where pn_No=0 "
            cursor.execute(sql,PIN_STAT_0)
            db.commit()
            time.sleep(0.100)
         
        if result[1][0] != PIN_STAT_4:  
            sql = "update operation_mode set pn_Status=%s  where pn_No=4"
            cursor.execute(sql,PIN_STAT_4)
            db.commit()
            time.sleep(0.100)
         
        if result[2][0] != PIN_STAT_5: 
            sql = "update operation_mode set pn_Status=%s  where pn_No=5 "
            cursor.execute(sql,PIN_STAT_5)
            db.commit()
            time.sleep(0.100)
            sql = "UPDATE operation_mode SET pn_Status = 0 WHERE pn_No = %s"
            cursor.executemany(sql,["14","15","18"])
            db.commit()
        if result[3][0] != PIN_STAT_9:
            sql = "update operation_mode set pn_Status=%s  where pn_No=9 "
            cursor.execute(sql,PIN_STAT_9)
            db.commit()
            time.sleep(0.100)
          
        if result[4][0] != PIN_STAT_10:  
            sql = "update operation_mode set pn_Status=%s  where pn_No=10 "
            cursor.execute(sql,PIN_STAT_10)
            db.commit()
            time.sleep(0.100)
         
        if result[5][0] != PIN_STAT_11:  
            sql = "update operation_mode set pn_Status=%s  where pn_No=11 "
            cursor.execute(sql,PIN_STAT_11)
            db.commit()
            time.sleep(0.100)
        
        if result[6][0] != PIN_STAT_13: 
            sql = "update operation_mode set pn_Status=%s  where pn_No=13 "
            cursor.execute(sql,PIN_STAT_13)
            db.commit()
            time.sleep(0.100)
         
        if result[9][0] != PIN_STAT_17: 
            sql = "update operation_mode set pn_Status=%s  where pn_No=17 "
            cursor.execute(sql,PIN_STAT_17)
            db.commit()
            time.sleep(0.100)
         
        if result[12][0] != PIN_STAT_22: 
            sql = "update operation_mode set pn_Status=%s  where pn_No=22 "
            cursor.execute(sql,PIN_STAT_22)
            db.commit()
            time.sleep(0.100)
        
        if result[11][0] != PIN_STAT_19:  
            sql = "update operation_mode set pn_Status=%s  where pn_No=19 "
            cursor.execute(sql,PIN_STAT_19)
            db.commit()
            time.sleep(0.100)