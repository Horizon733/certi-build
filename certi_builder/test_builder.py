import builder 
import os

class TestBuilder:

    def test_name(self):
        path = '../certi_builder/test_utillities/testexcel.xlsx'
        name_list = builder.get_names(path)
        name = str(name_list[0])
        assert 'abcd' == name


    def test_saved(self):
        image = '../certi_builder/test_utillities/certimg.png'
        name_excel = '../certi_builder/test_utillities/testexcel.xlsx'
        font_color = '#ffffff'
        font_path = '../certi_builder/test_utillities/ASMAN.TTF'
        out_location = '../certi_builder/test_utillities'
        builder.generate_certificate(
            image,
            name_excel,
            font_color,
            123,
            540,
            True,
            font_path,
            12,
            out_location
        )
        get_name_list = builder.get_names(name_excel)
        get_name = str(get_name_list[0])
        exp_path = f"{out_location}\certificate_{get_name}.png"
        boolean = os.path.isfile(exp_path)
        os.remove(exp_path)
        assert True == boolean