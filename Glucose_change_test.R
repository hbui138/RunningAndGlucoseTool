data <- read.csv("data_with_qualified_running.csv")

subset1 <- subset(data, study_group_pre %in% c("healthy", "pre_diabetes_lifestyle_controlled"))
subset1$study_group_pre <- droplevels(factor(subset1$study_group_pre))
bartlett.test(delta ~ study_group_pre, data = subset1)

subset2 <- subset(data, study_group_pre %in% c("healthy", "oral_medication_and_or_non_insulin_injectable_medication_controlled"))
subset2$study_group_pre <- droplevels(factor(subset2$study_group_pre))
bartlett.test(delta ~ study_group_pre, data = subset2)

subset3 <- subset(data, study_group_pre %in% c("healthy", "insulin_dependent"))
subset3$study_group_pre <- droplevels(factor(subset3$study_group_pre))
bartlett.test(delta ~ study_group_pre, data = subset3)