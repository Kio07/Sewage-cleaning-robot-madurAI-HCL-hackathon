# calculate translational velocity
# velocity is v_max when omega is 0,
# drops rapidly to zero as |omega| rises
v = self.supervisor.v_max() / ( abs( omega ) + 1 )**0.5