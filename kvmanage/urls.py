from django.urls import path 
from .views import KeyValueList , KeyValueDetail

urlpatterns = [
    path("kv/" , KeyValueList.as_view(), name="kv-list"),
    path("kv/<str:key>/" , KeyValueDetail.as_view() , name="kv-detail"),

]







'''
for admin admin

{
 
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2MTgyMDMyNCwiaWF0IjoxNzYxMjE1NTI0LCJqdGkiOiJhOWZmNjIwN2E0ODY0NGQ1YjQxZTc1MzdkN2MyMDBhMiIsInVzZXJfaWQiOiIxIn0.chI48ZgHmh8wzBwu_ZnPIk48yUwkkv_Zj2iux630s6k",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYxMjE5MTI0LCJpYXQiOjE3NjEyMTU1MjQsImp0aSI6Ijg0Y2I5YTk5ZDQ5ZTRlYWZiYmM3N2FjOWE2YTU5ZTA4IiwidXNlcl9pZCI6IjEifQ.XZsOaKQgp5DSxLMxOcFwZWRdnZVJKp3fBxduhGgl0Os"
}

for alireza abcde1234

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2MTgyMDY0OCwiaWF0IjoxNzYxMjE1ODQ4LCJqdGkiOiJjMDkzNTM2NmY0MTk0N2E1OGViZGUxMmNlMDY4MTA5YiIsInVzZXJfaWQiOiIyIn0.jUPUVhPEIW_weJrg6OWbQBFOZJbSLf1Qjp7B8GMjh1Q",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYxMjIxMTU5LCJpYXQiOjE3NjEyMTc1NTksImp0aSI6IjdhOWJhNzgxMTNhYjQ1YTY5YTU2MGU5ODJiZmU3N2ViIiwidXNlcl9pZCI6IjIifQ.Z4g0Y9JNQotNJwNAZt2qStiRV0bC9LWt7hucVc73oZY"
}


'''