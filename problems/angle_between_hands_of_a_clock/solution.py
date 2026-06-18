class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour_angle=((float(minutes)/60)*30 + (float(hour)/12)*360)%360
        min_angle=(float(minutes)/60)*360
        return min(abs(hour_angle-min_angle),abs((360-hour_angle)+min_angle),abs(360-min_angle)+hour_angle)
        