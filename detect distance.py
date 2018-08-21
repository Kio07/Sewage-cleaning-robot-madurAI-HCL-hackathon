# update the distances indicated by the proximity sensors
def _update_proximity_sensor_distances( self ):
    self.proximity_sensor_distances = [ 0.02-( log(readval/3960.0) )/30.0 for
        readval in self.robot.read_proximity_sensors() ]