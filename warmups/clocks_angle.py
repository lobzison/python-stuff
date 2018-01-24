"""
Task from interview
Calculate angle between hour and minute arrows
"""


def get_angle_between_h_and_m(hours, minutes):
    """
    Takes hours in format hh12 and minutes in format mi
    """
    rad = 360
    m_part = 1.0 / 60
    h_part = 1.0 / 12
    i_hours = int(hours)
    i_minutes = int(minutes)
    minute_angle = m_part * i_minutes
    hour_angle = h_part * i_hours + minute_angle * h_part
    diff = minute_angle - hour_angle
    diff = abs(diff * rad)
    diff = min(diff, rad - diff)
    return diff

print get_angle_between_h_and_m('06', '00')