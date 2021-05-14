import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def sh1():
    """ Show given files columns """
    demo = pd.read_excel('Worksheet in Business case Interview.xlsx', sheet_name=0)
    print(demo.columns)

    """ Filter only our required columns from given file """
    df_gr = demo.loc[:, ['GR_PO_NUM', 'BTCH_NUM', 'Process Step', 'Site', 'Start Date', 'End Date']]
    print(df_gr)
    print("")

    """ Identity and removethe Duplicate values from the combination of columns 
        GR_PO_NUM, BTCH_NUM, Start_Date """
    dup = df_gr.duplicated(subset=['GR_PO_NUM', 'BTCH_NUM', 'Start Date']).sum()
    print("Total number of Duplicates from the combination of three columns :{}".format(dup))
    df_gr = df_gr.drop_duplicates(subset=['GR_PO_NUM', 'BTCH_NUM', 'Start Date'])
    print(df_gr)
    print("")

    """ Create Lead Time column from difference between the End Date and Start Date Columns"""
    df_gr['Lead Time'] = [int(i.days) for i in (df_gr['End Date'] - df_gr['Start Date'])]
    print(df_gr)
    print("\n Description of the DataFame")
    print(df_gr.describe())
    print("")

    """ Filter Lead Time column for make result more accuracy
        from greater the 0 and less than 100 """
    df_gr = df_gr[df_gr['Lead Time'] > 0]
    df_gr = df_gr[df_gr['Lead Time'] < 100]
    print("\n Apply the control limit to the Lead Time 0 to 100")
    print(df_gr)
    print("\n Description of the DataFrame After limits")
    print(df_gr['Lead Time'].describe())

    """ Avoid Weekend days like Sunday using 
        print((df_gr['Start Date'].dt.weekday>5).sum()) """

    """ List the Unique objects and respective counts """
    print("\nList of Sites and their counts\n", df_gr['Site'].value_counts())
    print("\nList of Process Step and their counts\n", df_gr['Process Step'].value_counts())
    print("")

    """Two way Frequency table to Identify the occurrence of different combination"""

    print(pd.crosstab(index=df_gr['Start Date'].dt.year, columns=df_gr['Site'], margins=True))
    print("")
    print(pd.crosstab(index=df_gr['Start Date'].dt.month, columns=df_gr['Site'], margins=True))
    print("")
    print(pd.crosstab(index=df_gr['End Date'].dt.year, columns=df_gr['Site'], margins=True))
    print("")
    print(pd.crosstab(index=df_gr['End Date'].dt.month, columns=df_gr['Site'], margins=True))
    print("")
    print(pd.crosstab(index=df_gr['Site'], columns=df_gr['Lead Time'], margins=True))
    print("")

    print(pd.crosstab(index=df_gr['Start Date'].dt.year, columns=df_gr['Process Step'], margins=True))
    print("")
    print(pd.crosstab(index=df_gr['Start Date'].dt.month, columns=df_gr['Process Step'], margins=True))
    print("")
    print(pd.crosstab(index=df_gr['End Date'].dt.year, columns=df_gr['Process Step'], margins=True))
    print("")
    print(pd.crosstab(index=df_gr['End Date'].dt.month, columns=df_gr['Process Step'], margins=True))
    print("")
    print(pd.crosstab(index=df_gr['Process Step'], columns=df_gr['Lead Time'], margins=True))
    print("")

    df_gr["Lead_Time"] = df_gr["Lead Time"]

    print(pd.crosstab(index=df_gr['Process Step'], columns=df_gr['Site'], margins=True))
    print("")

    print("\n Mean Lead Time based on Site")
    print(df_gr.groupby(['Site']).Lead_Time.mean())

    print("\n Mean Lead Time based on Process Step")
    print(df_gr.groupby(['Process Step']).Lead_Time.mean())

    print("\n Mean Lead Time based on Started Year ")
    print(df_gr.groupby(df_gr['Start Date'].dt.year).Lead_Time.mean())
    print("\n Mean Lead Time based on Started Month")
    print(df_gr.groupby(df_gr['Start Date'].dt.month).Lead_Time.mean())
    print("\n Mean Lead Time based on Ended Year ")
    print(df_gr.groupby(df_gr['End Date'].dt.year).Lead_Time.mean())
    print("\n Mean Lead Time based on Ended Month")
    print(df_gr.groupby(df_gr['End Date'].dt.month).Lead_Time.mean())

    sns.boxplot(x=df_gr['Lead Time'], y=df_gr['Process Step'], hue=df_gr['Site'])

    # plt.plot(df_gr.groupby(df_gr['Start Date'].dt.month).Lead_Time.mean())
    # plt.plot(df_gr['Start Date'].dt.month.value_counts().sort_index())
    # plt.title("Mean Lead Time and Counts Based on Start Month")
    # plt.xlabel("Month")
    # plt.ylabel("Mean Lead Time / Total Count")

    plt.show()


