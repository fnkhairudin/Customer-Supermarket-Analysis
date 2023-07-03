def readfilepandas(file):
    """Fungsi untuk membaca read csv file menggunakan pandas

    Args:
        file: string excel/csv file name ('.....'.csv/excel)
    
    Return:
        df : DataFrame
    """
    import pandas as pd
    import pyinputplus as pyip

    # userinput file extension
    choices = ['csv', 'excel']
    userinput = pyip.inputMenu(prompt='Which one is your file extension ?\n', choices=choices, numbered=True)
    if userinput == 'csv':
        # userinput1 = 
        df = pd.read_csv(file)
    elif userinput == 'excel':
        df = pd.read_excel(file)

    return df


def qualitydf(df):
    """Fungsi untuk menampilkan columns, data_type, null_value(%), number_unique, zero_value, negative_value, sample_unique
    
    Args:
        df: DataFrame

    Return:
        DataFrame yang berisi yang telah disebutkan diatas
    """
    import pandas as pd
    pd.options.display.max_rows = 50
    pd.set_option('max_colwidth', None)
    df = pd.DataFrame(
                {
                'columns': df.columns.values,
                'data_type': df.dtypes.values,
                'null_value(%)': df.isna().mean().values * 100,
                'n_unique': df.nunique().values,
                'zero_value' : [True if (df[col] == 0).any() else False for col in df.columns],
                'neg_value' : [True if (df[col].dtype == int or df[col].dtype == float) and (df[col] < 0).any() else False for col in df.columns],
                'sample_unique': [df[col].unique() for col in df.columns]
                }
            )

    return df


def checkdf(df):
    """Fungsi untuk mengecek df.info dan df.describe

    Args:
        df : DataFrame
    """
    from IPython.display import display
    print('----------------- df.info() -----------------')
    a = df.info()
    print('\n----------------- df.describe() -----------------')
    b = df.describe()
    
    return display(a,b)


def dropduplicated(df):
    print(f"Jumlah data duplikat : {df[df.duplicated()].shape[0]}")
    df = df.drop_duplicates(keep='first', inplace=True, ignore_index=True) # True : reset index
    
    return df


def checkquantiles(df,cols):
    """Function for check interval between min, q1 (quantile 0.25), q2 (quantile 0.5), q3 (quantile 0.75), and q4 (quantile 1)
    
    Args:
        df : DataFrame
        cols (string) : which column you want to know the quantity of (numerical (continue) column)
    Return:
        tuple : (min,q1,q2,q3,q4)
    """
    
    min = df[cols].min()
    q1 = int(df[cols].quantile([0.25]).values)
    q2 = int(df[cols].quantile([0.5]).values)
    q3 = int(df[cols].quantile([0.75]).values)
    q4 = int(df[cols].quantile([1]).values)

    return min,q1,q2,q3,q4

def ageclass(df, cols):
    """Function to make age classification as new column. 
        How to use:
        - df[cols] = df.apply(ageclass, args=('age',), axis=1) 
            #### cols : name of your new column, for instance: age_category
            #### args ('age') : name of your age column

    Args:
        df : DataFrame
        cols (string) : name of the age column
    Return:
        age classification:
        - Children (1 year through 12 years)
        - teenagers (13 years through 17 years)
        - Adults (18 years through 39 years)
        - Middle-aged Adults (40 years thorough 59 years)
        - old adults (60 years and older)
    """
    if df[cols] <= 12:
        return 'childrens'
    elif df[cols] <= 17:
        return 'teenagers'
    elif df[cols] <= 39:
        return 'adults'
    elif df[cols] <= 59:
        return 'middle-aged adults'
    else:
        return 'old adults'