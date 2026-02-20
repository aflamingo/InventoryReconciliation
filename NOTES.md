### How I approached the problem
I approached the exercise in steps: setup and load, inspect and clean, reconcile, and output.

Following is the logic I used for each step

#SETUP AND LOAD - prepare your working environment
	1. install and import packates (pandas, numpy, datetime)
	2. read in data snapshots
	3. put name of data snapshots into list to support flexible code (easier to reuse)
 
#INSPECT AND CLEAN - review the data, clean discrepancies and quality issues
	First make column names and data types match, then begin comparison of values within snapshots.
	
	1. Make column names match: used general clean of column names: make all lower, trim values to remove extra spaces, replace spaces in column name to "_", then started compare of column names. Found and normalized discrepancies (see assuptions).
	2. Standardize data types between snapshots.
	3. Review data within rows: first used general clean of values to make all lower and remove extra spaces. Making all values lower makes it easier to compare since python is case sensitive.
	4. Replaced NA with 0 for all columns

#Reconcile - identify differences between snapshots
	1. Megerged dataframes using an outer join. Added column for "qty_diff" to show varience in quantity.
	2. Used variable to identify records in common, removed, or added. Created three separate outputs.

#Assumptions 
1. Assumed "sku" is key value between snapshots
2. Mapping of Column Names
		product_name -> name, 
		qty -> quantity, 
		warehouse -> location
		updated_at -> last_counted

#Data Quality Issues:
1. mismatch of column names
2. mismatch of data types: quantity, last_counted
3. mismatch of sku format: removed "-" and make upper for easier handling
4. review mismatch between product names
	

