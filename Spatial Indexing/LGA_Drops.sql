SET @poly = 'POLYGON((
40.7662 -73.8888,
40.7736 -73.8898,
40.7751 -73.8843,
40.7808 -73.8852,
40.7812 -73.8795,
40.7842 -73.8788,
40.7827 -73.8751,
40.7864 -73.8711,
40.788 -73.8673,
40.7832 -73.868,
40.7808 -73.8716,
40.773 -73.8534,
40.7697 -73.8557,
40.7673 -73.8505,
40.7645 -73.85,
40.7637 -73.8529,
40.7676 -73.856,
40.7659 -73.8594,
40.7654 -73.8625,
40.7693 -73.8672,
40.7714 -73.8732,
40.7697 -73.8871,
40.7665 -73.8866,
40.7662 -73.8888
))';



SELECT count(d_point) as LGA_Drops FROM taxidata_init where ST_Within(d_point, ST_GeomFromText(@poly)) = 1 LIMIT 0,20000000;