getwd()
#importing dataset
newYork <- read_csv("D:/MS/GMU/AIT-580/Assignments/Project/Dataset.csv")
colnames(newYork) <- gsub(" ", "", colnames(newYork))
# Convert necessary columns to numeric and factor
newYork$DOFSquareFootage <- as.numeric(newYork$DOFSquareFootage)
newYork$BuildingClass <- as.factor(newYork$BuildingClass)
class(newYork$BuildingClass)
# Linear regression model
model <- lm(DOFSquareFootage ~ Borough + BuildingClass, data = newYork)
# Summary of the regression model
summary(model)

# ANOVA to test significance of the model
anova(model)
library(TukeyC)

#research question 4
newYork <- na.omit(newYork)
# Check for infinite values in the 'Street name' variable
sum(!is.finite(newYork$StreetName))
# Convert 'Street' to a factor if it's a character variable
newYork$StreetName <- as.factor(newYork$StreetName)

cluster_data <- newYork[, c("Postcode", "NumberofBuildings")]

# Perform hierarchical clustering
hc <- hclust(dist(cluster_data), method = "ward.D2")
num_clusters <- 3  
clusters <- cutree(hc, num_clusters)
newYork$Cluster <- as.factor(clusters)
library(ggplot2)
# Visualize the clusters
ggplot(newYork, aes(x = Postcode, y = NumberofBuildings, color = Cluster)) +
  geom_point() +
  labs(title = "Hierarchical Clustering of Buildings",
       x = "Zip Code",
       y = "Number of Buildings",
       color = "Cluster")




