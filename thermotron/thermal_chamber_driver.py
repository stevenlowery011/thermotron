import visa

class thermal_chamber:
    def __init__(self, address_string):
        self.Address = address_string
        rm = visa.ResourceManager()
        self.instrument = rm.open_resource(self.Address)
    
    def ping(self):
        '''Check communication with thermal chamber. '''
        response = self.instrument.query('*IDEN?\r')
        return response.strip('\n').strip('\r')
        
    def goto_set_point(self, setpoint):
        ''' Sets the setpoint on current channel. Returns TRUE when setpoint +/- 0.5 degree C is reached'''
        self.instrument.write("L1S" + str(setpoint)+"\r")
        self.instrument.write("RM\r")
        return True
    
    def stop(self):
        '''Stop the chamber from running'''
        self.instrument.query('S\r')
        return self.instrument.last_status
    
    def current_temp(self):
        '''Returns current chamber temperature'''
        curr_temp = float(self.instrument.query('D1V\r'))
        return curr_temp
        