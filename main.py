from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

def main():
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.
    #directory = requests.request('GET', 'http://www.al-mishkat.com/words/part2/')
    #soup = BeautifulSoup(directory.content, 'html.parser')
    #links = soup.findAll('a')
    #for i, link in enumerate(links):
    #    print(i, link)
    #we concluded from the above print that the range of required linkes is 34 to 62

    data = pd.DataFrame(columns=['الموضع', 'الكلمة'])
    for i in range(34, 62):
        link_str = 'http://www.al-mishkat.com/words/part2/' + '{0}'.format(str(i-33).zfill(2)) + '.htm'
        #data = data.append(extract_from_page(link_str, data))
        #print(data)
        data = extract_from_page(link_str, data)
        data.to_csv('words_positions_quran.csv', mode="a") #unicode utf-8  export the csv from excel sheet
        #csv.writer('words_positions_quran.csv', )
    #print(data)
    #data.to_csv()

def extract_from_page(link_str, data):
    page = requests.request('GET', link_str)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(page.url)
    spans = soup.findAll('span')

    i=0
    for i, span in enumerate(spans):
        #print(i, span)
        # we conclude from the above print that we should skip first span and last span and that spans are duplicated
        if i==0 or i==len(span)-1 or i%2==0:
            pass
        else:
            #remove the *
            my_list = span.text.replace('*','').replace('\r','').replace('\n','').replace('\xa0','').rsplit(':-')
            if len(my_list) == 2:
                data = data.append({'الكلمة':[my_list[0]],'الموضع':[my_list[1]]}, ignore_index=True)
    print('Data of single page:')
    print(data)
    return data
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
