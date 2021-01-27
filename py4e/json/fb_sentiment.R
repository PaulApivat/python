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
    select(row:pos) %>%
    pivot_longer(cols = neg:pos, names_to = 'polarity', values_to = 'value') %>%
    #group_by(row) %>%
    ggplot(aes(x = row, y = value, fill=polarity)) +
    geom_area() +
    theme_minimal() +
    scale_fill_manual(values = c("#ef8a62", "black", "#67a9cf")) +     # "#f7f7f7"
    theme(
        legend.position = 'bottom'
    ) +
    labs(
        x = "Posts",
        y = "Value",
        fill = "Polarity",
        title = "Facebook Post Polarity Index: 2006 - 2020",
        subtitle = "Using Python NLTK Vader Library",
        caption = "Data & Visualization: @paulapivat"
    )

# Line Chart: positive
df3 %>%
    select(row:pos) %>%
    pivot_longer(cols = neg:pos, names_to = 'polarity', values_to = 'value') %>%
    filter(polarity=='pos') %>%
    ggplot(aes(x = row, y = value)) +
    geom_line(color = "#69b3a2") +
    theme_minimal() +
    labs(
        title = "Positivity Scores: Facebook Post 2006 - 2020",
        subtitle = "Using Python NLTK Vader Library",
        caption = "Data & Visualization: @paulapivat",
        x = "Sentences",
        y = "Positivity Score"
    )

# Line Chart: negative
df3 %>%
    select(row:pos) %>%
    pivot_longer(cols = neg:pos, names_to = 'polarity', values_to = 'value') %>%
    filter(polarity=='neg') %>%
    ggplot(aes(x = row, y = value)) +
    geom_line(color = "#404080") +
    theme_minimal()+
    labs(
        title = "Negativity Scores: Facebook Post 2006 - 2020",
        subtitle = "Using Python NLTK Vader Library",
        caption = "Data & Visualization: @paulapivat",
        x = "Sentences",
        y = "Negativity Score"
    )



# Density is harder to interpret

# density plot: neg, neu or pos
df3 %>%
    select(row:pos) %>%
    pivot_longer(cols = neg:pos, names_to = 'polarity', values_to = 'value') %>%
    filter(polarity=='pos') %>%
    ggplot(aes(x = value)) +
    geom_density(fill="#69b3a2", color="#e9ecef", alpha=0.8)

# double sided density
df3 %>%
    select(row:pos) %>%
    #pivot_longer(cols = neg:pos, names_to = 'polarity', values_to = 'value') %>%
    ggplot(aes(x=row))+
    geom_density(aes(x=neg, y = ..density..), fill="#69b3a2")+
    geom_density(aes(x=pos, y = -..density..), fill= "#404080")

# Histogram: Positive
df3 %>%
    select(row:pos) %>%
    pivot_longer(cols = neg:pos, names_to = 'polarity', values_to = 'value') %>%
    filter(polarity=='pos') %>%
    filter(value > 0) %>%
    ggplot(aes(x = value)) +
    geom_histogram(fill="#69b3a2") +
    theme_minimal() +
    labs(
        title = "Distribution of Positivity Scores",
        subtitle = "Facebook Posts 2006 - 2020",
        caption = "Data & Visualization: @paulapivat",
        x = "Positivity Score",
        y = "Number of Sentences"
    )

# Histogram: Negative
df3 %>%
    select(row:pos) %>%
    pivot_longer(cols = neg:pos, names_to = 'polarity', values_to = 'value') %>%
    filter(polarity=='neg') %>%
    filter(value > 0) %>%
    ggplot(aes(x = value)) +
    geom_histogram(fill="#404080")+
    theme_minimal() +
    labs(
        title = "Distribution of Negativity Scores",
        subtitle = "Facebook Posts 2006 - 2020",
        caption = "Data & Visualization: @paulapivat",
        x = "Negativity Score",
        y = "Number of Sentences"
    )


# Histogram: Both Overlap
df3 %>%
    select(row:pos) %>%
    pivot_longer(cols = neg:pos, names_to = 'polarity', values_to = 'value') %>%




sum(df3$neg)
sum(df3$pos)
