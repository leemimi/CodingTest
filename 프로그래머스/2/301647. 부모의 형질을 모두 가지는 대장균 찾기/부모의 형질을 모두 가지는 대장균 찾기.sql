SELECT A.ID, A.GENOTYPE, B.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA A JOIN ECOLI_DATA B ON B.ID = A.PARENT_ID
WHERE B.GENOTYPE & A.GENOTYPE = B.GENOTYPE
ORDER BY A.ID ASC
