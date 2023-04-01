#Introduction
#In this section, please describe the dataset you are using. 
#Include a link to the source of this data. 
#You should also provide some explanation on why you choose this dataset.

#I found my data on kaggle - https://www.kaggle.com/datasets/ashishraut64/global-methane-emissions
#'The following dataset has information about methane gas emissions globally'
#I choose this dataset because I am curious how this data will look visualilly.


#Data exploration
#Summary statistics means, medians, quartiles,
#Missing value information
#Any other relevant information about the dataset.

import pandas as pd
import matplotlib.pyplot as plt

#import data into DF
emisions = 'Methane_final.csv'
df_emm = pd.read_csv(emisions, header=0)

#drop the unnamed column since this is jsut the row #
df_emm = df_emm.drop('Unnamed: 0', axis=1)
#display column names
df_emm.columns
#header
df_emm.head
#summary stats
df_emm.describe()



#Data wrangling
#lets round the emissions column to 2 decimal places 
df_emm['emissions'] = df_emm['emissions'].round(2)
print(df_emm['emissions'])
#lets break out the data into 2 dataframes - one for 2022 and the other for 2019-2021 and excluding region world
df_2022 = df_emm.loc[(df_emm['baseYear'] == '2022') & (df_emm['region'] != 'World')] #2022
df_19_21 = df_emm.loc[(df_emm['baseYear'] == '2019-2021') & (df_emm['region'] != 'World')] #2019-2021


#Visualizations 
#part 1

#chart 1 - here we are looking at the 4 different emission types and the amount that each have by using a bar graph
#create bar chart and add labels to axis, title
plt.bar(df_emm['type'], df_emm['emissions'], label='emission amount')
plt.title('Emissions by Type', fontsize=35)
plt.xlabel('Type')
plt.ylabel('Emission Amount')
plt.legend(loc="upper right")
plt.show()

#chart 2 - this is the same as chart 1 - here we are manipulating the title size and locaition of the legend
#move legend outside chart and changing fontsize 
plt.bar(df_emm['type'], df_emm['emissions'], label='emission amount')
plt.xlabel('Type')
plt.ylabel('Emission Amount')
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.tight_layout()
plt.title('Emission Type', fontsize=10)
plt.show()

#chart 3 - here, we are layering 2022 and 2019-2021 to see how the region has been affected by the emission amounts
#adding color and markers to plt
plt.plot(df_2022['emissions'], df_2022['region'], marker='o', label='2022', color='purple')
plt.plot(df_19_21['emissions'], df_19_21['region'], marker='x', label='2019-2021', color='red')
plt.legend(loc='lower right')
plt.xlabel('Emission Amount')
plt.ylabel('Region')
plt.title('Emission Amounts by Region: 2022v2019-2021')
plt.show()


#part 2- recreate in seaborn
import seaborn as sns

#chart 1 (see above for comments)
sns.set_style('whitegrid')
sns.barplot(data=df_emm, x='type', y='emissions', label='emission amount')
plt.xlabel('Type')
plt.ylabel('Emission Amount')
plt.title('Emissions by Type', fontsize=35)
plt.legend(loc="upper right")
plt.show()

#chart 2 (see above for comments)
sns.set_style('whitegrid')
sns.barplot(data=df_emm, x='type', y='emissions', label='emission amount')
plt.xlabel('Type')
plt.ylabel('Emission Amount')
plt.title('Emission Type', fontsize=10)
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.tight_layout()
plt.show()

#chart 3 (see above for comments)
sns.set_style('whitegrid')
sns.scatterplot(data=df_2022, x='emissions', y='region', marker='o', color='purple', label='2022')
sns.scatterplot(data=df_19_21, x='emissions', y='region', marker='x', color='red', label='2019-2021')
plt.legend(loc='lower right')
plt.xlabel('Emission Amount')
plt.ylabel('Region')
plt.title('Emission Amounts by Region: 2022 vs 2019-2021')
plt.show()


#part 3
#we can see that matplot lib is used to create a more generic/easy chart whereas seaborn is more of an advanced package to use for creating charts
#the big difference is how we determine the plot type - for example, in matplotlib we use plt.plot and in seaborn we use sns.scatterplot


#Conclusion
#in conclusion, we can see that 2022 has higher amounts of emissions, especially in the Asia Pacific, Russia & Caspian, and North America regions.
#We can also see that the overall emission type is primarily caused by agriculture and energy. 
#there is plenty more to explore within this dataset, but at a high overview, I can confidently say that emission levels have risen from 2019. 
