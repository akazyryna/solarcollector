import math as m


# часовой угол захода Солнца для горизонтальной поверхности
def formula_for_horizontal(lat, horz_angle):
    return m.degrees(m.acos(-m.tan(m.radians(lat)) * m.tan(m.radians(horz_angle))))


def formula_for_inclination(lat, horz_angle, incn_angle):
    return m.degrees(m.acos(-m.tan(m.radians(lat - incn_angle)) * m.tan(m.radians(horz_angle))))


# часовой угол захода Солнца для наклонной поверхности
def formula_min(formula_for_horizontal, formula_for_inclination):
    return min(formula_for_horizontal, formula_for_inclination)


# коэффициент пересчета прямого излучения с горизонтальной на наклонную поверхность
def formula_conversion_factor(lat, incn_angle, formula_min, horz_angle, formula_for_horizontal):
    return ((m.cos(m.radians(lat - incn_angle)) * m.cos(m.radians(horz_angle)) * m.sin(m.radians(formula_min))) + (
            (m.pi / 180) * m.radians(formula_min) * m.sin(m.radians(lat - incn_angle)) * m.sin(
        m.radians(horz_angle)))) / ((m.cos(m.radians(lat)) * m.cos(m.radians(horz_angle)) * m.sin(
        m.radians(formula_for_horizontal))) + (m.sin(m.radians(lat)) * m.sin(m.radians(horz_angle)) * (
            m.pi / 180) * m.radians(formula_for_horizontal)))


# коэффициент пересчета солнечной радиации для наклонной поверхности с южной ориентацией
def formula_convers(incn_angle, ed, e, formula_conversion_factor, ro):
    return ((1 - (ed / e)) * formula_conversion_factor) + (((1 + m.cos(m.radians(incn_angle))) / 2) * (ed / e)) + (
            ro * ((1 - m.cos(m.radians(incn_angle)) / 2)))


# среднемесячное дневное количество солнечной энергии
def formula_amount_energy(formula_convers, e):
    return formula_convers * e


# средняя суточная тепловая нагрузка
def formula_monthly_heat_load(heat_cap, daily_dis, hot_temp, cold_temp):
    return (heat_cap * daily_dis * (hot_temp - cold_temp)) / 10 ** 5


# средняя месячная тепловая нагрузка
def formula_avrg_monthly_heat_load(formula_monthly_heat_load, n, nd):
    return (formula_monthly_heat_load * n * nd) / 10


# среднемесячная продолжительность в месяце
def formula_avrg_monthly_durt(lat, horz_angle):
    return (2 / 15) * (m.degrees(m.acos(-m.tan(m.radians(lat)) * m.tan(m.radians(horz_angle)))))


# удельная плоность солнечного излучения
def formula_spec_density_solrad(formula_amount_energy, formula_avrg_monthly_durt, nd):
    return (formula_amount_energy / (formula_avrg_monthly_durt * nd * 3600)) * 10 ** 6


# полезная мощность гелиоколлектора
def formula_net_power_sc(efficiency, square, formula_spec_density_solrad):
    return efficiency * square * formula_spec_density_solrad


# расход жидкости через гелиоколлектор
def formula_flow_rate_sc(formula_net_power_sc, heat_cap, hot_temp, cold_temp):
    return (formula_net_power_sc / (heat_cap * (hot_temp - cold_temp))) * 10 ** 4


def formula_b(square, length_pipe):
    return square / length_pipe


# плоность воды
def formula_density_water(hot_temp, cold_temp):
    return 1005 / (0.99534 + 0.466 * 10 ** -3 * ((hot_temp + cold_temp) / 2))


# скорость теплоносителя в канале
def formula_heat_carrier_speed(formula_flow_rate_sc, formula_b, channel_height, formula_density_water):
    return ((formula_flow_rate_sc) * 10 ** -4 / (formula_b * channel_height * formula_density_water)) * 10 ** 5


# коэффициент теплопроводности воды
def formula_thermal_cond_water(hot_temp, cold_temp):
    return 0.5514 + (0.2588 * 10 ** -2) * ((hot_temp + cold_temp) / 2) - (0.1278 * 10 ** -4) * (
            (hot_temp + cold_temp) / 2) ** 2


# коэффициент кинематической вязкости воды
def formula_kinematic_viscosity_water(hot_temp, cold_temp):
    return m.exp(m.exp(33.23 - 5.93043 * m.log(((hot_temp + cold_temp) / 2) + 273)) - 0.87) * 10 ** -6


# число Прандтля для воды
def formula_prandtl_water(formula_kinematic_viscosity_water, heat_cap, formula_density_water,
                          formula_thermal_cond_water):
    return (
                   formula_kinematic_viscosity_water * (
               heat_cap) * formula_density_water) / formula_thermal_cond_water


# эквивалентный диаметр
def formula_equivalent_diameter(channel_height):
    return 2 * channel_height


