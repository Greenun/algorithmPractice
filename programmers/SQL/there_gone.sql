SELECT i.ANIMAL_ID, i.NAME FROM ANIMAL_INS AS i INNER JOIN ANIMAL_OUTS AS o ON (i.ANIMAL_ID = o.ANIMAL_ID) WHERE i.DATETIME > o.DATETIME ORDER BY i.DATETIME ASC;