def sh2():
    demo = pd.read_excel('Worksheet in Business case Interview.xlsx', sheet_name=1, na_values=['?', '#', '#1'])
    # print(demo)

    df_pr = demo.loc[:, ['ORDER_NUM', 'MFG_BTCH_NUM', 'Process Step', 'Site', 'Start Date', 'End Date']]
    print(df_pr)
    print(df_pr.isnull().sum())
    df_pr = df_pr.dropna(subset=['End Date'])
    df_pr = df_pr.dropna(subset=['MFG_BTCH_NUM'])
    print(df_pr.isnull().sum())

    """ Identity and removethe Duplicate values from the combination of columns 
        ORDER_NUM, MFG_BTCH_NUM, Start_Date """
    dup = df_pr.duplicated(subset=['ORDER_NUM', 'MFG_BTCH_NUM']).sum()
    print("Total number of Duplicates from the combination of three columns :{}".format(dup))

    """ Create Lead Time column from difference between the End Date and Start Date Columns"""
    df_pr['Lead Time'] = [int(i.days) for i in (df_pr['End Date'] - df_pr['Start Date'])]
    print(df_pr)
    print("\n Description of the DataFame")
    print(df_pr.describe())
    print("")

    """ Filter Lead Time column for make result more accuracy
        from greater the 0 """
    df_pr = df_pr[df_pr['Lead Time'] > 0]
    df_pr = df_pr[df_pr['Lead Time'] < 166]
    print("\n Apply the control limit to the Lead Time 0 to 100")
    print(df_pr)
    print("\n Description of the DataFrame After limits")
    print(df_pr['Lead Time'].describe())

    """ Avoid Weekend days like Sunday using
        print((df_gr['Start Date'].dt.weekday>5).sum()) """

    """ List the Unique objects and respective counts """
    print("\nList of Sites and their counts\n", df_pr['Site'].value_counts())
    print("\nList of Process Step and their counts\n", df_pr['Process Step'].value_counts())
    print("")

    """Two way Frequency table to Identify the occurrence of different combination"""

    print(pd.crosstab(index=df_pr['Start Date'].dt.year, columns=df_pr['Site'], margins=True))
    print("")
    print(pd.crosstab(index=df_pr['Start Date'].dt.month, columns=df_pr['Site'], margins=True))
    print("")
    print(pd.crosstab(index=df_pr['End Date'].dt.year, columns=df_pr['Site'], margins=True))
    print("")
    print(pd.crosstab(index=df_pr['End Date'].dt.month, columns=df_pr['Site'], margins=True))
    print("")
    print(pd.crosstab(index=df_pr['Site'], columns=df_pr['Lead Time'], margins=True))
    print("")

    print(pd.crosstab(index=df_pr['Start Date'].dt.year, columns=df_pr['Process Step'], margins=True))
    print("")
    print(pd.crosstab(index=df_pr['Start Date'].dt.month, columns=df_pr['Process Step'], margins=True))
    print("")
    print(pd.crosstab(index=df_pr['End Date'].dt.year, columns=df_pr['Process Step'], margins=True))
    print("")
    print(pd.crosstab(index=df_pr['End Date'].dt.month, columns=df_pr['Process Step'], margins=True))
    print("")
    print(pd.crosstab(index=df_pr['Process Step'], columns=df_pr['Lead Time'], margins=True))
    print("")

    df_pr["Lead_Time"] = df_pr["Lead Time"]

    print(pd.crosstab(index=df_pr['Process Step'], columns=df_pr['Site'], margins=True))
    print("")

    print("\n Mean Lead Time based on Site")
    print(df_pr.groupby(['Site']).Lead_Time.mean())

    print("\n Mean Lead Time based on Process Step")
    print(df_pr.groupby(['Process Step']).Lead_Time.mean())

    print("\n Mean Lead Time based on Started Year ")
    print(df_pr.groupby(df_pr['Start Date'].dt.year).Lead_Time.mean())
    print("\n Mean Lead Time based on Started Month")
    print(df_pr.groupby(df_pr['Start Date'].dt.month).Lead_Time.mean())
    print("\n Mean Lead Time based on Ended Year ")
    print(df_pr.groupby(df_pr['End Date'].dt.year).Lead_Time.mean())
    print("\n Mean Lead Time based on Ended Month")
    print(df_pr.groupby(df_pr['End Date'].dt.month).Lead_Time.mean())

    sns.boxplot(x=df_pr['Lead Time'], y=df_pr['Process Step'], hue=df_pr['Site'])

    # plt.plot(df_pr.groupby(df_pr['Start Date'].dt.month).Lead_Time.mean())
    # # plt.plot(df_pr['Start Date'].dt.month.value_counts().sort_index())
    # plt.title("Mean Lead Time and Counts Based on Start Month")
    # plt.xlabel("Month")
    # plt.ylabel("Mean Lead Time")

    plt.show()


if __name__ == "__main__":
    print(" Welcome to the Business Case Analytics Area!")
    print("Two sheets insights are here :")
    print("1.) GR-QR")
    print("2.) PR-QR")
    choose = int(input("Enter the number (1 or 2) to choose Which file you need first:"))
    if choose == 1:
        sh1()
    elif choose == 2:
        sh2()
    else:
        print("Enter valid Input!")
