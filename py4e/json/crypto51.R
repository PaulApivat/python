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


# Bubble Plot
df %>%
    slice(1:38) %>% 
    select(name, market_cap, hash_rate, attack_hourly_cost) %>%
    mutate(attack_hourly_cost = as.numeric(attack_hourly_cost)) %>%
    # consider removing Handshake
    filter(name != 'Bitcoin' & name != 'Ethereum' & name != 'Litecoin' & name != 'Handshake') %>%
    # remove 0 market cap
    filter(market_cap > 0) %>%
    ggplot(aes(x = market_cap, y = attack_hourly_cost, size = market_cap)) +
    geom_point(alpha = 0.7)


# Remove coins with no marketcap
# log10 transformation instead of segment by <M, M or B

# market_cap
df %>%
    slice(1:38) %>% 
    ggplot(aes(x=reorder(symbol, market_cap), y=market_cap, color = symbol)) +
    geom_point(aes(size = market_cap)) +
    geom_segment(aes(xend = symbol, yend = 0, color = symbol), size = 1) +
    theme(
        legend.position = 'none',
        axis.text.x = element_text(angle = 45, hjust = 1)
    ) +
    scale_y_log10(labels = scales::comma)
    
# attack_hourly_cost
df %>%
    slice(1:38) %>% 
    # change character to numeric
    mutate(attack_hourly_cost = as.numeric(attack_hourly_cost)) %>%
    ggplot(aes(x=reorder(symbol, attack_hourly_cost), y=attack_hourly_cost, color = symbol)) +
    geom_point(aes(size = market_cap)) +
    geom_segment(aes(xend = symbol, yend = 0, color = symbol), size = 1) +
    theme(
        legend.position = 'none',
        axis.text.x = element_text(angle = 45, hjust = 1)
    ) +
    scale_y_continuous(labels = scales::number_format(accuracy = 0.01))+
    scale_y_log10(labels = scales::comma)


# scatter_plot w/ log10 transformation
library(ggrepel)

df1 <- df1 %>%
    mutate(
        annotation = ifelse(market_cap > 60000000000, "yes", "no")
    )


df %>%
    slice(1:38) %>% 
    # change character to numeric
    mutate(attack_hourly_cost = as.numeric(attack_hourly_cost)) %>%
    ggplot(aes(x=market_cap, y=attack_hourly_cost)) +
    geom_point(aes(size = log10(market_cap), color = symbol), alpha = 0.8) +
    scale_y_log10(label= scales::dollar) +
    scale_x_log10(label= scales::dollar) +
    theme(
        legend.position = 'none'
    ) +
    geom_text_repel(data = df %>% filter(symbol =="BTC" & symbol=="ETH"), 
                    aes(label=name), size = 4)
    #geom_smooth(method = "lm", se = FALSE)


df1 %>%
    slice(1:38) %>% 
    filter(attack_hourly_cost != "?") %>% 
    # change character to numeric
    mutate(
        attack_hourly_cost = as.numeric(attack_hourly_cost)
    ) %>% 
    ggplot(aes(x=market_cap, y=attack_hourly_cost)) +
    geom_point(aes(size = log10(market_cap)), color = "white", alpha = 0.8) +
    scale_y_log10(label= scales::dollar) +
    scale_x_log10(label= scales::dollar) +
    theme_minimal() +
    theme(
        legend.position = 'none',
        panel.background = element_rect(fill = "dodger blue"),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        plot.background = element_rect(fill = "dodger blue"),
        plot.title = element_text(colour = "white", face = "bold", size = 30, 
                                  margin = margin(10,0,30,0)),
        plot.caption = element_text(color = "white"),
        axis.title = element_text(colour = "white", face = "bold"),
        axis.title.x = element_text(margin = margin(30,0,10,0)),
        axis.text = element_text(colour = "white", face = "bold"),
        axis.title.y = element_text(margin = margin(0,20,0,30), angle = 0)
    ) +
    labs(
        x = "Market Capitalization",
        y = "Attack\nHourly\nCost",
        title = "The More a Crypto Network is Worth,\n the Harder it is to Attack.",
        caption = "Data: www.crypto51.app | Graphics: @paulapivat"
    )


