#'
#' Erick Orellana
#' 
#' Final Exam Problem 5
#' 
#' Code to generate a graph to showcase logistic regression
#'

geom_jitter(width = 0, height = 0.05, alpha = 0.5) +
    theme_bw()
data_space

data_space <- ggplot(Loan_Accepted2_middle, aes(x = age, y = Subscribe)) +
    ggtitle("Subscription Based on Age") + xlab("Age") + ylab("Subscribed") +
    geom_jitter(width = 0, height = 0.05, alpha = 0.5) +
    theme_bw()
data_space

data_space +
    geom_smooth(method = "glm", se = FALSE, method.args = list(family = "binomial"))