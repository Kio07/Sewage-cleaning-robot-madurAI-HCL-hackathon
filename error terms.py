# calculate the error terms
theta_d = atan2( self.gtg_heading_vector[1], self.gtg_heading_vector[0] )

# calculate angular velocity
omega = self.kP * theta_d