import pandas as pd
from transform_functions import * 



def test_convert_country_code():

    # ASSEMBLE 
    input_df = pd.DataFrame({
        "id": [1,2],
        "country": ["Finland","Denmark"],
    })

    # expected_df = pd.main_df({
    #     "id": [1,2],
    #     "code": ["FI","DK"], 
    # })
    expected_result = ["FL","DK"]

    # ACT 
    codes = convert_country_code(main_df=input_df)

    # ASSERT 
    assert expected_result == codes

