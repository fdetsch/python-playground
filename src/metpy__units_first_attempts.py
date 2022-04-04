from metpy.units import units

mins = 5 * units.minute
mins

secs = 30 * units.second

mins.to(
    units.second
) / secs
