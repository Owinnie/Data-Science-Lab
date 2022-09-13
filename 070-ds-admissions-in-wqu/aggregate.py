""" Using the aggregate method() """

import imports


# aggregate by nationality
result = <collectionName>.aggregate(
    [
        {
            "$group": {"_id": "$countryISO2", "count": {"$count": {}}}
        }
    ]
)
