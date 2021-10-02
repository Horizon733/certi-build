import builder

def testtt(self):
    path = '../certi_builder/test_utillities/testexcel.xlsx'
    name_list = builder.get_names(path)
    name = name_list[0]
    print('abcd' == name)


