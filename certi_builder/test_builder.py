import builder
import os


class TestBuilder:
    def test_name(self):
        path = "../certi_builder/test_utillities/testexcel.xlsx"
        name_list = builder.get_names(path)
        name = str(name_list[0])
        assert "abcd" == name

    def test_saved(self):
        image = "../certi_builder/test_utillities/certimg.png"
        name_excel = "../certi_builder/test_utillities/testexcel.xlsx"
        font_color = "#ffffff"
        font_path = "../certi_builder/test_utillities/ASMAN.TTF"
        out_location = "../certi_builder/test_utillities"
        builder.generate_certificate(
            image, name_excel, font_color, 123, 540, True, font_path, 12, out_location
        )
        get_name_list = builder.get_names(name_excel)
        get_name = str(get_name_list[0])
        exp_path = f"{out_location}\certificate_{get_name}.png"
        boolean = os.path.isfile(exp_path)
        os.remove(exp_path)
        assert True == boolean

    def test_hexcode(self):
        test_element = ["#3f871c", "#67gzs0", "#884444", "#786543f", "#7e707d"]
        test_result = [True, False, True, False, True]
        function_results = []
        for element in test_element:
            function_result = builder.validate_hex(element)
            function_results.append(function_result)

        assert test_result == function_results
