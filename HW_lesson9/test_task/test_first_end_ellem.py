from utils import first_end_ellem
import pytest




l_example=[([2, 3, 5, 9, 3],[6, 27, 25]),([25, 3, 5, 9, 3,6,7,8],[200, 21, 30, 27]),([12, 3, 25, 9, 3,55,9,4,1],[12, 12, 225, 495, 9]),([20, 13, 55, 19, 0],[0, 247, 3025])]

@pytest.mark.parametrize('array, expected_result', l_example)


def test_first_end_ellem(array,expected_result):

    assert first_end_ellem(array) == expected_result
 

@pytest.mark.parametrize('expected_expeption, array', [(TypeError,5)]) # array =1  #TypeError: object of type 'int' has no len()
                                                 
def  test_type_int_error(expected_expeption,array):

     with pytest.raises(expected_expeption):
        first_end_ellem(array) == expected_expeption


@pytest.mark.parametrize('expected_expeption, array', [(TypeError,['1','55','56','5'])]) # array =['1','55','56','5'] TypeError: unsupported operand type(s) for +=: 'int' and 'str'
                                                 
def  test_type_str_error(expected_expeption,array):

     with pytest.raises(expected_expeption):
        first_end_ellem(array) == expected_expeption


                