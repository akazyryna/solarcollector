from django.test import TestCase, tag

from . import formulas


class FormulasTests(TestCase):
    def test_formula_for_horizontal(self):
        result = formulas.formula_for_horizontal(54, 9.4)

        self.assertEqual(round(result, 2), 103.17)

    def test_formula_for_inclination(self):
        result = formulas.formula_for_inclination(54, 9.4, 47)

        self.assertEqual(round(result, 2), 91.16)

    def test_formula_min(self):
        result = formulas.formula_min(103.17, 91.16)

        self.assertEqual(result, 91.16)

    def test_formula_conversion_factor(self):
        result = formulas.formula_conversion_factor(54, 47, 91.16, 9.4, 103.17)

        self.assertEqual(round(result, 2), 1.26)

    def test_formula_convers(self):
        result = formulas.formula_convers(47, 214.4, 392.3, 1.26, 0.2)

        self.assertEqual(round(result, 2), 1.06)

    @tag("")
    def test_formula_amount_energy(self):
        result = formulas.formula_amount_energy(1.06, 392.3)

        self.assertEqual(round(result, 2), 415.84)

    '''
    def test_formula_monthly_heat_load(self):
        result = formulas.formula_monthly_heat_load(4186, 80, 55, 7)

        self.assertEqual(round(result, 2), 160.74)

    def test_formula_avrg_monthly_heat_load(self):
        result = formulas.formula_avrg_monthly_heat_load(160.74, 1, 30)

        self.assertEqual(round(result, 2), 482.22)

    def test_formula_avrg_monthly_durt(self):
        result = formulas.formula_avrg_monthly_durt(54, 9.4)

        self.assertEqual(round(result, 2), 13.76)

    def test_formula_spec_density_solrad(self):
        result = formulas.formula_spec_density_solrad(415.84, 13.76, 30)

        self.assertEqual(round(result, 2), 279.82)

    def test_formula_net_power_sc(self):
        result = formulas.formula_net_power_sc(0.3976, 1, 279.82)

        self.assertEqual(round(result, 2), 111.26)

    def test_formula_flow_rate_sc(self):
        result = formulas.formula_flow_rate_sc(111.26, 4186, 55, 7)

        self.assertEqual(round(result, 2), 5.54)

    def test_formula_b(self):
        result = formulas.formula_b(1, 1.2)

        self.assertEqual(round(result, 2), 0.83)

    def test_formula_density_water(self):
        result = formulas.formula_density_water(55, 7)

        self.assertEqual(round(result, 2), 995.26)

    def test_formula_heat_carrier_speed(self):
        result = formulas.formula_heat_carrier_speed(5.54, 0.83, 0.012, 995.26)

        self.assertEqual(round(result, 2), 5.59)

    def test_formula_thermal_cond_water(self):
        result = formulas.formula_thermal_cond_water(55, 7)

        self.assertEqual(round(result, 2), 0.62)

    def test_formula_kinematic_viscosity_water(self):
        result = formulas.formula_kinematic_viscosity_water(55, 7)

        self.assertEqual(round(result, 9), 0.000000697)

    def test_formula_prandtl_water(self):
        result = formulas.formula_prandtl_water(0.000000697, 4186, 995.26, 0.62)

        self.assertEqual(round(result, 2), 4.68)

    def test_formula_equivalent_diameter(self):
        result = formulas.formula_equivalent_diameter(0.012)

        self.assertEqual(round(result, 3), 0.024)

    def test_formula_reynolds_num(self):
        result = formulas.formula_reynolds_num(0.024, 5.59, 0.000000697)

        self.assertEqual(round(result, 3), 1.925)

    def test_formula_coef_heat_transfer(self):
        result = formulas.formula_coef_heat_transfer(0.62, 0.024, 1.925, 4.68, 4.68)

        self.assertEqual(round(result, 3), 9.34)

    def test_formula_heat_trans(self):
        result = formulas.formula_heat_trans(0.005, 220, 9.34)

        self.assertEqual(round(result, 2), 9.34)

    def test_formula_temp_plate(self):
        result = formulas.formula_temp_plate(55, 7, 111.26, 9.34, 1)

        self.assertEqual(round(result, 2), 42.91)

    def test_formula_density_plate(self):
        result = formulas.formula_density_plate(42.91)

        self.assertEqual(round(result, 2), 989.82)

    def test_formula_thermal_cond_plate(self):
        result = formulas.formula_thermal_cond_plate(42.91)

        self.assertEqual(round(result, 3), 0.639)

    def test_formula_kinematic_viscosity_plate(self):
        result = formulas.formula_kinematic_viscosity_plate(42.91)

        self.assertEqual(round(result, 9), 0.000000629)

    def test_formula_prandtl_plate(self):
        result = formulas.formula_prandtl_plate(0.000000629, 4186, 989.82, 0.639)

        self.assertEqual(round(result, 2), 4.08)

    def test_formula_coef_heat_transfer_plate(self):
        result = formulas.formula_coef_heat_transfer_plate(0.62, 0.024, 1.925, 4.68, 4.08)

        self.assertEqual(round(result, 3), 9.666)

    def test_formula_thermal_cond_env(self):
        result = formulas.formula_thermal_cond_env(42.91, 19.57)

        self.assertEqual(round(result, 4), 0.0268)

    def test_formula_kinematic_viscosity_env(self):
        result = formulas.formula_kinematic_viscosity_env(42.91, 19.57)

        self.assertEqual(round(result, 6), 0.000016)

    def test_formula_grashof(self):
        result = formulas.formula_grashof(42.91, 19.57, 9.81, 0.018, 0.000016)

        self.assertEqual(round(result, 2), 17144.75)

    def test_formula_convect_transfer(self):
        result = formulas.formula_convect_transfer(0.0268, 0.018, 47, 17144.75)

        self.assertEqual(round(result, 3), 1.954)

    def test_formula_radiation_coef(self):
        result = formulas.formula_radiation_coef(5.67, 42.91, 19.57, 0.9, 0.4)

        self.assertEqual(round(result, 3), 2.45)

    def test_formula_free_convection(self):
        result = formulas.formula_free_convection(47, 19.57, 5.3)

        self.assertEqual(round(result, 2), 4.68)

    def test_formula_radiation_transfer(self):
        result = formulas.formula_radiation_transfer(5.67, 0.4, 19.57, 5.3)

        self.assertEqual(round(result, 3), 2.111)

    def test_formula_loss_factor(self):
        result = formulas.formula_loss_factor(1.954, 2.45, 0.004, 50, 4.68, 2.111)

        self.assertEqual(round(result, 3), 2.671)

    def test_formula_temp_glass(self):
        result = formulas.formula_temp_glass(5.3, 42.91, 2.671, 4.68, 2.111)

        self.assertEqual(round(result, 2), 20.09)

    def test_formula_thermal_cond_gl(self):
        result = formulas.formula_thermal_cond_gl(42.91, 20.09)

        self.assertEqual(round(result, 4), 0.0268)

    def test_formula_kinematic_viscosity_env_gl(self):
        result = formulas.formula_kinematic_viscosity_env_gl(42.91, 20.09)

        self.assertEqual(round(result, 6), 0.000016)

    def test_formula_grashof_gl(self):
        result = formulas.formula_grashof_gl(42.91, 20.09, 9.81, 0.018, 0.000016)

        self.assertEqual(round(result, 2), 16748.46)

    def test_formula_convect_transfer_gl(self):
        result = formulas.formula_convect_transfer_gl(0.0268, 0.018, 47, 16748.46)

        self.assertEqual(round(result, 3), 1.939)

    def test_formula_radiation_coef_gl(self):
        result = formulas.formula_radiation_coef_gl(5.67, 42.91, 20.09, 0.9, 0.4)

        self.assertEqual(round(result, 3), 2.456)

    def test_formula_free_convection_gl(self):
        result = formulas.formula_free_convection_gl(47, 20.09, 5.3)

        self.assertEqual(round(result, 2), 4.73)

    def test_formula_radiation_transfer_gl(self):
        result = formulas.formula_radiation_transfer_gl(5.67, 0.4, 20.09, 5.3)

        self.assertEqual(round(result, 3), 2.117)

    def test_formula_loss_factor_gl(self):
        result = formulas.formula_loss_factor_gl(1.939, 2.456, 0.004, 50, 4.73, 2.117)

        self.assertEqual(round(result, 3), 2.676)

    def test_formula_temp_gl(self):
        result = formulas.formula_temp_gl(5.3, 42.91, 2.676, 4.73, 2.117)

        self.assertEqual(round(result, 2), 20.0)

    def test_formula_efficiency_coefficient(self):
        result = formulas.formula_efficiency_coefficient(2.676, 9.666, 0.005, 220)

        self.assertEqual(round(result, 3), 0.783)

    def test_formula_kpd(self):
        result = formulas.formula_kpd(0.75, 2.676, 55, 7, 5.3, 279.82, 0.783)

        self.assertEqual(round(result, 3), 0.395)

    def test_formula_en(self):
        result = formulas.formula_en(415.84, 30)

        self.assertEqual(round(result, 3), 13.861)

    def test_formula_qk(self):
        result = formulas.formula_qk(0.395, 1, 13.861)

        self.assertEqual(round(result, 3), 5.475)
    '''
