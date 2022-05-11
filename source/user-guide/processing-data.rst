.. _processing_data:

Managing Data
=============================

Once data has been collected, you will
need to verify a few things before you
access your final results. 

In localisation, you tried to identify units, 
crops, and livestock which are likely to appear
in the survey. It is impossible to anticipate
all potential values which might come up in the 
survey. Enumerators are given the option to input
unexpected values using "free-text-entry" fields.
We do not want this data to be lost, and we give 
project managers the opportunity to verify new values.


.. note::

    Unit extraction, price calculations, and data 
    processing take time. Wait for each stage to 
    finish. The results will load automatically

.. youtube:: LF95SrwI62M
    :width: 100%

|



1. Verifying Units
#######################################

The main units which need to be converted are summarised 
below with examples:

.. list-table:: 
   :widths: 25 50 25 25
   :header-rows: 1

   * - Unit type 
     - Description
     - Example Survey Value 
     - Example Conversion 

   * - bees_honey_production_units 
     - The conversion factor should be used to convert to kilograms/litres.
     - buckets_12_litre 
     - 12 
  
   * - country
     - The conversion factor should be used to convert country names to `two-letter ISO country codes <https://www.iban.com/country-codes>`_.  
     - uganda 
     - UG 

   * - crop_name 
     - The name of crops entered in the survey. Often enumerators may specify "other" crops in a free-text-entry field. Sometimes these crops can be mispelt, or in a language other than English. Here we correct mispellings and translations into standard forms (**all lower case**)  
     - maze 
     - maize 

   * - crop_sold_price_quantityunits
     - The price units for crops which were sold. Please note that only one unit will be converted into a string, "total_income_per_year" will be converted to "total_income_per_year" as this is treated as a special case in the analysis scripts.
     - price_per_50kg_sack
     - 0.02 

   * - crop_yield_units
     - The unit of crops which have been collected. This needs to be converted to kilograms
     - cart_250kg
     - 250

     
   * - eggs_sold_price_timeunits
     - The amount of money made per unit time for selling eggs. This needs to be converted into an income per year
     - income for 3 months
     - 4

   * - eggs_units 
     - The number of eggs collected per year
     - pieces/day
     - 365
     
   * - fertiliser_units 
     - The amount of fertiliser in kg
     - sacks_25kg
     - 25
     
   * - livestock_name 
     -
     -
     -
     
   * - milk_sold_price_timeunits 
     - The names of livestock entered in the survey. As with crop names, enumerators can also enter extra livestock names which are in a different language or mispelt. This conversion is used to standardise livestock names entered in the survey
     - month
     - month
   
   * - 
     - 
     - 0.3_litres
     - 0.3
     
   * - milk_units 
     - The amount of milk  collected in litres per year. There are a number of exceptions which must be kept as text strings, and are dealt with in the analysis scripts (e.g. "per animal per day" and "l/animal/day"
     - l/day
     - 365
     
   * - unitland 
     - The amount of land in hectares
     - acres
     - 0.4




2. Checking Prices and Calories
#######################################

Price verification is show in the video above. 
The main points to note are prices **prices for
products** (e.g. crops, meat, milk) must be in 
local currency units (LCU) per kg or per litre. 
Price for whole livestock must be in LCU per animal.



3. Accessing Results
#######################################

Once units and prices have been verified. It should be
possible to access your final results. If you collect
more data, you will need to check any new units and 
prices again. 