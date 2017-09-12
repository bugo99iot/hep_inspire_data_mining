library(rworldmap)
library(RColorBrewer)

d <- data.frame(
  country=c('Italy', 'Czech Republic', 'Usa', 'France', 'Netherlands', 'Ireland', 'Norway', 'Israel', 'Australia', 'Serbia And Montenegro', 'Iceland', 'Slovenia', 'Germany', 'Armenia', 'Belgium', 'Spain', 'Canada', 'Chile', 'Denmark', 'Poland', 'Finland', 'Sweden', 'Croatia', 'Japan', 'Switzerland', 'New Zealand', 'Russia', 'Romania', 'Portugal', 'United Kingdom', 'Austria', 'Greece', 'Hungary', 'South Korea'),
  value=c(111, 24.8, 113.8, 28.1, 50.1, 83.5, 28.5, 111.3, 81.7, 29.7, 50.5, 101.9, 77.4, 44.6, 56, 56.5, 107, 22.6, 42.9, 25.4, 54.8, 59.5, 48.2, 73.7, 111.7, 126.4, 25.9, 23.7, 61.8, 112.2, 55, 131.1, 38, 32.5))




n <- joinCountryData2Map(d, joinCode="NAME", nameJoinColumn="country")


mapCountryData(n, nameColumnToPlot="value", mapTitle="Inspire data mining, UG Europe",
  xlim=c(2, 10), ylim=c(35, 66),
  colourPalette=c("moccasin","brown3"),
  addLegend=TRUE,
  oceanCol="blue", missingCountryCol="antiquewhite", lwd="1.0", borderCol
="black")
