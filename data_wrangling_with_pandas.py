import pandas as pd
import numpy as np

EXAMPLES = ['Demonstrate creating dataframe',
            'Demonstrate crating dataframe using list',
            'Demonstrate crating df numpy array',
            'Demonstrate locating rows using index and location',
            'Demonstrate performing math opertaion on columns and print column as Series object',
            'Read data from csv file',
            'Demonstrate sort dataframe in decending orger using heapsort while keepint NaN values at bottom',
            'Demonstrate merging two dataframes',
            'Demonstrate concatination of two dataframes',
            'Demonstrate getting list of guest belongs to Actiog group',
            'Demonstrate renaming column "Group" to "Occupation"',
            'Demonstrate removing duplicate rows',
            'Demonstrate replacing NaN values with zero',
            'Demonstrate calculations',
            'Demonstrate saving dataframe in external file',
            ]

def run(input):
    if(input == 0): # create dataframe
        product_data=[['E-book', 2000], ['Plants', 6000], ['pencil', 3000]] # 2d list, similar to 2d array
        indexes=[1,2,3]
        columns_name=['product', 'unit_sold']
        product_df = pd.DataFrame(data=product_data, index=indexes, columns=columns_name)
        print(product_df)

    elif(input == 1): # crate df using list
        product_data={'product': ['E-book', 'Plants', 'pencil'], 'unit_sold': [2000, 5000, 3000]}
        product_df = pd.DataFrame(data=product_data)
        print(product_df)

    elif(input == 2): # crate df numpy array
        products = np.array([['','product','unit_sold'], [1, 'E-book', 2000],[2, 'Plants', 6000], [3, 'pencil', 3000]])
        product_df = pd.DataFrame(data=products[1:,1:], # [1:,1:] from first row till end, from first column till end
                                  index=products[1:,0], # [1:,0] from first row till end, only first column
                                  columns=products[0,1:]) # [1:,0] only first row, form first column till end
        print(product_df) # output is same as of first case

    elif(input == 3): # locating rows using index and location
        products = np.array([['','product','unit_sold'], ['a', 'E-book', 2000],[2, 'Plants', 6000], [3, 'pencil', 3000]])
        product_df = pd.DataFrame(data=products[1:,1:], # [1:,1:] from first row till end, from first column till end
                                  index=products[1:,0], # [1:,0] from first row till end, only first column
                                  columns=products[0,1:]) # [1:,0] only first row, form first column till end

        print(product_df)
        row = product_df.iloc[2]
        rows = product_df.iloc[0:2]
        print(row)
        print(rows)
        row = product_df.loc['a']
        print(row)
        print(product_df.at['2','product'])

    elif(input == 4): # perform opertaion on columns and print column as Series object
        product_data={'product': ['e-book', 'plants', 'pencil'], 'unit_sold': [2000, 5000, 3000]}
        product_df = pd.DataFrame(data=product_data)
        products = product_df['product'] # return column as series object
        print(products)
        gt_products = [product_df['unit_sold'] > 2500]
        gt_products = product_df['unit_sold'] > 2500 # return a series object of bool type for values greater than 2500
        print(gt_products)
        product_df['next_target'] = product_df['unit_sold']+ ( product_df['unit_sold'] * 10)/100
        print(product_df)

    elif(input == 5): # read data from csv file
        guest_list_df = pd.read_csv('daily_show_guests.csv', sep=',')
        print(guest_list_df.head(5))
##        guest_list_df = pd.read_excel('excelsheet_path.xlsx', sheet_name='Sheet1')
##        print(guest_list_df)        

    elif(input == 6): # sort dataframe in decending orger using heapsort while keepint NaN values at bottom
        guest_list_df = pd.read_csv('daily_show_guests.csv', sep=',')
        sorted_guest_df = guest_list_df.sort_values('GoogleKnowlege_Occupation', # sort by column
                                         ascending=False, # enable descending order
                                         kind='heapsort', #sorting algorithm
                                         na_position='last') # keep NaN value at last
        print(sorted_guest_df.head(5))

    elif(input == 7): # merge two dataframes
        guest_list_df = pd.read_csv('daily_show_guests.csv', sep=',')
        sorted_guest_df = pd.merge(guest_list_df.head(3),
                                   guest_list_df.tail(3),
                                   how='outer',
                                   indicator = True)
        print(sorted_guest_df)

    elif(input == 8): # concat two dataframes
        guest_list_df = pd.read_csv('daily_show_guests.csv', sep=',')
        top_df = guest_list_df.head(3)
        bottom_df = guest_list_df.tail(3)
        combined_guest_df = pd.concat( [top_df, bottom_df] )
        print(combined_guest_df)

    elif(input == 9): # get list of guest belongs to Actiog group
        guest_list_df = pd.read_csv('daily_show_guests.csv', sep=',')
        guest_group = guest_list_df.groupby('Group')
        print(guest_group.get_group('Acting'))

    elif(input == 10): # rename column 'Group' to 'Occupation'
        guest_list_df = pd.read_csv('daily_show_guests.csv', sep=',')
        guest_list_df = guest_list_df.rename(columns={'Group':'Occupation'}, index={1:10})
        print(guest_list_df.head(5))

    elif(input == 11): # remove duplicate rows
        df = pd.DataFrame({'Name':['Pavneet','Pavneet']}, index=[1,2])
        print(df.drop_duplicates(subset='Name'
                                 ,keep='last'))

    elif(input == 12): # replace NaN values with zero
        product_data={'product': ['E-book', 'Plants'], 'unit_sold': [12, np.NaN]}
        product_df = pd.DataFrame(data=product_data)
        product_df.fillna(0, inplace=True)
        print(product_df)

    elif(input == 13): # peform calculations
        product_df = pd.DataFrame(data={'product': ['E-book', 'Plants'],
                                        'unit_sold': [2000, 5000],
                                        'types': [800, 200]})
        print(product_df.describe())
        print("Mean of unit_sold")
        print(product_df['unit_sold'].mean())
        print("Mean value of rows")
        print(product_df.mean(axis=1))

    elif(input == 14): # save dataframe in external file
        product_df = pd.DataFrame(data={'product': ['E-book', 'Plants'],
                                'unit_sold': [2000, 5000],
                                'types': [800, 200]})
        product_df.to_csv('aa.csv',
                          index=False, # otherwise will add extra comman at start
                          sep=',',
                          encoding='utf-8')
        print('File Saved')

def printSelection():
    print('Enter Input: ')
    for i in range(0, len(EXAMPLES)):
        print('',i,'to',EXAMPLES[i], sep = ' ')

def executeAllCase():
    for i in range(0,15):
        print('case '+ str(i))
        run(i)

sep_len = 80

if __name__ == '__main__':
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.width', 800)
    pd.set_option('display.max_columns', None)
##    executeAllCase()
    while(True):
        print('\n'+('=' * sep_len))
        printSelection()
        choice = input('Enter choice: ')
        try:
            choice = int(choice)
        except ValueError:
            print('Invalid input, stop program')
            break
        if(choice not in range(0,15)):
            print('Invalid input, stoppin program')
            break
        print(EXAMPLES[choice]+'\n'+('=' * sep_len))
        run(choice)
