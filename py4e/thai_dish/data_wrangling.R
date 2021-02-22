library(tidyverse)

# load data
df <- read_csv("thai_dishes.csv")

# exploratory
df %>% str()

# change column name
df <- df %>%
    rename(
        Thai_name = `Thai name`,
        Thai_script = `Thai script`,
        English_name = `English name`
    )

df %>%
    select(Description)

# tally Columns Region
df %>%
    group_by(Region) %>%
    tally(sort = TRUE)

df %>%
    count(Region)

df %>%
    count(`Thai name`)

# remove  \n from all columns
df$Thai_name <- gsub("[\n]", "", df$Thai_name)
df$Thai_script <- gsub("[\n]", "", df$Thai_script)
df$English_name <- gsub("[\n]", "", df$English_name)
df$Image <- gsub("[\n]", "", df$Image)
df$Region <- gsub("[\n]", "", df$Region)
df$Description <- gsub("[\n]", "", df$Description)

df$Image
df$Region
df$Description

## NOTE ##
## Web-Scrapping Process need to get text from links