# число Рейнольдса
def formula_reynolds_num(formula_equivalent_diameter, formula_heat_carrier_speed, formula_kinematic_viscosity_water):
    return (formula_equivalent_diameter * (formula_heat_carrier_speed) * 10 ** -5) / formula_kinematic_viscosity_water


# коэффициент теплоотдачи от поглощающей панели к теплоносителю для ламинарного режима
def formula_coef_heat_transfer(formula_thermal_cond_water, formula_equivalent_diameter, formula_reynolds_num,
                               formula_prandtl_water, prandtl_plate):
    return (formula_thermal_cond_water / formula_equivalent_diameter) * (0.15 * (formula_reynolds_num) ** 0.33) * (
            (formula_prandtl_water) ** 0.43) * (formula_prandtl_water / prandtl_plate) ** 0.25


# коэффициент теплопередачи от поглощающей панели к теплоносителю
def formula_heat_trans(plate_thickness, thermal_cond_plate, formula_coef_heat_transfer):
    return ((plate_thickness / thermal_cond_plate) + (1 / formula_coef_heat_transfer)) ** -1


# температура поглощающей панели
def formula_temp_plate(hot_temp, cold_temp, formula_net_power_sc, formula_heat_trans):
    return ((hot_temp + cold_temp) / 2) + (formula_net_power_sc / formula_heat_trans)


# плотность для пластины
def formula_density_plate(formula_temp_plate):
    return 1005 / (0.99534 + 0.466 * 10 ** -3 * (formula_temp_plate) / 2)


# коэффициент теплопроводности пластины
def formula_thermal_cond_plate(formula_temp_plate):
    return 0.5514 + (0.2588 * 10 ** -2) * ((formula_temp_plate) / 2) - (0.1278 * 10 ** -4) * (
            (formula_temp_plate) / 2) ** 2


# коэффициент кинематической вязкости пластины
def formula_kinematic_viscosity_plate(formula_temp_plate):
    return m.exp(m.exp(33.23 - 5.93043 * m.log(((formula_temp_plate) / 2) + 273)) - 0.87) * 10 ** -6


# число Прандтля для пластины
def formula_prandtl_plate(formula_kinematic_viscosity_plate, heat_cap, formula_density_plate,
                          formula_thermal_cond_plate):
    return (
                   formula_kinematic_viscosity_plate * (
               heat_cap) * formula_density_plate) / formula_thermal_cond_plate


# коэффициент теплоотдачи от поглощающей панели к теплоносителю для ламинарного режима (пластина)
def formula_coef_heat_transfer_plate(formula_thermal_cond_water, formula_equivalent_diameter, formula_reynolds_num,
                                     formula_prandtl_water, formula_prandtl_plate):
    return (formula_thermal_cond_water / formula_equivalent_diameter) * (0.15 * (formula_reynolds_num) ** 0.33) * (
            (formula_prandtl_water) ** 0.43) * (formula_prandtl_water / formula_prandtl_plate) ** 0.25


# коэффициент теплопроводности среды
def formula_thermal_cond_env(formula_temp_plate, temp_glass):
    return (2.43 + 0.008 * (formula_temp_plate + temp_glass) / 2) * 10 ** -2


# коэффициент кинематической вязкости среды
def formula_kinematic_viscosity_env(formula_temp_plate, temp_glass):
    return (13.28 + 0.09 * (formula_temp_plate + temp_glass) / 2) * 10 ** -6


# число Грасгофа
def formula_grashof(formula_temp_plate, temp_glass, g, channel_height, formula_kinematic_viscosity_env):
    return 1 / (273 + ((formula_temp_plate + temp_glass) / 2)) * g * (formula_temp_plate - temp_glass) * (
            (channel_height) ** 3) / ((formula_kinematic_viscosity_env) ** 2)


# коэффициент конвективного теплообмена
def formula_convect_transfer(formula_thermal_cond_env, channel_height, incn_angle, formula_grashof):
    return (formula_thermal_cond_env / channel_height) * (0.060 - 0.00019 * incn_angle) * (formula_grashof) ** 0.333


# радиационный коэффициент
def formula_radiation_coef(boltzman, formula_temp_plate, temp_glass, blackness_plate, blackness_glass):
    return (boltzman / ((formula_temp_plate - temp_glass) * ((1 / blackness_plate) + (1 / blackness_glass) - 1))) * (
            (((formula_temp_plate + 273) / 100) ** 4) - (((temp_glass + 273) / 100) ** 4))


# коэффициент теплоотдачи для свободной конвекции
def formula_free_convection(incn_angle, temp_glass, temp_air):
    return (2.26 - 0.0067 * incn_angle) * (temp_glass - temp_air) ** 0.33


# радиационный коэффициент теплопередачи
def formula_radiation_transfer(boltzman, blackness_glass, temp_glass, temp_air):
    return (boltzman * blackness_glass / (temp_glass - temp_air)) * (
            (((temp_glass + 273) / 100) ** 4) - (((temp_air + 273) / 100) ** 4))


