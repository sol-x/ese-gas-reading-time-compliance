def check_gas_testing_time_compliance() -> bool:
    # Put your code here
    import pandas as pd
    import numpy as np
    
    df1 = pd.read_csv('periodical_gas_reading.csv')
    df2 = pd.read_csv('entrant_gas_reading.csv')
    
    if (df1['gas reading time'] > df2['entry time']) & (df1['gas reading time'] < df2['exit time']):
        return True

if __name__ == "__main__":
    if check_gas_testing_time_compliance():
        print("Compliant")
    else:
        print("Not Compliant")
