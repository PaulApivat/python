library(tidyverse)

# load data
df <- read_csv("sent_sentiment.csv")       # 3194
df2 <- read_csv('sent_sentiment_2.csv')    # 12776

# create row column for df
df1 <- df %>%
    mutate(row = row_number())

# long-to-wide for df2
# note: create a unique identifier for each label then use pivot_wider
# source: https://stackoverflow.com/questions/58837773/pivot-wider-issue-values-in-values-from-are-not-uniquely-identified-output-w

df3 <- df2 %>%
    group_by(label) %>%
    mutate(row = row_number()) %>%
    pivot_wider(names_from = label, values_from = values) %>%
    left_join(df1, by = 'row') %>%
    select(row, sentence, neg:compound, numbers) 

# df3 Overall summary 
# neg 96.561
# neu 2526.149
# pos 568.288

df3 %>%
    select(sentence:pos) %>%
    pivot_longer(cols = neg:pos, names_to = 'polarity', values_to = 'value') %>%
    ggplot(aes(x = sentence, y = value, fill=polarity)) +
    geom_area()
    

