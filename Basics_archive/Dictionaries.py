# no duplicate keys in dictionaries
months = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(months.get("Lov","Not a valid key"))
# get function se u can set a default value to print if the key passed is not in dictionary 
# otherwise can also use print(months["Nov"]) like that then it will show none