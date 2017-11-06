###inputs : 

#input vector type :
(
preference : float
weather : char (defined by macro)
temperature : char
time : int 
location : (float,float)
gender는 M, F(남성, 여성으로 표현)
나이는 int;
)


#number of restaurant
defined by macro

#information of restaurant
(
name : string
type : char
rate : float
distance : caculated on our code
recommed result(0~1) : float
)


###outputs :
(
string of 3-top-recommended rest. 
)
(
feedbacked user preference
)

음식 종류는 설문 순서대로 0에서 11까지로 매핑