# коэффициент потерь
def formula_loss_factor(formula_convect_transfer, formula_radiation_coef, width_surface, cond_surface,
                        formula_free_convection, formula_radiation_transfer):
    return ((1 / (formula_convect_transfer + formula_radiation_coef)) + (width_surface / cond_surface) + (
            1 / (formula_free_convection + formula_radiation_transfer))) ** -1


# действительную температуру остекления
def formula_temp_glass(temp_air, formula_temp_plate, formula_loss_factor, formula_free_convection,
                       formula_radiation_transfer):
    return temp_air + (formula_temp_plate - temp_air) * (
            formula_loss_factor / (formula_free_convection + formula_radiation_transfer))


# коэффициент теплопроводности среды (с действительной температурой стекла)
def formula_thermal_cond_gl(formula_temp_plate, formula_temp_glass):
    return (2.43 + 0.008 * (formula_temp_plate + formula_temp_glass) / 2) * 10 ** -2


# коэффициент кинематической вязкости среды
def formula_kinematic_viscosity_env_gl(formula_temp_plate, formula_temp_glass):
    return (13.28 + 0.09 * (formula_temp_plate + formula_temp_glass) / 2) * 10 ** -6


# число Грасгофа
def formula_grashof_gl(formula_temp_plate, formula_temp_glass, g, channel_height, formula_kinematic_viscosity_env_gl):
    return 1 / (273 + ((formula_temp_plate + formula_temp_glass) / 2)) * g * (
            formula_temp_plate - formula_temp_glass) * (
                   (channel_height) ** 3) / ((formula_kinematic_viscosity_env_gl) ** 2)


# коэффициент конвективного теплообмена
def formula_convect_transfer_gl(formula_thermal_cond_gl, channel_height, incn_angle, formula_grashof_gl):
    return (formula_thermal_cond_gl / channel_height) * (0.060 - 0.00019 * incn_angle) * (
        formula_grashof_gl) ** 0.333


# радиационный коэффициент
def formula_radiation_coef_gl(boltzman, formula_temp_plate, formula_temp_glass, blackness_plate, blackness_glass):
    return (boltzman / (
            (formula_temp_plate - formula_temp_glass) * ((1 / blackness_plate) + (1 / blackness_glass) - 1))) * (
                   (((formula_temp_plate + 273) / 100) ** 4) - (((formula_temp_glass + 273) / 100) ** 4))


# коэффициент теплоотдачи для свободной конвекции
def formula_free_convection_gl(incn_angle, formula_temp_glass, temp_air):
    return (2.26 - 0.0067 * incn_angle) * (formula_temp_glass - temp_air) ** 0.33


# радиационный коэффициент теплопередачи
def formula_radiation_transfer_gl(boltzman, blackness_glass, formula_temp_glass, temp_air):
    return (boltzman * blackness_glass / (formula_temp_glass - temp_air)) * (
            (((formula_temp_glass + 273) / 100) ** 4) - (((temp_air + 273) / 100) ** 4))


# коэффициент потерь
def formula_loss_factor_gl(formula_convect_transfer_gl, formula_radiation_coef_gl, width_surface, cond_surface,
                           formula_free_convection_gl, formula_radiation_transfer_gl):
    return ((1 / (formula_convect_transfer_gl + formula_radiation_coef_gl)) + (width_surface / cond_surface) + (
            1 / (formula_free_convection_gl + formula_radiation_transfer_gl))) ** -1


# действительную температуру остекления
def formula_temp_gl(temp_air, formula_temp_plate, formula_loss_factor_gl, formula_free_convection_gl,
                    formula_radiation_transfer_gl):
    return temp_air + (formula_temp_plate - temp_air) * (
            formula_loss_factor_gl / (formula_free_convection_gl + formula_radiation_transfer_gl))


# коэффициент эффективности
def formula_efficiency_coefficient(formula_loss_factor_gl, formula_coef_heat_transfer_plate, plate_thickness,
                                   thermal_cond_plate):
    return (1 / formula_loss_factor_gl) / (
            (1 / formula_coef_heat_transfer_plate) + (plate_thickness / thermal_cond_plate) + (1 / formula_loss_factor_gl))


# действительный КПД гелиоколлектора
def formula_kpd(optical_efficiency, formula_loss_factor, hot_temp, cold_temp, temp_air, formula_spec_density_solrad,
                formula_efficiency_coefficient):
    return (optical_efficiency - formula_loss_factor * ((((
                                                                  hot_temp + cold_temp) / 2) - temp_air) / formula_spec_density_solrad)) * formula_efficiency_coefficient


# En
def formula_en(formula_amount_energy, nd):
    return formula_amount_energy / nd


# Qk
def formula_qk(formula_kpd, square, formula_en):
    return formula_kpd * square * formula_en
