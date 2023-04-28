# DAX30-GoogleTrends

## Introduction

A sister program of the DAX30-Analyser (see https://github.com/tombo92/DAX30-Analyser.git).

* requests Google Trends data per the pyTrends API for each word in the keywords list
* each keyword category has its own .xlsx file of the compiled data, with the general search data as well as the filtered AI-specific search data
* data extracted to be compared and analysed with corresponding absolute figures requested from KeywordsEverywhere (see https://keywordseverywhere.com/)

## Table of Contents

1. [Introduction](#Introduction)
2. [How to use](#Howtouse)
   1. [Setup](#Setup)
   2. [Usage](#Usage)

## How to use

### Setup

* The tool is written in Python and the version **3.8.6** is used.
* **Installation of used libaries**
  The used libaries (that are not installed by default) are listed in the **`requirements.txt`** file.
  To install them use the command: 
  ```console
  pip install -r requirements.txt
  ```

### Usage

The keywords.xlsx file should consist of lists of keywords separated into columns with the column title pertaining to the category to which the subseqent keywords belong. This file should be placed into the main folder. The script is requests the Google Trends data of each keyword and exports it into the `extracted_data` folder as a `<category name>.xlsx` file for each category in the file. The Google trends data is requested twice; once where each keyword is considered as a general search term (`cat=0`) and once where each keyword is considered as an AI-specific search term (`cat=1299`). The produced files are therefore stored in subfolders within the  `extracted_data` folder `cat_general` and `cat_ai`.
