library(tidyverse)

df <- read_csv("crypto51.csv")

str(df)

# Bar Chart Without Outliers
df %>%
    select(name, market_cap, hash_rate, attack_hourly_cost) %>%
    mutate(attack_hourly_cost = as.numeric(attack_hourly_cost)) %>%
    # consider removing Handshake
    filter(name != 'Bitcoin' & name != 'Ethereum' & name != 'Litecoin') %>%
    ggplot(aes(x = reorder(name, attack_hourly_cost), y = attack_hourly_cost)) +
    geom_bar(stat = "identity") +
    geom_line() +
    theme(
        axis.text.x = element_text(angle = 45, hjust = 1)
    )


df %>%
    select(name, market_cap, hash_rate, attack_hourly_cost) %>%
    mutate(attack_hourly_cost = as.numeric(attack_hourly_cost)) %>%
    # consider removing Handshake
    filter(name != 'Bitcoin' & name != 'Ethereum' & name != 'Litecoin' & name != 'Handshake') %>%
    # remove 0 market cap
    filter(market_cap > 0) %>%
    ggplot(aes(x = market_cap, y = attack_hourly_cost)) +
    geom_point()+
    geom_smooth(method = 'lm', formula = y~x, se = FALSE)


library(ggExtra)

p <- df %>%
    select(name, market_cap, hash_rate, attack_hourly_cost) %>%
    mutate(attack_hourly_cost = as.numeric(attack_hourly_cost)) %>%
    # consider removing Handshake
    filter(name != 'Bitcoin' & name != 'Ethereum' & name != 'Litecoin' & name != 'Handshake') %>%
    # remove 0 market cap
    filter(market_cap > 0) %>%
    ggplot(aes(x = market_cap, y = attack_hourly_cost)) +
    geom_point()

 
ggMarginal(p, type = "histogram") 
