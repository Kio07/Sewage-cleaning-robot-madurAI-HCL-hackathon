def turn_to(brick, new_x, new_y, old_x, old_y, angle):
    delta_x = new_x - old_x
    print delta_x
    delta_y = new_y - old_y
    print delta_y

    roboCturn = base * pi
    Circumference = diameter * pi

    if(angle > 315 or angle < 45):
        #tested
        if (delta_x < 0 and delta_y == 0):
            #180 degrees tested
            angle_rad = math.radians(180)
            angle_deg = (angle_rad) * (180/pi)
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho      

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x == 0 and delta_y > 0):
            #90 degrees right tested
            angle_rad = math.radians(90)
            angle_deg = (angle_rad) * (180/pi)
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x == 0 and delta_y < 0): 
            #90 degrees left tested
            angle_rad = math.radians(90)
            angle_deg = (angle_rad) * (180/pi)
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            right.weak_turn(power=power, tacho_units=tachoUnits)
            left.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x > 0 and delta_y > 0):
            # degrees in 1st quadrant tested
            angle_rad = math.atan2(delta_y, delta_x)
            angle_deg = 90 - ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x > 0 and delta_y < 0):
            #degrees in 4th quadrant tested
            angle_rad = math.atan2((math.fabs(delta_y)), delta_x)
            angle_deg = 90 - ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            right.weak_turn(power=power, tacho_units=tachoUnits)
            left.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x < 0 and delta_y > 0):
            #degrees in 2nd quadrant tested
            angle_rad = math.atan2(delta_y, (math.fabs(delta_x)))
            angle_deg = 90 + ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x < 0 and delta_y < 0):
            #degrees in 3rd quadrant tested
            angle_rad = math.atan2((math.fabs(delta_y)), (math.fabs(delta_x)))
            angle_deg = 90 + ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            right.weak_turn(power=power, tacho_units=tachoUnits)
            left.weak_turn(power=-power, tacho_units=tachoUnits)

        else:
            left.weak_turn(power=0, tacho_units=0)
            right.weak_turn(power = 0, tacho_units=0)

    elif(angle > 45 and angle < 135):
        #tested
        if (delta_x == 0 and delta_y < 0):
            #180 degrees tested
            angle_rad = math.radians(180)
            angle_deg = (angle_rad) * (180/pi)
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho      

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x < 0 and delta_y == 0):
            #90 degrees right tested
            angle_rad = math.radians(90)
            angle_deg = (angle_rad) * (180/pi)
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x > 0 and delta_y == 0): 
            #90 degrees left tested
            angle_rad = math.radians(90)
            angle_deg = (angle_rad) * (180/pi)
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            right.weak_turn(power=power, tacho_units=tachoUnits)
            left.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x > 0 and delta_y > 0):
            # degrees in 1st quadrant tested
            angle_rad = math.atan2(delta_y, delta_x)
            angle_deg = 90 - ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            right.weak_turn(power=power, tacho_units=tachoUnits)
            left.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x > 0 and delta_y < 0):
            #degrees in 4th quadrant tested
            angle_rad = math.atan2((math.fabs(delta_y)), delta_x)
            angle_deg = 90 + ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            right.weak_turn(power=power, tacho_units=tachoUnits)
            left.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x < 0 and delta_y > 0):
            #degrees in 2nd quadrant tested
            angle_rad = math.atan2(delta_y, (math.fabs(delta_x)))
            angle_deg = 90 - ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x < 0 and delta_y < 0):
            #degrees in 3rd quadrant tested
            angle_rad = math.atan2((math.fabs(delta_y)), (math.fabs(delta_x)))
            angle_deg = 90 + ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        else:
            left.weak_turn(power=0, tacho_units=0)
            right.weak_turn(power = 0, tacho_units=0)

    elif(angle > 135 and angle < 225):
        #tested
        if (delta_x > 0 and delta_y == 0):
            #180 degrees tested
            angle_rad = math.radians(180)
            angle_deg = (angle_rad) * (180/pi)
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho      

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x == 0 and delta_y < 0):
            #90 degrees right tested
            angle_rad = math.radians(90)
            angle_deg = (angle_rad) * (180/pi)
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x == 0 and delta_y > 0): 
            #90 degrees left tested
            angle_rad = math.radians(90)
            angle_deg = (angle_rad) * (180/pi)
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            right.weak_turn(power=power, tacho_units=tachoUnits)
            left.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x > 0 and delta_y > 0):
            # degrees in 1st quadrant tested
            angle_rad = math.atan2(delta_y, delta_x)
            angle_deg = 90 + ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            right.weak_turn(power=power, tacho_units=tachoUnits)
            left.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x > 0 and delta_y < 0):
            #degrees in 4th quadrant tested
            angle_rad = math.atan2((math.fabs(delta_y)), delta_x)
            angle_deg = 90 + ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x < 0 and delta_y > 0):
            #degrees in 2nd quadrant tested
            angle_rad = math.atan2(delta_y, (math.fabs(delta_x)))
            angle_deg = 90 - ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            right.weak_turn(power=power, tacho_units=tachoUnits)
            left.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x < 0 and delta_y < 0):
            #degrees in 3rd quadrant tested
            angle_rad = math.atan2((math.fabs(delta_y)), (math.fabs(delta_x)))
            angle_deg = 90 - ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        else:
            left.weak_turn(power=0, tacho_units=0)
            right.weak_turn(power = 0, tacho_units=0)

    elif(angle > 225 and angle < 315):
        #tested
        if (delta_x == 0 and delta_y > 0):
            #180 degrees tested
            angle_rad = math.radians(180)
            angle_deg = (angle_rad) * (180/pi)
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho      

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x > 0 and delta_y == 0):
            #90 degrees right tested
            angle_rad = math.radians(90)
            angle_deg = (angle_rad) * (180/pi)
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x < 0 and delta_y == 0): 
            #90 degrees left tested
            angle_rad = math.radians(90)
            angle_deg = (angle_rad) * (180/pi)
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            right.weak_turn(power=power, tacho_units=tachoUnits)
            left.weak_turn(power=-power, tacho_units=tachoUnits)

        elif (delta_x > 0 and delta_y > 0):
            # degrees in 1st quadrant tested
            angle_rad = math.atan2(delta_y, delta_x)
            angle_deg = 90 + ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        elif(delta_x > 0 and delta_y < 0):
            #degrees in 4th quadrant tested
            angle_rad = math.atan2((math.fabs(delta_y)), delta_x)
            angle_deg = 90 - ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            left.weak_turn(power=power, tacho_units=tachoUnits)
            right.weak_turn(power=-power, tacho_units=tachoUnits)

        elif(delta_x < 0 and delta_y > 0):
            #degrees in 2nd quadrant tested
            angle_rad = math.atan2(delta_y, (math.fabs(delta_x)))
            angle_deg = 90 + ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            right.weak_turn(power=power, tacho_units=tachoUnits)
            left.weak_turn(power=-power, tacho_units=tachoUnits)

        elif(delta_x < 0 and delta_y < 0):
            #degrees in 3rd quadrant tested
            angle_rad = math.atan2((math.fabs(delta_y)), (math.fabs(delta_x)))
            angle_deg = 90 - ((angle_rad) * (180/pi))
            print angle_deg
            distanceTurned = (angle_deg/360) * (roboCturn)
            numberRotations = (distanceTurned) / (Circumference)
            tachoUnits = (numberRotations) * tacho

            right.weak_turn(power=power, tacho_units=tachoUnits)
            left.weak_turn(power=-power, tacho_units=tachoUnits)

        else:
            left.weak_turn(power=0, tacho_units=0)
            right.weak_turn(power = 0, tacho_units=0)