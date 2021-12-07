import pandas as pd
from transform_functions import * 



def convert_country_code():

    # ASSEMBLE 
    input_df = pd.main_df({
        "country": ["Finland","Denmark"],
    })

    expected_df = pd.main_df({
        "code": ["FI","DK"], 
    })

    # ACT 
    output_df = convert_country_code(input_df=input_df)

    # ASSERT 

    pd.testing.assert_frame_equal(left=output_df, right=expected_df,check_exact=True)