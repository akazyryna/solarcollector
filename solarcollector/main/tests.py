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

        self.assertEqual(round(result, 2), 1.72)

    def test_formula_convers(self):
        result = formulas.formula_convers(47, 214.4, 392.3, 1.72, 0.2)

        self.assertEqual(round(result, 2), 1.37)

    @tag("")
    def test_formula_amount_energy(self):
        result = formulas.formula_amount_energy(1.37, 392.3)

        self.assertEqual(round(result, 2), 537.45)

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
        result = formulas.formula_spec_density_solrad(537.45, 13.76, 30)

        self.assertEqual(round(result, 2), 361.66)

    def test_formula_net_power_sc(self):
        result = formulas.formula_net_power_sc(0.398, 1, 361.66)

        self.assertEqual(round(result, 2), 143.94)

    def test_formula_flow_rate_sc(self):
        result = formulas.formula_flow_rate_sc(143.94, 4186, 55, 7)

        self.assertEqual(round(result, 2), 7.16)

    def test_formula_b(self):
        result = formulas.formula_b(1, 1.2)

        self.assertEqual(round(result, 2), 0.83)

    def test_formula_density_water(self):
        result = formulas.formula_density_water(55, 7)

        self.assertEqual(round(result, 2), 995.26)

    def test_formula_heat_carrier_speed(self):
        result = formulas.formula_heat_carrier_speed(7.16, 0.83, 0.012, 995.26)

        self.assertEqual(round(result, 2), 7.22)

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
        result = formulas.formula_reynolds_num(0.024, 7.22, 0.000000697)

        self.assertEqual(round(result, 3), 2.486)

    def test_formula_coef_heat_transfer(self):
        result = formulas.formula_coef_heat_transfer(0.62, 0.024, 2.486, 4.68, 4.68)

        self.assertEqual(round(result, 3), 10.162)

    def test_formula_heat_trans(self):
        result = formulas.formula_heat_trans(0.005, 220, 10.162)

        self.assertEqual(round(result, 2), 10.16)

    def test_formula_temp_plate(self):
        result = formulas.formula_temp_plate(55, 7, 143.94, 10.16)

        self.assertEqual(round(result, 2), 45.17)

    def test_formula_density_plate(self):
        result = formulas.formula_density_plate(45.17)

        self.assertEqual(round(result, 2), 999.14)

    def test_formula_thermal_cond_plate(self):
        result = formulas.formula_thermal_cond_plate(45.17)

        self.assertEqual(round(result, 3), 0.603)

    def test_formula_kinematic_viscosity_plate(self):
        result = formulas.formula_kinematic_viscosity_plate(45.17)

        self.assertEqual(round(result, 9), 0.000000765)

    def test_formula_prandtl_plate(self):
        result = formulas.formula_prandtl_plate(0.000000765, 4186, 999.14, 0.603)

        self.assertEqual(round(result, 2), 5.31)

    def test_formula_coef_heat_transfer_plate(self):
        result = formulas.formula_coef_heat_transfer_plate(0.62, 0.024, 2.486, 4.68, 5.31)

        self.assertEqual(round(result, 3), 9.846)

    def test_formula_thermal_cond_env(self):
        result = formulas.formula_thermal_cond_env(45.17, 19.57)

        self.assertEqual(round(result, 4), 0.0269)

    def test_formula_kinematic_viscosity_env(self):
        result = formulas.formula_kinematic_viscosity_env(45.17, 19.57)

        self.assertEqual(round(result, 7), 0.0000162)

    def test_formula_grashof(self):
        result = formulas.formula_grashof(47.17, 19.57, 9.81, 0.012, 0.0000162)

        self.assertEqual(round(result, 2), 5414.97)

