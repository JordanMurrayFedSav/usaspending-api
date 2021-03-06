FORMAT: 1A
HOST: https://api.usaspending.gov

# Download Count [/api/v2/download/count/]

These endpoints support the advanced search page and allow for complex filtering for specific subsets of spending data.

## POST

Returns the number of transactions that would be included in a download request for the given filter set.

+ Request (application/json)
    + Attributes (object)
        + `filters` (required, FilterObject)

+ Response 200 (application/json)
    + Attributes (object)
        + `transaction_rows_gt_limit` (required, boolean)
            A boolean returning whether the transaction count is over the maximum row limit.
        + `calculated_transaction_count` (required, number)
            The calculated count of all transactions which would be included in the download files.
        + `maximum_transaction_limit` (required, number)
            The current allowed maximum number of transactions in a row-limited download. Visit https://www.usaspending.gov/#/download_center/custom_award_data to download larger volumes of data.
        + `messages` (optional, array[string])
            An array of warnings or instructional directives to aid consumers of this endpoint with development and debugging.
    + Body

            {
                "calculated_transaction_count": 87343,
                "maximum_transaction_limit": 500000,
                "transaction_rows_gt_limit": false,
                "messages": ["For searches, time period start and end dates are currently limited to an earliest date of 2007-10-01.  For data going back to 2000-10-01, use either the Custom Award Download feature on the website or one of our download or bulk_download API endpoints as listed on https://api.usaspending.gov/docs/endpoints."]
            }

# Data Structures

## FilterObject (object)
+ `keywords`: `transport` (optional, array[string])
+ `time_period` (optional, array[TimePeriodObject], fixed-type)
+ `place_of_performance_scope` (optional, enum[string])
    + Members
        + `domestic`
        + `foreign`
+ `place_of_performance_locations` (optional, array[LocationObject], fixed-type)
+ `agencies` (optional, array[AgencyObject], fixed-type)
+ `recipient_search_text`: `Hampton` (optional, array[string])
+ `recipient_id` (optional, string)
    A hash of recipient DUNS, name, and level. A unique identifier for recipients, used for profile page urls.
+ `recipient_scope` (optional, enum[string])
    + Members
        + `domestic`
        + `foreign`
+ `recipient_locations` (optional, array[LocationObject], fixed-type)
+ `recipient_type_names`: `category_business` (optional, array[string])
+ `award_type_codes` (optional, FilterObjectAwardTypes)
+ `award_ids`: `SPE30018FLGFZ`, `SPE30018FLJFN`  (optional, array[string])
    Award IDs surrounded by double quotes (e.g. `"SPE30018FLJFN"`) will perform exact matches as opposed to the default, fuzzier full text matches.  Useful for Award IDs that contain spaces or other word delimiters.
+ `award_amounts` (optional, array[AwardAmounts], fixed-type)
+ `program_numbers`: `10.331` (optional, array[string])
+ `naics_codes`: `311812` (optional, array[string])
+ `psc_codes`: `8940`, `8910` (optional, array[string])
+ `contract_pricing_type_codes`: `J` (optional, array[string])
+ `set_aside_type_codes`: `NONE` (optional, array[string])
+ `extent_competed_type_codes`: `A` (optional, array[string])
+ `tas_codes` (optional, array[TASCodeObject], fixed-type)

## TimePeriodObject (object)
+ `start_date`: `2017-10-01` (required, string)
    Currently limited to an earliest date of `2007-10-01` (FY2008).  For data going back to `2000-10-01` (FY2001), use either the Custom Award Download
    feature on the website or one of our `download` or `bulk_download` API endpoints.
+ `end_date`: `2018-09-30` (required, string)
    Currently limited to an earliest date of `2007-10-01` (FY2008).  For data going back to `2000-10-01` (FY2001), use either the Custom Award Download
    feature on the website or one of our `download` or `bulk_download` API endpoints.
+ `date_type` (optional, enum[string])
    + Members
        + `action_date`
        + `last_modified_date`

## LocationObject (object)
+ `country`: `USA` (required, string)
+ `state`: `VA` (optional, string)
+ `county` (optional, string)
+ `city` (optional, string)
+ `district` (optional, string)
+ `zip` (optional, string)

## AgencyObject (object)
+ `type` (required, enum[string])
    + Members
        + `awarding`
        + `funding`
+ `tier` (required, enum[string])
    + Members
        + `toptier`
        + `subtier`
+ `name`: `Department of Defense` (required, string)

## AwardAmounts (object)
+ `lower_bound` (optional, number)
+ `upper_bound`: 1000000 (optional, number)

## TASCodeObject (object)
+ `ata` (optional, string, nullable)
    Allocation Transfer Agency Identifier - three characters
+ `aid`: `000` (required, string)
    Agency Identifier - three characters
+ `bpoa` (optional, string, nullable)
    Beginning Period of Availability - four digits
+ `epoa` (optional, string, nullable)
    Ending Period of Availability - four digits
+ `a` (optional, string, nullable)
    Availability Type Code - X or null
+ `main`: `3500` (required, string)
    Main Account Code - four digits
+ `sub` (optional, string, nullable)
    Sub-Account Code - three digits

## FilterObjectAwardTypes (array)
List of filterable award types

### Sample
- A
- B
- C
- D

### Default
- 02
- 03
- 04
- 05
- 06
- 07
- 08
- 09
- 10
- 11
- A
- B
- C
- D
- IDV_A
- IDV_B
- IDV_B_A
- IDV_B_B
- IDV_B_C
- IDV_C
- IDV_D
- IDV_E
