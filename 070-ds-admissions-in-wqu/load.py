""" Loading into a data frame """

import aggregate


<df_Name> = pd.DataFrame(result).rename(
  {"_id": "country_iso2"}, axis="columns").sort_values("count")
