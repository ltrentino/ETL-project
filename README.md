# ETL-project



ggplot(merge,aes(x=long,y=lat,group=group,fill=h.score)) + geom_polygon() + scale_fill_gradient(high="red", low="yellow", name="Happiness Score") + theme(axis.title.x=element_blank(), axis.text.x=element_blank(), axis.ticks.x=element_blank(), axis.title.y=element_blank(), axis.text.y=element_blank(), axis.ticks.y=element_blank()) + labs(title="World Happiness By Country")