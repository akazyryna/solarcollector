import math as m


def formula_for_horizontal(lat, horz_angle):
    return m.degrees(m.acos(-m.tan(m.radians(lat)) * m.tan(m.radians(horz_angle))))


def formula_for_inclination(lat, horz_angle, incn_angle):
    return m.degrees(m.acos(-m.tan(m.radians(lat - incn_angle)) * m.tan(m.radians(horz_angle))))


def formula_min(formula_for_horizontal, formula_for_inclination):
    return min(formula_for_horizontal, formula_for_inclination)


def formula_conversion_factor(lat, incn_angle, formula_min, horz_angle, formula_for_horizontal):
    return ((m.cos(m.radians(lat - incn_angle)) * m.cos(m.radians(horz_angle)) * m.sin(m.radians(formula_min))) + (
            (m.pi / 180) * m.radians(formula_min) * m.sin(m.radians(lat - incn_angle)) * m.sin(
        m.radians(horz_angle)))) / ((m.cos(m.radians(lat)) * m.cos(m.radians(horz_angle)) * m.sin(
        m.radians(formula_for_horizontal))) + (m.sin(m.radians(lat)) * m.sin(m.radians(horz_angle)) * (
            m.pi / 180) * m.radians(formula_for_horizontal)))


def formula_convers(incn_angle, ed, e, formula_conversion_factor, ro):
    return ((1 - (ed / e)) * formula_conversion_factor) + (((1 + m.cos(m.radians(incn_angle))) / 2) * (ed / e)) + (
            ro * ((1 - m.cos(m.radians(incn_angle)) / 2)))


def formula_amount_energy(formula_convers, e):
    return formula_convers * e
