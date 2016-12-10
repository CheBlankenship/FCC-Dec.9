# Change repeat js to python

# function repeatStringNumTimes(str, num) {
#   // repeat after me
#   var result ="";
#   for(var i=0; i< num; i++){
#     result += str;
#   }
#   return result;
# }
#
# repeatStringNumTimes("abc", 3);


def repeatStringNumTimes(str, num):
    result = ""
    for i in range(num):
        result+=str

    return result


print repeatStringNumTimes("sbc", 4);
