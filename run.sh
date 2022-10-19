#! /usr/bin/bash

# file name from the user input
read -p "Enter the csv file that you want to load: " fileName
echo "Loading file " $fileName

echo "Enter the action you want to perform: 
1->show country info; 
2->sort the dataset by total cases and return top 30 countries' name; "
read mode
if [ $mode -eq 1 ]
then
echo "You want to show specific country info"
read -p "Enter the country that you want to look at: " countryName
python3 app.py -d $countryName $fileName | tee output.txt
elif [ $mode -eq 2 ]
then
echo "You want to sort the dataset by total cases"
python3 app.py -s $fileName | tee output.txt
fi